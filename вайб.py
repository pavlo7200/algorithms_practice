from flask import Flask, request, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    # Если отправили форму (POST) — считаем
    if request.method == 'POST':
        try:
            a_str = request.form.get('a', '')
            op = request.form.get('op', '')
            b_str = request.form.get('b', '')

            if not a_str or not b_str:
                raise ValueError("Пустые значения")

            a = float(a_str)
            b = float(b_str)

            if op == 'plus':
                result = a + b
                symbol = '+'
            elif op == 'minus':
                result = a - b
                symbol = '-'
            elif op == 'multiply':
                result = a * b
                symbol = '*'
            elif op == 'divide':
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль")
                result = a / b
                symbol = '/'
            else:
                raise ValueError("Неизвестная операция")

        except ValueError:
            error = "Ошибка ввода: проверьте числа и операцию"
        except ZeroDivisionError:
            error = "Деление на ноль!"

    # Отдаем HTML: форма + результат/ошибка
    html = """
    <h2>Калькулятор</h2>
    <form method="post">
      <input type="number" step="any" name="a" placeholder="Первое число" required>

      <select name="op">
        <option value="plus">+</option>
        <option value="minus">-</option>
        <option value="multiply">×</option>
        <option value="divide">÷</option>
      </select>

      <input type="number" step="any" name="b" placeholder="Второе число" required>
      <button type="submit">Посчитать</button>
    </form>
    """

    if result is not None:
        html += f"<h3>Результат: {escape(str(a))} {symbol} {escape(str(b))} = <b>{escape(str(result))}</b></h3>"
    if error:
        html += f"<p style='color:red;'><b>{escape(error)}</b></p>"

    return html


if __name__ == "__main__":
    app.run(debug=True)
