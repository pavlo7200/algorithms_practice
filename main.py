from flask import Flask, url_for
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    link = url_for("hello", name="мир")
    return f"<a href='{link}'>Нажми сюда, чтобы поздороваться!</a>"

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {escape(name)}!'


if __name__ == "__main__":
    app.run(debug=True)
