from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/main")
def main():
    return render_template('main.html')

@app.route('/')
@app.route("/info")
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True)