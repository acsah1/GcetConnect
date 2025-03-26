from flask import Blueprint

auth_bp = Blueprint('authservice', __name__, template_folder='templates')

from app.authservice import routes

