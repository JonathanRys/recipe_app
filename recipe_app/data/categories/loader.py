import requests
import json

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
                    'ingredient': line[:-1] if '\n' in line else line,
                    'type': entry
                }
                requests.put(url=url, headers=headers, data=json.dumps(entry_data))
                index += 1

if __name__ == '__main__':
    load_data(data)
    print('Data loaded.')

