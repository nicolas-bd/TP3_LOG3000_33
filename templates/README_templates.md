# Module Templates

## 🎯 Raison d’être
Le dossier `templates/` contient les fichiers HTML utilisés par le serveur Flask pour générer les pages web de l’application.  
Flask recherche automatiquement les modèles HTML dans ce dossier lorsqu’une route appelle la fonction `render_template()`.

## 📁 Contenu
- **index.html** : page principale de la calculatrice.  
  Elle définit :
  - le champ d’affichage du résultat (`<input id="display">`) ;
  - les boutons numériques (0–9) et opératoires (+, −, ×, ÷) ;
  - le bouton `=` pour soumettre le formulaire au serveur Flask ;
  - le bouton `C` pour réinitialiser l’affichage.

  Le code JavaScript intégré gère :
  - la mise à jour du champ d’affichage lors de la saisie ;
  - la réinitialisation du champ (`clearDisplay()`).

## 🔗 Dépendances
- Appelé depuis `app.py` via la fonction :
  ```python
  render_template('index.html', result=result)
  ```
- Le fichier charge la feuille de style `style.css` depuis le dossier `static/`.
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  ```

## 🧭 Navigation
- Le fichier `index.html` est la seule vue utilisée par l’application.
- Lorsqu’un utilisateur accède à la route `/`, Flask rend ce modèle et insère dynamiquement la variable `result`.
