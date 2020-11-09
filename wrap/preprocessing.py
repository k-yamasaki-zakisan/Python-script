import spacy
import neologdn
import re

class EnglishCorpus:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def preprocessing(self, text):
        text = text.replace("\n", "")
        text = neologdn.normalize(text)        

        return text

    def make_sentence_list(self, sentences):
        doc = self.nlp(sentences)
        self.ginza_sents_object = doc.sents
        sentence_list = [s for s in doc.sents]

        return sentence_list

    def make_corpus(self):
        corpus = []
        for s in self.ginza_sents_object:
            tokens = [str(t) for t in s]
            corpus.append(" ".join(tokens))

        return corpus