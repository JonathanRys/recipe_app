import requests
import json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index, Document, Text, Object, Search, SearchAsYouType
from elasticsearch_dsl import connections, analyzer
from elasticsearch_dsl.query import MultiMatch, Match

connections.create_connection(alias='default', hosts='192.168.56.92')

# client = Elasticsearch()
# s = Search(using=client)
# def file_to_list(stop_words):
#     words_list = []
#     with open(stop_words, 'r') as f:
#         for line in f:
#             words_list.append(line[:-1] if '\n' in line else line)
#     return words_list

ingredient_tokenizer = tokenizer("gram", "ngram", min_gram=3, max_gram=7)

ingredient_analyzer = analyzer(
    'keyword',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
    stopwords_path='stop_words.txt',
    # stop_words=file_to_list('stop_words.txt')
)

# Define mappings
class Ingredient(Document):
    name = SearchAsYouType(required=True)
    # name_kw = Text(required=True, analyzer='keyword')
    nutrition_info = Object()
    classification = Text(multi=True)
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

file_list = {
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
    for entry in ingredients_data:
        with open(ingredients_data[entry], 'r') as f:
            for line in f:
                entry_data = {
                    'name': line[:-1] if '\n' in line else line,
                    'classification': entry
                }

                # Add to classification if it exists, otherwise creat a new record
                ingredient = Ingredient(**entry_data)
                ingredient.save()

    Ingredient._index.refresh()


def match_prefix(prefix):
    s = Ingredient.search()

    s.query = MultiMatch(
        query=prefix,
        type="bool_prefix",
        fields=["name", "name._2gram", "name._3gram"],
    )

    return s.execute()

def exact_match(term):
    s = Ingredient.search()

    s.query = Match(name={"query": term})
    s.filter("term", name=term)
    # s = Search().query("match", name=term)

    return s.execute()

def suggest_match(term):
    # s = s.suggest('my_suggestion', 'pyhton', term={'field': 'title'})
    pass

if __name__ == '__main__':
    # load_data(file_list)
    print('Data loaded.')
    prefix_to_match = 'appl'
    print('match prefix ({}):'.format(prefix_to_match), ['{}:{}'.format(p.name, p.classification) for p in match_prefix(prefix_to_match)])
    print('exact match (apple):', ['{}:{}'.format(match.name, match.classification) for match in exact_match('apple')])

