import os

dirname = os.path.dirname(__file__)

all_categories = ['fruit', 'seed', 'vegetable', 'nut', 'herb', 'legume']

def get_item_gen(category):
    '''Returns a generator to return each item from the given category'''
    def next_item():
        with open(os.path.join(dirname, './plu_categories/{}.txt'.format(category))) as f:
            # remove the newline character
            line = f.readline()[:-1]
            while line:
                yield line
                line = f.readline()[:-1]

    return next_item


def classify(name):
    categories = {}
    for category in all_categories:
        categories[category] = get_item_gen(category)()

    for category in categories:
        for item in categories[category]:
            if item in name:
                return category

    return 'unknown'

def test(item):
    print('{} is a {}'.format(item, classify(item)))

if __name__ == '__main__':
    test('apple')
    test('potato')
    test('small regular/red/black cherries')
    test('anise')
