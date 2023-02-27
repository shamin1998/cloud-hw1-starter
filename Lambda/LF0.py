import json
import boto3
import logging

def lambda_handler(event, context):
    client = boto3.client('lexv2-runtime')
    
    msg = "Hey"
    
    response = client.recognize_text(
        botId='5B3QSXNZEN',
    botAliasId='CGWLJ5W2AU',
    localeId='en_US',
    sessionId='testuser',
    text=msg)
    
    msg_from_lex = response.get('messages',[])
    if msg_from_lex:
        print("Message from Lex :",msg_from_lex[0]['content'])
        print(response)
        
        resp = {
            'statusCode':200,
            'body': "Hello from LF0"
        }
    
        return resp
    