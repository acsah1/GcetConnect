from flask import Blueprint,render_template
from flask_login import login_required, current_user
from . import db #. means current directory
from friend_recommend import jaccard_recommendations

main = Blueprint('main', __name__)

@main.route('/') #home
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',name=current_user.name)

@main.route('/recommend')
# @login_required
def recommend():
    user_id = current_user.id
    jr=jaccard_recommendations(user_id)
    return render_template('recommend.html',name=current_user.name)