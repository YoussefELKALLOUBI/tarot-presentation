# Tarot Presentation 🔮

Projet Django développé avec l'architecture MVC présentant le tarot dans le monde, sans base de données.

## 🚀 Démo en ligne

Consultez directement : [https://tarot-presentation.onrender.com/](https://tarot-presentation.onrender.com/)

## 📋 Fonctionnalités

- Navigation entre les pages avec un menu
- Gestion des exceptions 404 (testez avec `url/adressenonexistante`)
- Architecture Django MVC

## 🛠️ Installation

### Option 1 : Installation locale avec pip

1. Clonez le projet :
```bash
git clone https://github.com/YoussefELKALLOUBI/tarot-presentation.git
cd tarot-presentation
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Lancez le serveur :
```bash
python manage.py runserver
```

4. Accédez à l'application : `http://localhost:8000`

### Option 2 : Avec Docker

1. Clonez le projet :
```bash
git clone https://github.com/YoussefELKALLOUBI/tarot-presentation.git
cd tarot-presentation
```

2. Construisez et lancez avec Docker Compose :
```bash
docker-compose up --build
```

3. Accédez à l'application : `http://localhost:8000`

## 🏗️ Architecture

- **Framework** : Django (architecture MVC)
- **Frontend** : HTML, CSS, JavaScript
- **Base de données** : Aucune
- **Déploiement** : Render.com

## 🔧 Test de la gestion 404

Testez la gestion des erreurs 404 en accédant à : `votre-url/adressenonexistante`

---

**Auteur** : Youssef ELKALLOUBI  
