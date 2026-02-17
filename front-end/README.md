# Module Templates - Interface Utilisateur de la Calculatrice

## 📌 Raison d'être

Ce template constitue l'interface utilisateur de l'application calculatrice. Il affiche un formulaire interactif permettant aux utilisateurs de construire des expressions mathématiques et de les soumettre au serveur pour calcul. Le template gère l'interaction côté client et la communication avec le backend Flask.

## 📁 Fichiers et responsabilités

### `templates/index.html`

- Structure générale de l'affichage et logique locale de l'affichage
#### Boutons et actions
- **Boutons numériques** : `1`, `2`, `3`, ... `0`
  - Action : Append la valeur au champ d'affichage via `appendToDisplay()`
  - Classe CSS : `.btn`

- **Boutons opérateurs** : `+`, `-`, `*`, `/`
  - Action : Append le symbole opérateur au champ d'affichage
  - Classe CSS : `.btn .operator` (style distinct)

- **Bouton `C` (Effacer)** :
  - Action : Vide complètement le champ d'affichage via `clearDisplay()`
  - Classe CSS : `.btn`

- **Bouton `=` (Soumettre)**:
  - Type : `submit` pour soumettre le formulaire au serveur
  - Classe CSS : `.btn .operator`
  - Envoie l'expression au backend pour calcul

### `static/styles.css`

- Détermine le style des éléments du document index.html

## 🔧 Dépendances et hypothèses

### Dépendances externes
- **Flask (Jinja2)** : Moteur de template pour les variables dynamiques (`{{ result }}`, `{{ url_for() }}`)
- **Serveur Flask** : Route `/` configurée pour servir ce template avec la méthode POST

### Hypothèses structurelles
- Le serveur Flask expose `url_for()` pour générer les URLs statiques
- Le formulaire POST retourne un résultat à afficher dans le champ `result`

### Contexte Flask attendu
```python
return render_template('index.html', result=result)
```
- Variable `result` passée au template contenant le résultat du calcul ou un message d'erreur

## ⚠️ Points critiques à connaître

### Limitations
- **Pas de validation côté client** : Les expressions invalides sont envoyées au serveur (c'est volontaire, la validation se fait au backend)
- **Pas de feedback en temps réel** : Pas de vérification de l'expression avant soumission
- **Un seul opérateur supporté** : L'application ne gère que les expressions simple (a op b)