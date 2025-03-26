from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,FileField
from wtforms.validators import DataRequired, Length

class ProfileForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired(), Length(max=120)])
    bio = TextAreaField('Bio', validators=[Length(max=500)])
    location = StringField('Location', validators=[Length(max=100)])
    skills = StringField('Skills (comma-separated)', validators=[Length(max=255)])
    experience = TextAreaField('Experience (Job history, projects, etc.)')
    photo_url = FileField('Profile Photo')
    background_image = FileField('Background Image')
    summary = TextAreaField('Summary', validators=[Length(max=1000)])
    submit = SubmitField('Update Profile')
    
class RecommendationForm(FlaskForm):
    recommender_name = StringField('Recommender Name', validators=[DataRequired()])
    recommendation_text = TextAreaField('Recommendation', validators=[DataRequired()])
    submit = SubmitField('Update Recommendation')