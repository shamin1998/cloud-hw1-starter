import requests
import json
from decimal import Decimal
import csv
import cuisines

API_KEY = 'JpSiYrHh43GV_9dyyIeCWPBl1Uw5f6v61qlOMbfB4vjk01JZFAo4lskcpomNJ5ZuzIACvIUNqg8Fk_rvBw-_3o9rY1Hxp4Hmi5CJiIGpWMY-ItLuKMk8jRDWnpL5Y3Yx'

YELP_ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
YELP_HEADERS = {
    'Authorization': 'Bearer %s' % API_KEY,
    'Content-Type': 'application/json'
}

def get_restaurants(cuisine_type):
    restaurants = []
    for offset in range(0, 1000, 50):
        params = {
            'location': 'Manhattan',
            'term': cuisine_type,
            'limit': 50,
            'offset': offset
        }
        response = requests.get(YELP_ENDPOINT, headers=YELP_HEADERS, params=params)
        data = json.loads(response.text)
        for business in data['businesses']:
            if business['id'] not in [r['id'] for r in restaurants]:
                restaurants.append({
                    'id': business['id'],
                    'name': business['name'],
                    'address': business['location']['address1'],
                    'latitude': Decimal(str(business['coordinates']['latitude'])),
                    'longitude': Decimal(str(business['coordinates']['longitude'])),
                    'review_count': business['review_count'],
                    'rating': Decimal(str(business['rating'])),
                    'zip_code': business['location']['zip_code']
                })

    with open('data/%s_restaurants.csv' % cuisine_type, mode='w', encoding='utf-8', newline='') as csv_file:
        fieldnames = ['id', 'name', 'address', 'latitude', 'longitude', 'review_count', 'rating', 'zip_code']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for restaurant in restaurants:
            writer.writerow(restaurant)
    return restaurants

def main():
    for cuisine in cuisines.CUISINES:
        get_restaurants(cuisine)

if __name__ == '__main__':
    main()

