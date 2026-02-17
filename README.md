# Online Calculator

## Groupe 64

Une application web simple mais complète pour effectuer des calculs mathématiques de base via une interface utilisateur intuitive. 

### Portée actuelle
✅ Opérations mathématiques basiques : addition, soustraction, multiplication, division  
✅ Interface utilisateur responsive  
✅ Gestion d'erreurs au niveau du serveur
✅  Tests unitaires complets  

---

## Fonctionnalités

### Actuelles
- ✅ **Calculs de base** : Addition, soustraction, multiplication, division
- ✅ **Interface intuitive** : Clavier numérique avec boutons pour les opérateurs
- ✅ **Gestion d'erreurs** : Validation côté serveur avec messages d'erreur explicites
- ✅ **Effacement simple** : Bouton "C" pour réinitialiser l'affichage

### Limitations connues ⚠️
- ⚠️ **Un seul opérateur par expression** : Pas de support pour `5 + 3 * 2`

---

## Prérequis

Avant de commencer, assurez-vous d'avoir :

- **Python 3.8 ou supérieur** : [Télécharger Python](https://www.python.org/downloads/)
- **pip** : Gestionnaire de paquets Python (généralement inclus avec Python)
- **Git** : Pour cloner le repository
- **Navigateur web moderne** : Chrome, Firefox, Safari, Edge

### Vérifier vos installations

```bash
# Vérifier Python
python --version
# Résultat attendu : Python 3.8.x ou supérieur

# Vérifier pip
pip --version
# Résultat attendu : pip x.x.x from ...
```

---

## Installation

### Étape 1 : Cloner le repository

```bash
git clone https://github.com/votre-organisation/flask-calculator.git
cd flask-calculator
```

### Étape 2 : Créer un environnement virtuel

Il est fortement recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet.

**Sur macOS/Linux :**
```bash
python -m venv venv
source venv/bin/activate
```

**Sur Windows :**
```bash
python -m venv venv
venv\Scripts\activate
```

Vous devriez voir `(venv)` apparaître au début de votre ligne de commande.

### Étape 3 : Installer les dépendances

```bash
pip install flask
```

### Étape 4 : Vérifier la structure du projet

```bash
tree -L 2
# ou sur Windows : tree /L /F (si disponible)
```

Structure attendue :
```
flask-calculator/
├── back-end/
│   ├── app.py
│   └── operators.py

├── README.md
├── front-end/
│    ├── templates/
│    │   └── index.html
│    └── static/
│        └── style.css
└── tests/
     ├── operators-test.py
     └── app-test.py
```
---

## Utilisation

### Lancer l'application

1. Assurez-vous que votre environnement virtuel est activé (voir Étape 2)
2. Exécutez la commande :

```bash
python tests_app.py
```

3. Attendez le message :
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

4. Ouvrez votre navigateur et accédez à : `http://localhost:5000`

### Utiliser la calculatrice

#### Interface
L'application affiche une grille de boutons numérique :

```
[1] [2] [3] [+]
[4] [5] [6] [-]
[7] [8] [9] [*]
[0] [C] [=] [/]
```

#### Étapes pour effectuer un calcul

1. **Entrer le premier nombre** : Cliquez sur les boutons numériques (ex: `5`)
2. **Choisir un opérateur** : Cliquez sur `+`, `-`, `*` ou `/`
3. **Entrer le second nombre** : Cliquez sur les boutons numériques (ex: `3`)
4. **Obtenir le résultat** : Cliquez sur `=`
5. Le résultat s'affiche dans le champ en haut

#### Boutons spéciaux

- **C** : Efface le contenu du champ et prépare un nouveau calcul
- **=** : Soumet l'expression au serveur pour calcul

#### Messages d'erreur

Vous pouvez rencontrer les erreurs suivantes :

| Erreur | Cause | Solution |
|--------|-------|----------|
| `Error: empty expression` | Le champ était vide au moment du submit | Entrez une expression valide |
| `Error: only one operator is allowed` | Vous avez entré deux opérateurs (ex: `5 + 3 *`) | Utilisez une seule opération à la fois |
| `Error: invalid expression format` | Opérateur au début/fin ou pas trouvé | Format correct : `nombre opérateur nombre` |
| `Error: operands must be numbers` | Les opérandes ne sont pas des nombres | Utilisez uniquement des chiffres |

### Arrêter l'application

Appuyez sur **Ctrl+C** dans le terminal où Flask s'exécute.

---


## Tests

### État actuel

✅ **Tests unitaires complets** couvrant :
- Les 4 opérations mathématiques (addition, soustraction, multiplication, division)
- Les cas d'erreur (division par zéro, expression vide, format invalide, opérandes non numériques)
- **Couverture** : 8 tests couvrant tous les chemins critiques de la fonction `calculate()`

### Structure des tests

```
tests/
├── __init__.py
├── test_app.py               # Tests des routes Flask
└── test_operators.py         # Tests unitaires des opérateurs
```

### Prérequis pour les tests

Les tests utilisent le module `unittest` inclus dans Python. Optionnellement, vous pouvez installer pytest :

```bash
pip install pytest pytest-flask
```

### Exécuter les tests

#### Avec unittest (configuration actuelle)

```bash
# Exécuter tous les tests
python tests/test_app.py

# Avec sortie verbose
python tests/test_app.py -v

# Exécuter un test spécifique
python tests/test_app.py MyTestCase.test_addition

# Via la ligne de commande
python -m unittest tests.test_app -v
```

### Couverture des tests

#### ✅ Opérations arithmétiques valides

| Test | Expression | Résultat attendu |
|------|-----------|------------------|
| `test_addition` | `"2+3"` | `5` |
| `test_substraction` | `"5-3"` | `2` |
| `test_multiplication` | `"5*3"` | `15` |
| `test_division` | `"9/3"` | `3` |

#### ⚠️ Gestion des erreurs

| Test | Expression | Exception | Message |
|------|-----------|-----------|---------|
| `test_division_by_zero` | `"5/0"` | `ZeroDivisionError` | - |
| `test_empty` | `""` | `ValueError` | `"empty expression"` |
| `test_multiple_operators` | `"2++3"` | `ValueError` | `"only one operator is allowed"` |
| `test_invalid_format` | `"52+"` | `ValueError` | `"invalid expression format"` |
| `test_not_a_number` | `"a+b"` | `ValueError` | `"operands must be numbers"` |

### Résultat attendu

Lors d'une exécution réussie :

```
........
----------------------------------------------------------------------
Ran 8 tests in 0.002s

OK
```
### Modules clés

Pour une documentation détaillée de chaque module, consultez :

- **[back-end](./README.md)** - Application Flask principale
- **[front-end](./README.md)** - Interface utilisateur

### Flux de données

```
Utilisateur clique sur boutons
          ↓
JavaScript: appendToDisplay()
          ↓
Champ HTML accumule l'expression
          ↓
Utilisateur clique sur "="
          ↓
Form POST envoyé à /
          ↓
app.py: calculate(expression)
          ↓
operators.py: opération math (add/subtract/multiply/divide)
          ↓
Résultat retourné à template
          ↓
index.html affiche le résultat
```

---

## Contribution

### Bienvenue ! 🎉

Nous accueillons les contributions de tous les niveaux. Que vous trouviez un bug, proposiez une fonctionnalité ou amélioriez la documentation, votre aide est précieuse.

### Workflow de contribution

#### 1. Créer une branche

```bash
# Mettre à jour main
git checkout main
git pull origin main

# Créer une branche descriptive
git checkout -b feature/mon-amelioration
# ou
git checkout -b fix/mon-bug-fix
# ou
git checkout -b docs/update-readme
```

#### 2. Effectuer vos modifications

```bash
# Développer et tester localement
python tests_app.py

# Exécuter les tests
pytest

# Vérifier la qualité du code
# (pylint, black, flake8 à ajouter plus tard)
```

#### 3. Committer vos changements

```bash
# Voir les fichiers modifiés
git status

# Ajouter les fichiers pertinents
git add tests_app.py operators.py

# Committer avec un message descriptif
git commit -m "fix: corriger la division entière dans operators.divide()"
```

#### 4. Pousser et créer une Pull Request

```bash
# Pousser votre branche
git push origin feature/mon-amelioration
```

Puis sur GitHub :

1. Cliquez sur **Compare & pull request**
2. Remplissez le template de PR :

```markdown
## Description
Qu'est-ce que cette PR change ?

## Type de changement
- [ ] Bug fix
- [ ] Nouvelle fonctionnalité
- [ ] Documentation
- [ ] Autre

```

3. Un mainteneur examinera votre PR

### Signaler un bug ou proposer une fonctionnalité

#### Créer une issue

1. Allez dans l'onglet **Issues** du repository
2. Cliquez sur **New issue**
3. Remplissez le template :

```markdown
## Description du problème
Décrivez le bug ou la fonctionnalité demandée

## Étapes à reproduire (pour les bugs)
1. Aller à ...
2. Cliquer sur ...
3. Observer ...

## Comportement attendu
Ce qui devrait se passer

## Comportement actuel
Ce qui se passe réellement
```