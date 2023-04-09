import requests
import json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index, Document, Text, Object, Search
from elasticsearch_dsl import connections
from ..app import config

connections.create_connection(alias='default', hosts=config['ES_HOST'])
client = Elasticsearch()
s = Search(using=client)


#s.save(index='fooddata')


# Create mappings
class Ingredient(Document):
    name = Text(required=True)
    nutrition_info = Object()
    classification = Text()
    misspellings_1 = Text(multi=True)
    misspellings_2 = Text(multi=True)
    misspellings_3 = Text(multi=True)

    class Index:
        name = 'fooddata'
        settings = {"number_of_shards": 1, "number_of_replicas": 0}


# Create the index
if not Ingredient._index.exists():
    Ingredient.init()

'''
{
    "name": "apple",
    "nutrition_info": {
        s...
    },
    "misspellings_1": ["appl", "apple1" aple", "appel"],
    "misspellings_2": ["apl", "ppl", "ple"],
    "misspellings_3": ["ape"],
    "classification": ["fruit"]
}
'''

# Add data

data = {
    'alcohol': 'alcohol.txt',
    'artificial': 'artificial.txt',
    'carcinogen': 'carcinogen.txt',
    'celery': 'celery.txt',
    'dairy': 'dairy.txt',
    'egg': 'egg.txt',
    'fish': 'fish.txt',
    'fruit': 'fruit.txt',
    'grain': 'grain.txt',
    'herb': 'herb.txt',
    'insect': 'insect.txt',
    'kosher': 'kosher.txt',
    'legume': 'legume.txt',
    'mushroom': 'mushroom.txt',
    'non_vegan': 'non_vegan.txt',
    'nut': 'nut.txt',
    'oil': 'oil.txt',
    'pork': 'pork.txt',
    'poultry': 'poultry.txt',
    'processed': 'processed.txt',
    'red_meat': 'red_meat.txt',
    'rennet': 'rennet.txt',
    'seed': 'seed.txt',
    'shellfish': 'shellfish.txt',
    'spice': 'spice.txt',
    'vegetable': 'vegetable.txt',
    'wheat': 'wheat.txt',
    'yeast': 'yeast.txt'
}

headers = {
    'Content-Type': 'application/json'
}

def load_data(ingredients_data):
    index = 0
    for entry in ingredients_data:
        with open(ingredients_data[entry], 'r') as f:
            for line in f:
                url = 'http://localhost:9200/fooddata/foods/' + str(index)
                entry_data = {
                    'name': line[:-1] if '\n' in line else line,
                    'classification': entry
                }
                requests.put(url=url, headers=headers, data=json.dumps(entry_data))
                index += 1

if __name__ == '__main__':
    load_data(data)
    print('Data loaded.')

