import requests
import json
import re
import csv
import argparse

from char_mappings import non_english_char_mappings

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index, Document, Boolean, Text, Object, Search, SearchAsYouType
from elasticsearch_dsl import connections, analyzer, tokenizer, char_filter, token_filter
from elasticsearch_dsl.query import MultiMatch, Match
from plu_categorizer import classify

plu_data = 'PLU_codes_full'

connections.create_connection(alias='default', hosts='192.168.56.92')

# plu_token_filter = token_filter(
#     'plu_token_filter',
#     'stop',
#     stopwords=['red', 'green', 'yellow', 'large', 'small']
# )

plu_char_filter = char_filter(
    'plu_char_filter',
    'mapping',
    mappings=non_english_char_mappings
)

# filter to replace dividers with spaces
plu_punctuation_filter_1 = char_filter(
    'plu_punctuation_filter_1',
    'pattern_replace',
    pattern='[\\/|\-,._+]',
    replacement=" "
)

plu_punctuation_filter_2 = char_filter(
    'plu_punctuation_filter_2',
    'pattern_replace',
    pattern="[^a-zA-Z0-9 ]",
    replacement=""
)

# plu_tokenizer = tokenizer('gram', 'ngram', min_gram=3, max_gram=7)

plu_analyzer = analyzer(
    'plu_analyzer',
    type='custom',
    tokenizer='lowercase',
    char_filter=[plu_char_filter, plu_punctuation_filter_1, plu_punctuation_filter_2],
    filter=['stop', 'lowercase', 'snowball'],
)

# Define mappings
class PLU(Document):
    plu  = Text(required=True)
    name = Text(required=True, analyzer=plu_analyzer)
    nutrition_info = Object()
    classification = Text(multi=True)
    retailer_assigned = Boolean()

    class Index:
        name = 'plu'
        tokenizer = 'lowercase'
        analysis = plu_analyzer
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

def get_farming_method(plu):
    '''Returns the farming method for the givenn PLU'''
    if len(plu) == 4:
        return 'conventional'
    elif len(plu) == 5:
        if plu[:1] == 8:
            return 'gmo'
        elif plu[:1] == 9:
            return 'organic'
    return 'unknown'

# Create the index
if not PLU._index.exists():
    PLU.init()

def refresh(mapping):
    mapping._index.refresh()

def load_data(plu_data=plu_data):
    missing_codes  = []
    with open(plu_data, 'r') as f:
        for line in csv.reader(f, delimiter=',', quotechar='\"'):
            (code, name) = line
            name = name.lower()

            retailer_assigned = False

            if 'retailer assigned' in name:
                retailer_assigned = True
                name = name.replace('retailer assigned ', '')

            entry_data = {
                'plu': code,
                'name': name,
                'classification': classify(name),
                'retailer_assigned': retailer_assigned
            }

            s = PLU.search()
            s.query = Match(id={'query': code})
            results = s.execute()

            if not results:
                # check if it already exists, otherwise create a new record
                plu = PLU(**entry_data)
                plu.save()
    return PLU

def exact_match(term):
    s = PLU.search()

    s.query = Match(name={'query': term})
    s.filter('term', name=term)

    return s.scan()

def prefix_match(prefix):
    s = PLU.search()

    s.query = MultiMatch(
        query=prefix,
        type='bool_prefix',
        fields=['name', 'name._2gram', 'name._3gram'],
    )

    return s.scan()

def plu_lookup(plu):
    s = PLU.search()

    s.query = Match(plu={'query': plu})

    return s.execute()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--load', help='Load data into ElasticSearch', action='store_true')
    parser.add_argument('--test', help='Run tests', action='store_true')
    args = parser.parse_args()

    if args.load:
        load_data()
        refresh(PLU)
        print('Data loaded.')

    if args.test:
        print('\n### Run Tests:')
        print('prefix match (apple):', [entry.name for entry in prefix_match('apple')])
        print('\n')
        print('exact match (apple):', [entry.name for entry in exact_match('apple')])
        print('\n')
        print('plu lookup (4133):', [entry.name for entry in plu_lookup('4133')])

        print('analyzer test: {}'.format([token.token for token in plu_analyzer.simulate('Small Gravenstein, Red Apples').tokens]))
        print('analyzer test: {}'.format([token.token for token in plu_analyzer.simulate('Jamaican Tangor (includes Ortanique, Mandor, Mandora, Tambor, Topaz, Ortanline) Tangerines/mandarins').tokens]))
