import os
from pathlib import Path

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

BASE_DIR = Path(__file__).parent
FRONT_END_DIR = BASE_DIR.parent / 'front_end'
TEMPLATE_DIR = FRONT_END_DIR / 'templates'
STATIC_DIR = FRONT_END_DIR / 'static'

app = Flask(__name__,
            template_folder=str(TEMPLATE_DIR),
            static_folder=str(STATIC_DIR),
            static_url_path='/static')


OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)