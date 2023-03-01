import boto3
import json
import logging
from boto3.dynamodb.conditions import Key, Attr
from opensearchpy import OpenSearch, RequestsHttpConnection
from botocore.exceptions import ClientError
from requests_aws4auth import AWS4Auth

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
region = 'us-east-1' # For example, us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

def getSQSMsg():
    SQS = boto3.client("sqs")
    url = 'https://sqs.us-east-1.amazonaws.com/914175110612/DiningQueue'
    response = SQS.receive_message(
        QueueUrl=url, 
        AttributeNames=['SentTimestamp'],
        MessageAttributeNames=['All'],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )
    print("!!!!!!GET SQS RESPONSE!!!!!!!!",response)
    try:
        message = response['Messages'][0]
        if message is None:
            logger.debug("Empty message")
            return None
    except KeyError:
        logger.debug("No message in the queue")
        return None
    message = response['Messages'][0]
    SQS.delete_message(
            QueueUrl=url,
            ReceiptHandle=message['ReceiptHandle']
        )
    logger.debug('Received and deleted message: %s' % response)
    return message


def lambda_handler(event, context):
    
    """
        Query SQS to get the messages
        Store the relevant info, and pass it to the Elastic Search
    """
    print("!!!!!!!!LF2 CALLED!!!!!",)
    message = getSQSMsg() #data will be a json object
    
    if message is None:
        logger.debug("NO MESSAGE")
        return
    print("Message body returned for yelp of type :",type(message["MessageAttributes"]),"\n",message["MessageAttributes"])
    cuisine = message["MessageAttributes"]["Cuisine"]["StringValue"]
    location = message["MessageAttributes"]["Location"]["StringValue"]
    # date = message["MessageAttributes"]["Date"]["StringValue"]
    time = message["MessageAttributes"]["Time"]["StringValue"]
    numOfPeople = "N/A"
    if "NumPeople" in message["MessageAttributes"].keys():
        numOfPeople = message["MessageAttributes"]["NumPeople"]["StringValue"]
    email = message["MessageAttributes"]["Email"]["StringValue"]
    if not cuisine or not email:
        logger.debug("No Cuisine or PhoneNum key found in message")
        return
    
    # cuisine = "chinese"
    # email = "1234567890"

    """
        Query database based on elastic search results
        Store the relevant info, create the message and sns the info
    """
    
    host = "search-restaurants-nymmlgvcnnff4nmtkpilurupiy.us-east-1.es.amazonaws.com"
    index = 'restaurants'
    # query = {
    #     'size': 5,
    #     'query': {
    #         'multi_match': {
    #             'query': cuisine
    #         }
    #     }
    # }
    print("######### CUISINE ########## ", cuisine)
    query = {
        "size": 5,
        "query": {
            "function_score": {
                "query": {
                    "term": {
                        "cuisine.keyword": {
                            "value": cuisine
                        }
                    }
                },
                "functions": [
                    {
                        "random_score": {}
                    }
                ]
            }
        },
        "_source": "id"
    }
    
    # Make the signed HTTP request
    os = OpenSearch(
        hosts=[{'host': host, 'port': 443}],
        http_auth=awsauth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )

    print("$$$$$$$$ OS $$$$$$$$$$ ",os)

    res = os.search(index=index, body=query)
    print("********** OS Search Result ****** ",res)
    try:
        hits = res['hits']['hits']
    except KeyError:
        print("No HITS :(")
        return
    print("!!!!!!!!!! HITS !!!!!!!!!",hits)
    results = [hit['_source'] for hit in hits]
    ids = [result['id'] for result in results]
    
    messageToSend = "Hi! You made the following request for restaurant suggestions:\n"
    messageToSend += "\nLocation : " + location
    messageToSend += "\nNumber of people : " + numOfPeople
    messageToSend += "\nTime : " + time
    messageToSend += "\nCuisine : " + cuisine
    messageToSend += "\n\nHere are a few dining options:\n"

    # dynamodb = boto3.resource('dynamodb')
    # table_arn = 'arn:aws:dynamodb:us-east-1:267082252061:table/yelp_restaurants'
    
    # table = dynamodb.Table(resource_arn=table_arn)
    roleARN = 'arn:aws:iam::267082252061:role/Shamin_Access'
    client = boto3.client('sts')
    response = client.assume_role(RoleArn=roleARN, 
                                RoleSessionName='RoleSessionName', 
                                DurationSeconds=900)

    dynamodb = boto3.resource('dynamodb', region_name='us-east-1',
                aws_access_key_id=response['Credentials']['AccessKeyId'],
                aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                aws_session_token = response['Credentials']['SessionToken'])
    
    table_name = 'yelp_restaurants'
    table = dynamodb.Table(table_name)

    restaurant_data = []
    for id in ids:
        response = table.get_item(
            Key={
                'id': id
            }
        )
        print("RESPONSE :",response)
        restaurant_data.append(response['Item'])
    print("!!!!! DATA!!!!!!!\n",restaurant_data)

    for restaurant in restaurant_data:
        messageToSend += "\n\nRestaurant Name : " + restaurant['name']
        messageToSend += "\nAddress : " + restaurant['address'] + ", " + restaurant["zip_code"]
        messageToSend += "\nRating: " + restaurant['rating']

    client = boto3.client('ses', region_name='us-east-1')

    # Specify the email message
    sender = 'sa4129@columbia.edu'
    recipient = email
    subject = 'Restaurant suggestions for time:'+time
    body = messageToSend

    # Send the email message
    response = client.send_email(
        Source=sender,
        Destination={
            'ToAddresses': [recipient]
        },
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body}}
        }
    )

    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps("Lex LF2 responded")
    }
    