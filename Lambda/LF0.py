import json
import boto3
import logging

def lambda_handler(event, context):
    client = boto3.client('lexv2-runtime')
    
    msg = "Hey"
    print("@@@ EVENT @@@ ",event)
    # {'messages': [{'type': 'unstructured', 'unstructured': {'text': 'Hi'}}]}
    response = client.recognize_text(
        botId='5B3QSXNZEN',
    botAliasId='TSTALIASID',
    localeId='en_US',
    sessionId='testuser',
    text=event['messages'][0]['unstructured']['text'])
    
    print("!!! RESPONSE !!!",response)
    return response
