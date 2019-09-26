import os
import pydotenv
env = pydotenv.Environment()
from sqlaclchemy import create_engine
basedir = os.path.abspath(os.path.dirname(__file__))

FLASK_ADMIN_SWATCH = 'cerulean'
TEMPLATES_AUTO_RELOAD = True

SQLALCHEMY_DATABASE_URI = 'postgresql://username:'+env['PASS']+'@localhost:5432/your_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
SECRET_KEY = 'myrestaurant'
# WHOOSH_BASE = os.path.join(basedir, 'raj.db')