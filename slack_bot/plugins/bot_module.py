from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import slackbot_settings


# メンションあり応答
@respond_to('こんにちは')
def greeting(message):
    # メンションして応答
    message.reply('こんにちは!')


# メンションあり応答
@respond_to('もうかりまっか')
def greeting(message):

    # メンションして応答
    message.send('ぼちぼちでんな')

# メンションなし応答(全体チャンネルでの発言、hubotでは全体のチャンネルを読み込む権限がないから反応しない)
@listen_to('Can someone help me?')
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')

    # Message is sent on the channel
    message.send('I can help everybody!')

    # Start a thread on the original message
    message.reply("Here's a threaded reply", in_thread=True)


@default_reply
def my_default_handler(message):
    # デフォルトリプライをsendに変更する
    message.send(slackbot_settings.DEFAULT_REPLY)