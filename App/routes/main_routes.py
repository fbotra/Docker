# Importation du Blueprint, de render_template
from flask import Blueprint, render_template, request, redirect
# import du connecteur mongo/python
from pymongo import MongoClient
### import du module os pour la gestion de variable d'environement
import os

# Création d'un objet Blueprint nommé 'main_bp' avec un préfixe d'URL '/'
main_bp = Blueprint('main', __name__, url_prefix='/')

# Informations de connexion à MongoDB
mongo_host = os.getenv('MONGO_HOST', 'localhost')
mongo_port = int(os.getenv('MONGO_PORT', 27017))
mongo_db = os.getenv('MONGO_DB', 'devops')
mongo_collection = os.getenv('MONGO_COLLECTION', 'users')
mongo_username = os.getenv('MONGO_USERNAME', 'root')
mongo_password = os.getenv('MONGO_PASSWORD', 'test1234')

# Créez l'URI de connexion à MongoDB avec le nom d'utilisateur et le mot de passe
uri = f"mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}"

# Connexion à la base de données MongoDB
client = MongoClient(uri)
# Sélection de la base de données
db = client[mongo_db]
# Sélection de la collection
collection = db[mongo_collection]

@main_bp.route('/', methods=['GET'])
def read_user():
    """
    URL '/' avec la méthode GET
    Récupère les données de la collection users.
    Exclut le champ _id.
    Retourne les données des utilisateurs.
    """
    users = collection.find({}, {'_id': False})
    return render_template('index.html', users=users)

# à la suite du code précédent

@main_bp.route('/add-user', methods=['POST'])
def add_user():
    """
    URL '/add_user' avec la méthode POST
    Récupération des données du formulaire
    Retourne un message d'erreur et le code 40 si e-mail invalide
    """
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = int(request.form['age'])
    email = request.form['email']

    """
    Insertion du nouvel utilisateur dans la collection
    Redirection vers la page d'accueil après l'ajout de l'utilisateur
    """
    user_data = {'firstName': first_name, 'lastName': last_name, 'age': age, 'email': email}
    collection.insert_one(user_data)

    return redirect('/')

# import du module re pour la gestion de regex
import re

# reste du code

# Créer un foncion de validation d'email

def validate_email(email):
    """
    Valide l'adresse e-mail en utilisant une regex.
    Retourne True si l'e-mail est valide, False sinon.
    """
    emailRegex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return bool(re.match(emailRegex, email))

@main_bp.route('/add-user', methods=['POST'])
def add_user():
    """
    URL '/add_user' avec la méthode POST
    Récupération des données du formulaire
    Retourne un message d'erreur et le code 40 si e-mail invalide
    """
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = int(request.form['age'])
    email = request.form['email']

# Ajouter l'appel à la fonction

    if not validate_email(email):
        return {'error': 'Email invalide'}, 400

    """
    Insertion du nouvel utilisateur dans la collection
    Redirection vers la page d'accueil après l'ajout de l'utilisateur
    """
    user_data = {'firstName': first_name, 'lastName': last_name, 'age': age, 'email': email}
    collection.insert_one(user_data)

    return redirect('/')