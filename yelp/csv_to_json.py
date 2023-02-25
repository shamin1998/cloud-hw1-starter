import csv
import json
import cuisines

def csv_to_json(cuisine_type, csv_path, json_path):
    restaurants = []
    with open(csv_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row['cuisine'] = cuisine_type
            restaurants.append(row)

    indexed_data = []
    for restaurant in restaurants:
        indexed_data.append({
            'index': {
                '_index': 'restaurants',
                '_id': restaurant['id']
            }
        })
        indexed_data.append({
            'id': restaurant['id'],
            'cuisine': restaurant['cuisine']
        })

    with open(json_path, mode='w', encoding='utf-8') as json_file:
        for item in indexed_data:
            json.dump(item, json_file)
            json_file.write('\n')

if __name__ == '__main__':
    for cuisine in cuisines.CUISINES:
        csv_to_json(cuisine, "data/%s_restaurants.csv" % cuisine, "data/%s_restaurants.json" % cuisine)