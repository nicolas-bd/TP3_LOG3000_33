# Devoir3-LOG3000
## Équipe #48
TP 3 en Log3000, contenant le code d'une calculatrice en ligne.

## Objectif: 
Voici un repo git permettant de faciliter la compréhension du code pour les nouveaux membres de l'équipe. Notre but est la correction des problèmes 
dans le code ainsi que la documentation du travail déjà fait.

## Prérequis d'installation:
Pour effectuer l'installation complète du projet, il faut s'assurer d'effectuer les étapes suivantes :
- Se créer un compte GitHub.
- Installer Git.
- Installer les paquets de Python et de Pip.
- Installer un environnement de développement de logiciel (IDE).

## Instructions d'installation:
pour installer le projet, vous devez :
- Créer un nouveau dossier dans l'emplacement de votre choix.
- Ouvrir le terminal intégré dans le dossier.
- Cloner le projet à l'aide de la commande: "git clone https://github.com/nicolas-bd/TP3_LOG3000_33.git".
- Ouvrir le dossier à l'aide de votre IDE.
- Ouvrir le terminal intégré du répertoire source et entrer la commande "py -m pip install flask".

## Utilisation
Pour utiliser le programme, il faut:
- Ouvrir le fichier "app.py".
- Démarrer le programme à l'aide de la flèche verte en haut de la fenêtre.
- Copier l'adresse locale du projet qui a été affichée dans la console.
- Coller cette adresse dans un navigateur web.

Le programme ouvert est constitué d'une calculatrice pouvant effectuer des additions, des soustractions, des multiplication et des divisions.
Il faut entrer le numéro de son choix, puis l'opération choisie, et finalement entrer un deuxième numéro.
La touche "=" fera afficher la réponse dans la zone désignée, et fera afficher un message d'erreur en cas de problème.
La touche "C" fera nettoyer le champ de saisie.

## Tests
Vous pourrez trouver tous les tests du projet dans le dossier "src/tests".

### Prérequis
- Installer Python.
- Installer "pytest" à l'aide de la commande "python -m pip install pytest".


### Exécuter les tests
Depuis la racine du projet (*Devoir3-LOG3000*), lancer :
- Tous les tests :
  - `python -m pytest -v`
- Un fichier de test précis :
  - `python -m pytest -v src/tests/test_operators.py`
- Un test précis :
  - `python -m pytest -v src/tests/test_operators.py::test_add`

### Ajouter des tests plus tard
Pour ajouter de nouveaux tests :
- Créer (ou compléter) un fichier `test_*.py` dans *src/tests*.
- Nommer chaque fonction de test avec le préfixe `test_`.
- Utiliser des `assert` pour valider les résultats attendus.

## Contributions
- NicolasBilodeau?? (?/?/?) : Création du projet initial
- TCholette (02/27/2026) : Rédaction des documents ReadMe 
- AlonsoVidalHerrera?? (02/27/2026) : Rédaction de la documentation

