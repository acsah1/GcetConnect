from flask import Blueprint

profile_bp = Blueprint('profileservice', __name__, template_folder='templates')

from app.profileservice import routes