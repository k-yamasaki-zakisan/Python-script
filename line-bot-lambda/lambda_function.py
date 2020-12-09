import json  
import os  
import logging  
import urllib.request
import base64  
import hashlib  
import hmac

# ログ出力の準備  
logger = logging.getLogger()  
logger.setLevel(logging.INFO)  

def lambda_handler(event, context):  
    # リクエスト内容をログ出力  
    logger.info(event)  

    ###
    # 環境変数からLINEチャネルシークレットを取得  
    channel_secret = os.environ['LINE_CHANNNEL_SECRET']  
    # LINEチャネルシークレットを鍵として、HMAC-SHA256アルゴリズムを使用してリクエストボディのハッシュ値を算出  
    hash = hmac.new(channel_secret.encode('utf-8'), event['body'].encode('utf-8'), hashlib.sha256).digest()
    # ハッシュ値をBase64エンコード  
    signature = base64.b64encode(hash)

    # X-Line-Signatureを取得  
    xLineSignature = event['headers']['X-Line-Signature'].encode('utf-8')  
    # 署名の一致を検証し、不一致の場合はログ出力  
    if xLineSignature != signature:  
        logger.info('署名の不一致')  
        return {  
            'statusCode': 200,  
            'body': json.dumps('署名が正しくないみたいだよ。')  
        } 

    # 1. Webhookイベントの内容を抽出  
    body = json.loads(event['body'])  

    for event in body['events']:  
        # 応答用のメッセージオブジェクトのリストを定義  
        messages = []  
        # 2. Webhookイベントタイプがmessageであり、  
        if event['type'] == 'message':  
            # 3. メッセージタイプがtextの場合に、  
            if event['message']['type'] == 'text':  
                # 4. 受信したテキストの内容をメッセージオブジェクトとする  
                messages.append({  
                        'type': 'text',  
                        'text': event['message']['text']  
                    })  

                # 応答メッセージのリクエスト情報を定義  
                url = 'https://api.line.me/v2/bot/message/reply'  
                headers = {  
                    'Content-Type': 'application/json',  
                    # 環境変数からLINEチャネルアクセストークンを取得  
                    'Authorization': 'Bearer ' + os.environ['LINE_CHANNEL_ACCESS_TOKEN']  
                    }  
                data = {  
                    # 応答用トークンとメッセージオブジェクトを設定  
                    'replyToken': event['replyToken'],  
                    'messages': messages  
                }  
                request = urllib.request.Request(url, data = json.dumps(data).encode('utf-8'), method = 'POST', headers = headers)  
                with urllib.request.urlopen(request) as response:  
                    # レスポンス内容をログ出力  
                    logger.info(response.read().decode("utf-8"))  

    return {  
        'statusCode': 200,  
        'body': json.dumps('Hello from Lambda!')  
    }