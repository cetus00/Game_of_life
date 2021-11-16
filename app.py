from flask import Flask, render_template
from game_of_life import GameOfLife



app = Flask(__name__)
# app.run(debug=True) # or in Terminal: export FLASK_DEBUG=1

@app.route('/')
def index():
    GameOfLife(25, 25)
    return render_template("index.html")


@app.route('/live')
def live():
    game = GameOfLife()
    if game.generation > 0:
        game.form_new_generation()
    game.generation += 1
    return render_template("live.html", game=game)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)