README - Tests
================

Ce fichier explique comment exécuter la suite de tests ce qu'ils couvrent.

Pré-requis
----------
- Python 3.11+ (ou une version compatible installée localement)
- `requirements.txt` présent à la racine du projet (liste des dépendances pour les tests)

Installation rapide (pas d'environnement fourni)
---------------------------------------------
Ce dépôt ne fournit pas d'environnement virtuel préconfiguré. Créez-en un localement puis installez les dépendances :

```bash
# créer et activer un virtualenv (zsh / bash)
python3 -m venv env
source env/bin/activate

# installer les dépendances listées
pip install -r requirements.txt
```

Exécuter les tests
------------------
Les tests utilisent `pytest`. Après avoir activé votre virtualenv (voir ci-dessus), lancez :

```bash
# lancer toute la suite
python -m pytest -q

# lancer un fichier de tests précis (ex. tests d'UI)
python -m pytest tests/test_ui.py -q
```

Ce que couvrent les tests
-------------------------
- `tests/test_operators.py` : tests unitaires pour les fonctions arithmétiques dans `operators.py` (add, subtract, multiply, divide). Ces tests vérifient les cas normaux et quelques cas limites (nombres négatifs, zéro).

- `tests/test_app.py` : tests pour la fonction `calculate()` définie dans `app.py`. Ils vérifient :
  - le calcul pour les opérateurs `+`, `-`, `*`, `/` (format d'expression simple `a+b`),
  - le traitement des espaces,
  - la gestion des erreurs (expressions vides, opérateurs multiples, opérandes non-numériques, opérateur en première/dernière position).

- `tests/test_ui.py` : tests rapides côté serveur qui récupèrent la page HTML rendue et vérifient que :
  - les boutons attendus existent dans le HTML,
  - il n'y a pas de caractères de remplacement Unicode (\ufffd) indiquant un problème d'encodage ou de template,
  - il n'y a pas de boutons vides dans le template (les boutons devraient contenir des étiquettes visibles).
