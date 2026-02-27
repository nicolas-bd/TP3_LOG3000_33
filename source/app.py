from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

# creating the app
app = Flask(__name__)

"""
Map of operations for the server.
Key: string representing the operator.
Value: reference to the corresponding function as defined in the operators module.
"""
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Function used to calculate the result of the expression.
    :param expr: the string to evaluate. It must follow the strict format
    <operand><operator><operand>, with both operands being positive numbers.
    :return: the result of the calculation.
    """

    if not expr or not isinstance(expr, str):
        # empty expression
        raise ValueError("empty expression")

    # remove spaces
    s = expr.replace(" ", "")

    # find the operator index
    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                # found more than one operator...
                # This means you cannot use negative numbers
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    # separate the expression to find the operands
    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        # convert the operands into proper numbers
        a = float(left)
        b = float(right)
    except ValueError:
        # the API was called with invalid operands
        raise ValueError("operands must be numbers")
    # evaluate the expression using the OPS map and return
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
# HTML handler
def index():
    """
    Function used to render the index page.
    A GET request renders the index page.
    A POST request calculates the received expression.
    The form must contain a 'display' field.
    :return: a rendered index page.
    """
    # start with an empty string
    result = ""
    if request.method == 'POST':
        # when posting, get the expression from the display
        expression = request.form.get('display', '')
        try:
            # evaluate the expression
            result = calculate(expression)
        except Exception as e:
            # expression was not correctly defined
            result = f"Error: {e}"
    # render the result
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # run the application if executed directly by the interpreter
    # prevents execution if imported as a module
    app.run(debug=True)
