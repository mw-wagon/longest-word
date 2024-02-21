"""
This is a short game to make the longest English word from a given set of a 9 character grid
"""
import string
import random

class Game:
    """ A nine character grid is created and then words from that set are tested for validity"""

    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]


    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if word:
            if len(set(word).intersection(set(self.grid))) > 0:
                return True
        return False

    def __str__(self):
        return self.__class__.__name__

if __name__ == '__main__':
    game = Game()
