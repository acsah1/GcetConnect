from flask_login import UserMixin
from . import db #db is the object of SQLAlchemy
from flask_bcrypt import Bcrypt
bcrypt= Bcrypt()
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Encrypt password before storing
    def set_password(self, passwordx):
        self.password = bcrypt.generate_password_hash(passwordx).decode('utf-8')

    # Correct method to verify password
    def check_password(self, passwordx):
        return bcrypt.check_password_hash(self.password, passwordx)
