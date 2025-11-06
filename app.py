"""
Application web Flask servant d’interface pour une calculatrice.
Ce module définit la route principale et la logique de calcul utilisée pour traiter les expressions saisies.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

# Création de l’instance Flask pour exécuter le serveur web.
app = Flask(__name__)

# Dictionnaire associant les opérateurs aux fonctions correspondantes.
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Traite une expression arithmétique simple contenant un opérateur et deux opérandes.

    Args:
        expr (str): Expression saisie par l'utilisateur.

    Returns:
        float: Résultat du calcul après traitement de l'expression.

    Raises:
        ValueError: Si l'expression est vide, mal formée ou contient plusieurs opérateurs.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Suppression des espaces pour uniformiser le format de la chaîne.
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Parcours de l'expression pour identifier le symbole opératoire.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Vérifie que l’opérateur n’est pas au début ou à la fin.
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    # Extraction des deux parties numériques.
    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Exécution de l’opération correspondante.
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application.
    Gère l'affichage de la page et le traitement du formulaire de calcul.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Exécution du serveur en mode debug.
    app.run(debug=True)