# create database
import pydotenv
env = pydotenv.Environment()
from sqlaclchemy import create_engine
engine = create_engine('postgresql://lehbyte:'+env['PASS']+'@localhost:5432/raj_db')
from app import db
db.create_all()
