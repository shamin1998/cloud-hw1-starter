import boto3
import json
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

region = 'us-east-1' # For example, us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

def search_restaurants(cuisine):
    host = 'search-restaurants-nymmlgvcnnff4nmtkpilurupiy.us-east-1.es.amazonaws.com'
    index = 'restaurants'
    query = {
        "size": 1,
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

    res = os.search(index=index, body=query)
    hits = res['hits']['hits']
    results = [hit['_source'] for hit in hits]
    ids = [result['id'] for result in results]
    
    return ids

def search_dynamo(ids):
    dynamodb = boto3.resource('dynamodb')
    table_name = 'yelp_restaurants'
    table = dynamodb.Table(table_name)

    restaurant_data = []
    for id in ids:
        response = table.get_item(
            Key={
                'id': id
            }
        )
        
        restaurant_data.append(response['Item'])
    
    return restaurant_data

# Lambda execution starts here
def lambda_handler(event, context):
    cuisine = event['cuisine']
    restaurant_data = search_dynamo(search_restaurants(cuisine))

    return {
        'statusCode': 200,
        'body': restaurant_data
    }