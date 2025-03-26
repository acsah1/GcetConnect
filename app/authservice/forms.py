from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,TextAreaField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from wtforms.validators import DataRequired, Length
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    



