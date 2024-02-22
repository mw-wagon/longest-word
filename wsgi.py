# pylint: disable=missing-docstring

from flask import Flask, render_template, request
from longest_word.game import Game
# import pdb; pdb.set_trace()


app = Flask(__name__)

@app.route('/')
def home():
    game = Game()
    return render_template('home.html', grid=game.grid)
    # return "this is working "

@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    score = game.get_score(word)
    return render_template('check.html', is_valid=is_valid, grid=game.grid,
                           word=word, score=score)

