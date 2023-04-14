import os

dirname = os.path.dirname(__file__)

whitelists = {
    "spelling": {
        "alcohol": os.path.join(dirname, 'dictionaries/spelling_alcohol.txt'),
        "artificial": os.path.join(dirname, 'dictionaries/spelling_artificial.txt'),
        "carcinogens": os.path.join(dirname, 'dictionaries/spelling_carcinogens.txt'),
        "dairy": os.path.join(dirname, 'dictionaries/spelling_dairy.txt'),
        "eggs": os.path.join(dirname, 'dictionaries/spelling_eggs.txt'),
        "fish": os.path.join(dirname, 'dictionaries/spelling_fish.txt'),
        "fruits": os.path.join(dirname, 'dictionaries/spelling_fruits.txt'),
        "grains": os.path.join(dirname, 'dictionaries/spelling_grains.txt'),
        "insects": os.path.join(dirname, 'dictionaries/spelling_insects.txt'),
        "legumes": os.path.join(dirname, 'dictionaries/spelling_legumes.txt'),
        "mushrooms": os.path.join(dirname, 'dictionaries/spelling_mushrooms.txt'),
        "non_vegan": os.path.join(dirname, 'dictionaries/spelling_non_vegan.txt'),
        "nuts": os.path.join(dirname, 'dictionaries/spelling_nuts.txt'),
        "oil": os.path.join(dirname, 'dictionaries/spelling_oil.txt'),
        "pork": os.path.join(dirname, 'dictionaries/spelling_pork.txt'),
        "poultry": os.path.join(dirname, 'dictionaries/spelling_poultry.txt'),
        "processed": os.path.join(dirname, 'dictionaries/spelling_processed.txt'),
        "red_meat": os.path.join(dirname, 'dictionaries/spelling_red_meat.txt'),
        "rennet": os.path.join(dirname, 'dictionaries/spelling_rennet.txt'),
        "seeds": os.path.join(dirname, 'dictionaries/spelling_seeds.txt'),
        "shellfish": os.path.join(dirname, 'dictionaries/spelling_shellfish.txt'),
        "spices": os.path.join(dirname, 'dictionaries/spelling_spices.txt'),
        "vegetables": os.path.join(dirname, 'dictionaries/spelling_vegetables.txt'),
        "wheat": os.path.join(dirname, 'dictionaries/spelling_wheat.txt'),
        "yeast": os.path.join(dirname, 'dictionaries/spelling_yeast.txt'),
        "unidentified": os.path.join(dirname, 'dictionaries/spelling.dict')
    },
    "categories": {
        "alcohol": os.path.join(dirname, 'categories/alcohol.txt'),
        "artificial": os.path.join(dirname, 'categories/artificial.txt'),
        "carcinogens": os.path.join(dirname, 'categories/carcinogens.txt'),
        "dairy": os.path.join(dirname, 'categories/dairy.txt'),
        "eggs": os.path.join(dirname, 'categories/eggs.txt'),
        "fish": os.path.join(dirname, 'categories/fish.txt'),
        "fruits": os.path.join(dirname, 'categories/fruits.txt'),
        "grains": os.path.join(dirname, 'categories/grains.txt'),
        "insects": os.path.join(dirname, 'categories/insects.txt'),
        "legumes": os.path.join(dirname, 'categories/legumes.txt'),
        "mushrooms": os.path.join(dirname, 'categories/mushrooms.txt'),
        "non_vegan": os.path.join(dirname, 'categories/non_vegan.txt'),
        "nuts": os.path.join(dirname, 'categories/nuts.txt'),
        "oil": os.path.join(dirname, 'categories/oil.txt'),
        "pork": os.path.join(dirname, 'categories/pork.txt'),
        "poultry": os.path.join(dirname, 'categories/poultry.txt'),
        "processed": os.path.join(dirname, 'categories/processed.txt'),
        "red_meat": os.path.join(dirname, 'categories/red_meat.txt'),
        "rennet": os.path.join(dirname, 'categories/rennet.txt'),
        "seeds": os.path.join(dirname, 'categories/seeds.txt'),
        "shellfish": os.path.join(dirname, 'categories/shellfish.txt'),
        "spices": os.path.join(dirname, 'categories/spices.txt'),
        "vegetables": os.path.join(dirname, 'categories/vegetables.txt'),
        "wheat": os.path.join(dirname, 'categories/wheat.txt'),
        "yeast": os.path.join(dirname, 'categories/yeast.txt')
    }
}
