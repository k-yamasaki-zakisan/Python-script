from preprocessing import EnglishCorpus
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.utils import get_stop_words

from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.reduction import ReductionSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer

algorithm_dic = {"lex": LexRankSummarizer(), "tex": TextRankSummarizer(), "lsa": LsaSummarizer(),\
                 "kl": KLSummarizer(), "luhn": LuhnSummarizer(), "redu": ReductionSummarizer(),\
                 "sum": SumBasicSummarizer()}

def summarize_sentences(sentences, sentences_count=3, algorithm="lex"):
    corpus_maker = EnglishCorpus()
    preprocessed_sentences = corpus_maker.preprocessing(sentences)
    preprocessed_sentence_list = corpus_maker.make_sentence_list(preprocessed_sentences)
    corpus = corpus_maker.make_corpus()
    parser = PlaintextParser.from_string(" ".join(corpus), Tokenizer("English"))

    try:
        summarizer = algorithm_dic[algorithm]
    except KeyError:
        print(f"algorithm name:'{algorithm}'is not found.")

    summarizer.stop_words = get_stop_words("English")
    summary = summarizer(document=parser.document, sentences_count=len(corpus)*2//10)
    return summary
    
    #return " ".join([sentence.__str__() for sentence in summary])


if __name__ == "__main__":
    file = input("filename input->")
    with open(file) as f:
        sentences = f.readlines()
    sentences = ' '.join(sentences)

    result=summarize_sentences(sentences)
    for r in result:
        print(r)
