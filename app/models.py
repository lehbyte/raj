from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from app import raj
import bcrypt

db = SQLAlchemy(raj)
admin = Admin(raj)

class User(db.Model):
    __tablename__ = 'users'
    firstname = db.Column(db.String(127))
    lastname = db.Column(db.String(127))
    email = db.Column(db.String(120), unique=True, primary_key=True)    
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(127), unique=True)
    
    def __init__(self, username, email, password):        
        self.username = username
        self.email = email.lower()
        self.set_password(password)
    
    def set_password(self, password):
        self.password = bcrypt.hashpw(password, bcrypt.gensalt())
    
    def check_password(self, password):
        return bcrypt.checkpw(password, self.password)
    
    def __repr__(self):
        return '<Firstname: %r, Lastname: %r, Email: %r >' %\
             (self.firstname, self.lastname, self.email)

class Admin(User):        
    __tablename__ = 'admins'
    seniority = db.Column(db.Integer, unique=True)

class FoodItem(db.Model):
    __tablename__ = 'FoodItems'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.String(250), unique=True, nullable=False)
    price = db.Column(db.Float, unique=True, nullable=False)
    prep_time = db.Column(db.Integer, unique=True, nullable=False)
    #date_added = 

    def __repr__(self):
        return '<Name: %r, Price: %r, Cooktime: %r>' % (self.title, self.price, self.prep_time)

class UserView(ModelView):
    page_size = 50
    can_create = True
    can_edit = True
    can_delete = False

# Add views 
admin.add_view(UserView(User, db.session))
admin.add_view(ModelView(FoodItem, db.session))