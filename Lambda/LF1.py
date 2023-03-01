import math
import dateutil.parser
import datetime
import time
import os
import logging
import boto3
import json
#
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
SQS = boto3.client("sqs")

""" --- Helpers to build responses which match the structure of the necessary dialog actions --- """

def getQueueURL():
    """Retrieve the URL for the configured queue name"""
    q = SQS.get_queue_url(QueueName='Q1').get('QueueUrl')
    return q
    
def record(event,slots):
    print("!!!!!!!!RECORD FUNC CALLED!!!!!!!!!!")
    """The lambda handler"""
    logger.debug("Recording with event %s", event)
    data = event.get('data')
    try:
        logger.debug("Recording %s", data)
        u = 'https://sqs.us-east-1.amazonaws.com/914175110612/DiningQueue'
        logging.debug("Got queue URL %s", u)
        resp = SQS.send_message(
            QueueUrl=u, 
            MessageBody=str(get_slots(event)["Cuisine"]),
            MessageAttributes=slots
        )
        logger.debug("Send result: %s", resp)
        print("!!!!!SQS RESPONSE!!!!!",resp)
    except Exception as e:
        raise Exception("Could not record link! %s" % e)

def get_slots(intent_request):
    return intent_request['intent']['slots']


def close(session_attributes, fulfillment_state, message, intent_name):

    print("!!!CLOSING!!! Session attr :",session_attributes,"Fullfillment:",fulfillment_state,"Message:",message)
    
    response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close",
            },
            "intent": {
                "name": intent_name,
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": message
            }
        ]
        }

    return response


def delegate(session_attributes, slots):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }




def diningSuggestions(intent_request,context,req,intent_name):
    print("!!!!!!!DINING SUGGESTIONS FUNC CALLED!!!!!!!!!!")
    location = get_slots(intent_request)["Location"]
    cuisine = get_slots(intent_request)["Cuisine"]
    # date = get_slots(intent_request)["Date"]
    time = get_slots(intent_request)["Time"]
    numberOfPeople = get_slots(intent_request)["NumberOfPeople"]
    email = get_slots(intent_request)["Email"]
    # source = intent_request['invocationSource']
    source = req['invocationSource']
    event = intent_request
    slots = {
                "Location": {
                    "StringValue": str(get_slots(event)["Location"]["value"]["originalValue"]),
                    "DataType": "String"
                },
                "Cuisine": {
                    "StringValue": str(get_slots(event)["Cuisine"]["value"]["originalValue"]),
                    "DataType": "String"
                },
                # "Date" : {
                #     "StringValue": get_slots(event)["Date"]["value"]["originalValue"],
                #     "DataType": "String"
                # },
                "Time" : {
                    "StringValue": str(get_slots(event)["Time"]["value"]["originalValue"]),
                    "DataType": "String"
                },
                # "NumPeople" : {
                #     "StringValue": str(get_slots(event)["NumberOfPeople"]["value"]["originalValue"]),
                #     "DataType": "String"
                # },
                "Email" : {
                    "StringValue": str(get_slots(event)["Email"]["value"]["originalValue"]),
                    "DataType": "String"
                }
            }
    
    record(intent_request,slots)
    return close(req['sessionState']['sessionAttributes'],
                 'Fulfilled',
                 'Your request has been received, a list of dining suggestions shall be sent to you via SMS',intent_name)


""" --- Intents --- """

def greeting(intent_request):
    print("!!!!!GREETING INTENT FUNC CALLED!!!!!!!!")
    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'Hey there, How may I serve you today?'})

def thankYou(intent_request):
    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'My pleasure, Have a great day!!'})

def probable_intent(intent_request):
    
    max_conf = -1
    intent_name = None
    for intent in intent_request['interpretations']:
        if 'nluConfidence' in intent.keys():
            if intent['nluConfidence'] > max_conf:
                max_conf = intent['nluConfidence']
                intent_name = intent
    
    return intent_name
    
def botresponse(intent_request,context):
    
    print("!!!INTENT REQUEST!!!",intent_request)
    intent = probable_intent(intent_request)
    intent_name = intent['intent']['name']
    source = intent_request['invocationSource']
    logger.debug('dispatch sessionId={}, intentName={}'.format(intent_request['sessionId'], intent_name))


    # Dispatch to your bot's intent handlers
    if intent_name == 'DiningSuggestionsIntent':
        return diningSuggestions(intent,context,intent_request,intent_name)
    elif intent_name == 'ThankYouIntent':
        return thankYou(intent_request)
    elif intent_name == 'GreetingIntent':
        return greeting(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')


""" --- Main handler --- """

SQS = boto3.client("sqs")
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request as coming from the America/New_York time zone.
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    print("!!!DEBUG!!!",event)
    logger.debug('event.bot.name={}'.format(event['bot']['name']))
    
    # u = 'https://sqs.us-east-1.amazonaws.com/914175110612/Q1'
        
    # resp = SQS.send_message(QueueUrl=u, MessageBody="Hello World!")
        
    # print(resp)
    return botresponse(event,context)
    