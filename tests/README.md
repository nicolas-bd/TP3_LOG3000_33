# Tests Unitaires - Calculatrice

## Description

Ce projet contient une suite de tests unitaires pour une fonction `calculate()` qui effectue des opérations mathématiques simples. Les tests couvrent les cas nominaux ainsi que les gestion des erreurs.

## Structure du projet

```
.
├── back_end/
│   └── app.py              # Contient la fonction calculate()
├── test_suite.py           # Fichier des tests unitaires
└── README.md               # Ce fichier
```

## Prérequis

- Python 3.6 ou supérieur
- Aucune dépendance externe requise (utilise le module `unittest` de la stdlib)

## Comment exécuter les tests

### Exécution de tous les tests

```bash
python test_suite.py
```

### Exécution avec verbose (affichage détaillé)

```bash
python test_suite.py -v
```

### Exécution d'un test spécifique

```bash
python test_suite.py MyTestCase.test_addition
```

### Exécution avec unittest depuis la ligne de commande

```bash
python -m unittest test_suite.py -v
```

## Couverture des tests

La suite de tests couvre les fonctionnalités et cas d'erreur suivants :

### ✅ Opérations arithmétiques valides

| Test | Description | Exemple | Résultat attendu |
|------|-------------|---------|------------------|
| `test_addition` | Addition de deux nombres | `"2+3"` | `5` |
| `test_substraction` | Soustraction de deux nombres | `"5-3"` | `2` |
| `test_multiplication` | Multiplication de deux nombres | `"5*3"` | `15` |
| `test_dicision` | Division de deux nombres | `"9/3"` | `3` |

## Résultat attendu

Lors de l'exécution réussie des tests, vous devriez voir :

```
........
----------------------------------------------------------------------
Ran 8 tests in X.XXXs

OK
```
 les permissions d'exécution sont correctes sur le fichier test