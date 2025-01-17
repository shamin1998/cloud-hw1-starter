import boto3
import csv
import cuisines

def insert_restaurants(cuisine_type):
    # Set up a DynamoDB resource
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    # Set up a table object
    table = dynamodb.Table('yelp_restaurants')

    # Open the CSV file for reading
    with open('data/csvs/%s_restaurants.csv' % cuisine_type, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Insert each row into the DynamoDB table
            row['cuisine'] = cuisine_type
            table.put_item(Item=row)

if __name__ == '__main__':
    for cuisine in cuisines.CUISINES:
        insert_restaurants(cuisine)