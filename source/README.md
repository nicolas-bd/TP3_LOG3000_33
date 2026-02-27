# Source
Ce répertoire contient les différents fichiers python (.py) chargés d'exétuter les calculs de la calculatrice.
Il contient deux fichiers :

# operators.py :
Ce fichier sert à regrouper les opérations arithmétiques de base dans quatre fonctions : 
- "add", chargé de faire l'addition de deux variables.
- "substract", chargé de faire la soustraction de deux variables.
- "multiply", chargé de faire la multiplication de deux variables.
- "divide", chargé de faire la division de deux variables.

# app.py :
Ce fichier contient deux fonctions:
- "calculate", qui sert à analyser une expression et la diviser en trois parties :
    - "a", le premier opérand.
    - "b", le deuxième opérand.
    - "op_char", l'opérateur.
      la fonction trouve ensuite la fonction du fichier "operators.py" associée à l'opérateur pour l'exécuter
