from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'votre_cle_secrete_tres_difficile_a_deviner'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation des extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)

# Configuration de Flask-Login
login_manager.login_view = 'login'  # Vue vers laquelle rediriger si non connecté
login_manager.login_message = 'Veuillez vous connecter pour accéder à cette page.'
login_manager.login_message_category = 'info'

# Importations pour éviter les dépendances circulaires
# Ces imports doivent être APRÈS l'initialisation de 'app' et 'db'
from app import routes, models

# Configuration du user_loader pour Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))