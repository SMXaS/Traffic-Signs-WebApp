"""Links and Machine Learning Model connections"""
from flask import Flask, render_template, url_for
app = Flask(__name__)
from keras.models import load_model

# Importing model
model = load_model("Saved_Model\model.h5")

# Link to main page
@app.route("/")
@app.route("/main")
def main():
    return render_template('main.html')

# Link to info page
@app.route('/')
@app.route("/info")
def info():
    return render_template('info.html')

# Link to game page
@app.route("/")
@app.route("/game")
def game():
    return render_template('game.html')


if __name__ == '__main__':
    app.run(debug=True)