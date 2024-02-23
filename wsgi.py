# pylint: disable=missing-docstring

from flask import Flask, render_template, \
    session, request
from flask_session import Session

from longest_word.game import Game
import pdb; pdb.set_trace()


app = Flask(__name__)
# Check Configuration section of Session file for more details
# SESSION_TYPE = 'redis'
SESSION_TYPE = 'filesystem'
SESSION_FILE_DIR = "/tmp/flask_session"
app.config.from_object(__name__)
Session(app)

@app.route('/')
def home():
    game = Game()
    if "score" not in session:
        session["score"] = 0
    return render_template('home.html', grid=game.grid)
    # return "this is working "

@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    score = game.score
    session["score"] = session["score"] + score
    return render_template('check.html', is_valid=is_valid, grid=game.grid,
                           word=word, score=score, global_score=session["score"])
