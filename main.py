from flask import Flask, url_for
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
    link_hello = url_for("hello", name='мир')
    link_game = url_for("game", zero='кот')
    return f"""
        <p><a href='{link_hello}'>Нажми сюда, чтобы поздороваться!</a></p>
        <p><a href='{link_game}'>Нажми сюда, чтобы увидеть секрет!</a></p>
        """

@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {escape(name)}!'

@app.route('/game/<zero>')
def game(zero):
    return f'{10* escape(zero)}!'


if __name__ == "__main__":
    app.run(debug=True)