"""
This is a short game to make the longest English word from a given set of a 9 character grid
"""
import string
import random
import requests

class Game:
    """ A nine character grid is created and then words from that set are tested for validity"""

    def __init__(self, score=0) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]
        self.score = score

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if word: #for blanks
            if len(set(word).intersection(set(self.grid))) > 0 : # that uses letters in grid
                return self.__check_dictionary(word) # that is a word in English
        return False

    @staticmethod
    def __check_dictionary(word):
        word_good_bad = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}").json()
        return word_good_bad['found']

    def __str__(self):
        return self.__class__.__name__

    def get_score(self, word):
        self.score += len(word)
        return self.score


if __name__ == '__main__':
    game = Game()
