# Module App - Application Flask Principale

## 📌 Raison d'être

Ce module constitue la logique de l'application web. Il expose une interface utilisateur permettant de réaliser des calculs mathématiques simples via une application Flask. Il gère le routage HTTP et effectue les calcules nécessaires de la requête.

## 📁 Fichiers et responsabilités

### `app.py`

- **Initialisation Flask** : Configuration de l'application avec les chemins vers les templates et fichiers statiques
- **Fonction `calculate(expr: str)`** : 
  - Parse une expression mathématique simple (format : `a op b`)
  - Opérateurs supportés : `+` `-` `*` `/`
  - Valide que l'expression contient un seul opérateur
  - Convertit les opérandes en nombres
  - Exécute l'opération via les fonctions du fichier `operators`
  - Lève des exceptions en cas d'erreur
- **Route `/`** : 
  - Affiche le formulaire de calcul (GET)
  - Traite les données du formulaire (POST)
  - Retourne le résultat ou un message d'erreur

## 🔧 Dépendances et hypothèses

### Dépendances externes
- **Flask** : Framework web pour Python
- **Module `operators`** : Module local contenant les fonctions de calcul (`add`, `subtract`, `multiply`, `divide`)

### Hypothèses structurelles
- Le dossier `front-end/` existe au niveau parent du backend et contient :
  - `front-end/templates/` : Fichier `index.html`
  - `front-end/static/` : Ressources CSS/JS statiques
- L'application s'exécute en mode debug pour le développement

