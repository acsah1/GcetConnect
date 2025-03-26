from flask import Blueprint

postservice_bp = Blueprint('postservice', __name__, template_folder='templates')

from app.postservice import routes