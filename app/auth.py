import functools
from app import raj
from app.models import User, db
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask import ( Blueprint, flash, redirect, render_template, request, url_for, g)

bp = Blueprint('auth', __name__, url_prefix='/auth')

login_manager = LoginManager()
login_manager.init_app(raj)


db.create_all()
db.session.commit()

# Sign Up view
@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST': 
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        user_name = request.form['username']
        user_email = request.form['email']
        user_password = request.form['password']
        
        error = None
        
        if not user_name or firstname or lastname:
            error = 'All names are required.'
        elif not user_email:
            error = 'Email is required.'
        elif User.query.filter_by(email=user_email).first() is not None:
            error = 'The User {} is already registered.'.format(username)
        elif not user_password:
            error = 'Password can not be empty!'

        if error is None:
            db.session.add( User(username=user_name, email=user_email, password=user_password) )
            db.session.commit()
            return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/signup.html')

# Login view
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        user_password = request.form['password']        
        
        error = None        
        user_u = User.query.filter_by(username=user_name).first()

        if user_u is None:
            error = 'Username does not exist.'
        elif not user_u.check_password(user_password):
            error = 'Incorrect password.'

        if error is None:
            # session.clear()
            # session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    # session.clear()
    db.session.close()
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(email):
    return User.query.get(str(email))