"""
===============
 Spell Checker
===============

A class used to correct mispelled words

Dependencies:
    * nltk
    * collections

Available public methods:
    * correct(string)

Available dictionaries
    * alcohol
    * artificial
    * carcinogens
    * celery
    * dairy
    * eggs
    * fish
    * fruits
    * grains
    * insects
    * legumes
    * mushrooms
    * non_vegan
    * nuts
    * oil
    * pork
    * poultry
    * processed
    * red_meat
    * rennet
    * seeds
    * shellfish
    * spices
    * vegetables
    * wheat
    * all
"""

import re
import os
import collections

from nltk.corpus import stopwords
from .data.stop_words import stop_words
from .data.whitelists import whitelists
from .data.language_codes import language_codes

dirname = os.path.dirname(__file__)


class SpellChecker:
    """
    A class used to correct mispelled words.

    Attributes:
        self.words (Counter): A unique list of counted words.
        self.stopwords (list): A list of words to remove from the ingredient.
        self.dictionaries (dict): A list of corrected words.
        self.language_codes (dict): A dictionary to look up country codes.

    """

    def __init__(self, dict_file):
        """
        Args:
            dict_file (string): The path to or key of the dictionary to be used.

        """
        self.dictionaries = whitelists['spelling']
        self.stopwords = stopwords.words('english') + stop_words
        self.language_codes = language_codes

        # Check if the dict_file is a dictionary key
        if dict_file in self.dictionaries:
            dict_file = self.dictionaries[dict_file]

        with open(dict_file) as f:
            self.words = collections.Counter(self.get_words(f.read()))

    def P(self, word):
        """Probability of `word`."""
        N = sum(self.words.values())
        return self.words[word] / N

    def correct(self, word):
        """
        Most probable spelling correction for a word.

        Args:
            word (string): A word to be corrected

        Returns (string): The corrected word 
        """
        return max(self.candidates(word), key=self.P)

    def known(self, words):
        """The subset of `words` that appear in the dictionary."""
        matches = set(w for w in words if w in self.words)
        return [x for x in matches]

    def candidates(self, word):
        """Best matches found for word."""
        lower_word = word.lower()

        corrected_word = (self.known([word])
                          or self.known([word.capitalize()])
                          or self.known([lower_word])
                          or self.known([word.upper()])
                          or self.known(self.edits1(lower_word))
                          or self.known(self.edits2(lower_word))
                          or [word])

        return corrected_word
        # return self.apply_signature(corrected_word, word)

    def edits1(self, word):
        """All edits that are one edit away from `word`."""
        letters = 'abcdefghijklmnopqrstuvwxyz-_ '
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word):
        """All edits that are two edits away from `word`."""
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

    def get_words(self, text): return re.findall(r'\w+', text.lower())

    def apply_signature(self, words, template):
        """
        Changes the case of the words to match the case of the template.

        Args:
            words: A list of words to change the case of.
            template: A template representing the desired casing.

        Returns (set):
            A set containing the re-cased words.
        """

        formatted_words = set()

        if len(template) == 0:
            return formatted_words

        default_case = self.get_default_case(template)

        for word in words:
            # Add None if the the word is None or the template is null
            if word == None or not len(word):
                formatted_words.add(None)
                continue

            # Add trailing characters to the template as needed
            while len(word) > len(template):
                template += template[-1]

            # Fix case based on the template and the default case
            formatted_word = ""
            for letter, token in zip(word, template):
                formatted_word += token if letter.lower() == token.lower() else default_case(letter)

            formatted_words.add(formatted_word)

        return [x for x in formatted_words]

    def get_default_case(self, word):
        """
        A function to find the most prevalent case used in a word.

        Args:
            word: A word to use as an example.
        Returns (function):
            Either str.upper or str.lower based on most prevalent case.

        """

        tracker = 0
        lower_letters = 'abcdefghijklmnopqrstuvwxyz'
        upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for letter in word:
            if letter in lower_letters:
                tracker -= 1
            elif letter in upper_letters:
                tracker += 1

        if tracker > 0:
            return str.upper

        return str.lower


### TESTS ###
def test():
    """Unit tests"""
    spell_checker = SpellChecker(whitelists['spelling']['all'])
    assert(spell_checker.correct("fried") == "fried")

    fruit_test = SpellChecker(whitelists['spelling']['fruits'])
    assert(fruit_test.correct("Appil") == "Apple")

    mush_test = SpellChecker(whitelists['spelling']['mushrooms'])
    assert(mush_test.correct("Portabella") == "Portobello")

    fruit_test = SpellChecker('fruits')
    assert(fruit_test.correct("Appil") == "Apple")

    veg_test = SpellChecker(whitelists['spelling']['vegetables'])
    assert(veg_test.correct("celry") == "celery")
    assert(veg_test.correct("celeryz") == "celery")
    assert(veg_test.correct("cElryz") == "cElery")

    print("All tests passed.\n")


def cmd_ln_interface():
    """A command-line interface for testing the class."""
    spell_checker = SpellChecker(whitelists['spelling']['all'])

    while True:
        input_word = input(
            "Enter a word to correct, 'z' for option[z] or 'q' to [q]uit: ")

        if input_word == 'q':
            break
        elif input_word == 'z':
            while True:
                dictionary = input(
                    "Enter dictionary name or 'all' for default: ")
                if dictionary in whitelists['spelling']:
                    spell_checker = SpellChecker(
                        whitelists['spelling'][dictionary])
                    print("Dictionary changed to:", dictionary)
                    break
                else:
                    print("\nERROR: Dictionary", dictionary, "not found.")
                    print("Please choose one of:\n    alcohol\n    artificial\n    carcinogens\n    dairy\n    eggs\n    fish\n    fruits\n    grains\n    insects\n    legumes\n    mushrooms\n    non_vegan\n    nuts\n    oil\n    pork\n    poultry\n    processed\n    red_meat\n    rennet\n    seeds\n    shellfish\n    spices\n    vegetables\n    wheat\n")
            continue
        elif " " in input_word or not len(input_word):
            print("Please enter a single word.")
            continue

        corrected_word = spell_checker.correct(input_word)

        print("Corrected word:", corrected_word)


if __name__ == '__main__':
    test()
    cmd_ln_interface()
