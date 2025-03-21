from flask import Blueprint,render_template,redirect ,url_for, request,flash #request contains header information
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from .models import User
from . import db
from . import login_manager
from flask_login import login_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here 
    bemail = request.form.get('email')
    bpassword = request.form.get('password')
    bremember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=bemail).first()
    # user=''
    print("User",user.email,user.password,bemail,bpassword)
    if login(bemail, bpassword):
        flash("Login successful")
    else:
        flash("Invalid credentials")
    # # check if the user actually exists
    # # take the user-supplied password, hash it, and compare it to the hashed password in the database
    # user=<user1>
    mypassword=generate_password_hash(bpassword, method='pbkdf2:sha256')
    print("User",user.email,user.password,bemail,mypassword)
    if not user or not check_password_hash(user.password, mypassword):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))# if the user doesn't exist or password is wrong, reload the page
    # login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    if not email or not name or not password:
        flash('Please enter all the fields', category='error')
        return redirect(url_for('auth.signup'))
    
    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.login'))
    

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    # code to validate and add user to database goes here
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Load user from DB

def create_user(username, password):
    user = User(username=username)
    user.set_password(password)  # Hash and store password
    db.session.add(user)
    db.session.commit()

def login(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):  # Verify password
        login_user(user)  # Log in user
        return True
    return False

@login_required
def logout():
    logout_user()

