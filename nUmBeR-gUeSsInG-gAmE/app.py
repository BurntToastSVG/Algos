from flask import Flask

import random

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/secret")
def secret():
    return "<p>you found the secret </p>"

@app.route("/game")
def game():
    # secret = 1234
    # input = input("input the secret number")
    # if input == secret:
    #     print('Congradulations!')
    # elif input >= secret:
    #     print('Too many')
    # else:
    #     print('Too little')
    return render_template("game.html")
app.run(debug = True)