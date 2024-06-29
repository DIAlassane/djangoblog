# Projet Blog Multilingue avec Chatbot

Ce projet est un blog multilingue développé avec Django, intégrant un chatbot utilisant un modèle de langage (GPT)

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- Python (de préférence Python 3.x)
- Django
- openai (pour l'intégration avec GPT)
- python-dotenv (pour les variables d'environnement)

Assurez-vous également d'avoir une clé api Openai valide si vous prévoyez d'utiliser GPT.

## Installation

1. **Clonage du Repository :**

   Clonez ce repository sur votre machine locale :

   ```bash
   https://github.com/DIAlassane/djangoblog.git
   cd multilang_site

2. **Installez les dépendances :**
   
   pip install -r requirements.txt

3. **Configuration de l'environnement :**

   SECRET_KEY='votre_clé_secrète_django'
   AI_KEY='votre_clé_secrète_openai'

4. **Migrations et création de la base de données :**

   python manage.py makemigrations
   python manage.py migrate

5. **Démarrage du serveur Django :**

   python manage.py runserver

Accès à l'application : http://127.0.0.1:8000/
