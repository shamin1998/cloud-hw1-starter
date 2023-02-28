import boto3
import json
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

region = 'us-east-1' # For example, us-west-1
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

host = 'https://search-restaurants-nymmlgvcnnff4nmtkpilurupiy.us-east-1.es.amazonaws.com' 
# The OpenSearch domain endpoint with https:// and without a trailing slash
index = 'restaurants'
url = host + '/' + index + '/_search'

# Lambda execution starts here
def lambda_handler(event, context):

    # Put the user query into the query DSL for more accurate search results.
    # Note that certain fields are boosted (^).
    cuisine = 'chinese'
    query = {'size': 5, 'query': {'multi_match': {'query': cuisine}}}

    # Make the signed HTTP request
    client = OpenSearch(hosts=[{
        'host': host,
        'port': 443
    }],
                        http_auth=awsauth,
                        use_ssl=True,
                        verify_certs=True,
                        connection_class=RequestsHttpConnection)
    res = client.search(index=index, body=query)
    hits = res['hits']['hits']
    results = []
    for hit in hits:
        results.append(hit['_source'])

    # Create the response and add some extra content to support CORS
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": '*'
        },
        "isBase64Encoded": False
    }

    # Add the search results to the response
    response['body'] = [result['id'] for result in results]
    return response