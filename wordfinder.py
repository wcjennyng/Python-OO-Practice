"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    def __init__(self, path):
        """returns number of items in dictionary"""
        words_file = open(path)
        self.words = self.create_list(words_file)
        print(f"{len(self.words)} words read")
 
    def create_list(self, words_file):
        """creates list of words from dictionary"""
        for word in words_file:
            return word.strip()
 
    def random(self):
        """return random word"""
        return choice(self.words)

class SpecialWordFinder(WordFinder):
    def create_list(self, words_file):
        """creating list of words from dictionary without blanks or comments"""
        for word in words_file:
            if word.strip() and not words.startswith('#'):
                return word.strip()