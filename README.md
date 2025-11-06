# TP3 — LOG3000 : Calculatrice Web avec Flask

## 🎯 Objectif du projet
Ce projet vise à développer une **application web de calculatrice** en utilisant le framework **Flask (Python)**.  
L’application permet d’effectuer des opérations arithmétiques de base : addition, soustraction, multiplication et division.  
Ce travail s’inscrit dans le cadre du **TP3 du cours LOG3000**.

---

## 👥 Équipe
- **Nom de l’équipe :** 16  
- **Membres :**  
  - Mahdi Gargouri 
  - Charles Jobin 
  - Yanis Kadri   

---

## ⚙️ Prérequis
Avant d’exécuter le projet, assurez-vous d’avoir installé :
- **Python 3.10+**
- **pip**
- **Git**
- **Flask**

---

## 🧩 Installation et exécution

### 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/Mahdi01X/TP3---LOG3000.git
cd TP3---LOG3000
```

### 2️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3️⃣ Lancer le serveur Flask
```bash
python app.py
```

### 4️⃣ Accéder à l’application
Ouvrez votre navigateur et allez à :  
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧱 Structure du projet
```
TP3---LOG3000/
│
├── app.py                 # Point d’entrée du serveur Flask
├── operations.py          # Logique des opérations arithmétiques
├── static/
│   └── style.css          # Feuilles de style CSS
├── templates/
│   └── index.html         # Interface utilisateur
├── tests/                 # Dossier des tests unitaires (à venir)
├── requirements.txt       # Dépendances Python
└── README.md              # Documentation du projet
```

---

## 🧠 Documentation du code
Chaque fonction et classe du projet inclut un **docstring clair** :
- **Rôle**
- **Paramètres d’entrée**
- **Valeur de retour**

Chaque répertoire contient aussi un fichier `README.md` local expliquant :
- Le but du module
- Les fichiers qu’il contient
- Les dépendances éventuelles

---

## 🧪 Tests
Les tests unitaires se trouvent dans le dossier `tests/` et sont exécutés avec :
```bash
pytest
```
Chaque test échoué doit être documenté dans une **Issue GitHub**, avec étapes de reproduction et responsable assigné.

---

## 🔄 Flux de contribution
1. **main** → version stable du projet  
2. **dev** → développement en cours  
3. **feature/*** → nouvelles fonctionnalités ou corrections  

**Procédure :**
- Créer une branche à partir de `dev`
- Commit avec message clair
- Ouvrir une Pull Request
- Fusionner après revue et validation
