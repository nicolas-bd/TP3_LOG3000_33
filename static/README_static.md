# Module Static

## 🎯 Raison d’être
Le dossier `static/` contient les fichiers statiques utilisés par l’application Flask.  
Ces fichiers ne changent pas dynamiquement et sont envoyés tels quels au navigateur.

## 📁 Contenu
- **style.css** : feuille de style principale de la calculatrice.

## 🧩 Rôle du fichier style.css
- Définit la mise en page générale de la page HTML.
- Centre la calculatrice à l’écran et applique un thème sombre.
- Gère l’apparence des boutons, du champ d’affichage et des textes.
- Ajoute des effets visuels simples (ombrage, survol, transitions).

## 🔗 Dépendances
- Chargé dans `index.html` via Flask à l’aide de la fonction `url_for()` :
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  ```

## 🧭 Navigation
- Le dossier `static/` est le répertoire par défaut pour tous les fichiers CSS, JS ou images utilisés par Flask.
- Toute modification du style visuel de la calculatrice se fait ici.
