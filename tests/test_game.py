from longest_word.game import Game
import string
import random

class TestGame:

    def test_game_initialization(self):
            # setup
            game = Game()

            # exercise
            new_grid = game.grid

            # verify
            assert type(new_grid) == list
            assert len(new_grid) == 9 # as this is what our test word should have in it
            for character in new_grid:
                assert character in string.ascii_uppercase

            # teardown

    def test_empty_word_invalid(self):
            # setup
            game = Game()

            # verify
            assert game.is_valid("") is False

    def test_word_uses_right_letters(self):
            # setup
            game = Game()
            test_grid = "BEINLSGK"
            test_word = "BEING"
            # exercise
            game.grid = list(test_grid)
            # verify
            assert game.is_valid(test_word) is True
            # teardown
            assert game.grid == list(test_grid)

    def test_invalid_word(self):
            # setup
            game = Game()
            test_grid = "RUBBISHI"
            test_word = "AzCDEF"
            # exercise
            game.grid = list(test_grid)
            # verify
            assert game.is_valid(test_word) is False
            # teardown
            assert game.grid == list(test_grid)

    def test_no_word(self):
            # setup
            game = Game()
            test_grid = "R"
            test_word = ""
            # exercise
            game.grid = list(test_grid)
            # verify
            assert game.is_valid(test_word) is False
            # teardown
            assert game.grid == list(test_grid)

    def test_no_grd(self):
            # setup
            game = Game()
            test_grid = ""
            test_word = "RRSKDFL"
            # exercise
            game.grid = list(test_grid)
            # verify
            assert game.is_valid(test_word) is False
            # teardown
            assert game.grid == list(test_grid)

    def test_unknown_word_is_invalid(self):
        """A word that is not in the english directory should no be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
