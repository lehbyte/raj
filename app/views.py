from flask import request, render_template, redirect, url_for, g
from auth import login_manager, current_user
from functools import wraps
from flask_scss import Scss
from app import raj

app_name = "Raj's Restaurant App"
Scss(raj, asset_dir='app/assets/scss', static_dir='app/static/css')

def templated(template=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint.replace('.','/') + '.html'
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator

@raj.before_request
def before_request():
    g.user = current_user

@raj.route('/')
@raj.route('/home')
@raj.route('/index')
@templated()
def home():
    user = g.user
    return dict(title=app_name, user=user)

@raj.route('/about')
@templated('about.html')
def about():
    return dict(title=app_name)

@raj.route('/coupons')
def coupons():
    return render_template('coupons.html',title=app_name)

@raj.route('/blog')
def blog():
    return render_template('blog/index.html',title=app_name)

@raj.route('/support', methods=['GET','POST'])
def support():
    return render_template('support.html',title=app_name)