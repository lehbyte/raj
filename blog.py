flask flask import( Blueprint, flash, g, redirect, render_template, request, url_for )
from werkzeug.exceptions import abort
from raj.views import db

bp = Blueprint('blog', __name__)