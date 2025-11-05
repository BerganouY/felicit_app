import os
from app import app, db

# --- Correction ---
# @app.before_first_request n'existe plus.
# Nous allons créer la base de données en poussant un "contexte d'application"
# manuellement avant de lancer l'application.

# Crée le répertoire 'instance' s'il n'existe pas
# Le fichier 'site.db' sera stocké ici par défaut.
instance_path = os.path.join(os.path.dirname(__file__), 'instance')
if not os.path.exists(instance_path):
    os.makedirs(instance_path)

# Pousse un contexte d'application pour que db.create_all()
# sache quelle configuration utiliser (celle de 'app')
with app.app_context():
    db.create_all()

# --- Fin de la correction ---


if __name__ == '__main__':
    app.run(debug=True)