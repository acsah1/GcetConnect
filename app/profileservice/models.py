from app import db
from flask_login import UserMixin,current_user
from datetime import datetime

# class Profile(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
#     full_name = db.Column(db.String(120), nullable=False)
#     bio = db.Column(db.Text, nullable=True)
#     location = db.Column(db.String(100), nullable=True)
#     skills = db.Column(db.String(255), nullable=True)  # Comma-separated list
#     experience = db.Column(db.Text, nullable=True)  # JSON or plain text for now
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

#     def __repr__(self):
#         return f'<Profile {self.full_name}>'
    
class Profile(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(100), nullable=True)
    skills = db.Column(db.String(255), nullable=True)  # Comma-separated list
    experience = db.Column(db.Text, nullable=True)
    photo_url = db.Column(db.String(255), nullable=True)  # URL to user's photo
    background_image = db.Column(db.String(255), nullable=True)  # URL to background image
    summary = db.Column(db.Text, nullable=True)
    recommendations = db.relationship('Recommendation', backref='profile', lazy=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Profile {self.full_name}>'
class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    recommender_name = db.Column(db.String(120), nullable=False)
    recommendation_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Recommendation by {self.recommender_name}>'