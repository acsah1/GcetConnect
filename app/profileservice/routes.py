from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from .forms import ProfileForm, RecommendationForm
from .models import Profile, Recommendation, db

from app.profileservice import profile_bp

@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    # Get user profile or create a new one if it doesn't exist
    profile = Profile.query.filter_by(user_id=current_user.id).first()

    if profile is None:
        profile = Profile(user_id=current_user.id)

    form = ProfileForm(obj=profile)

    if form.validate_on_submit():
        profile.full_name = form.full_name.data
        profile.bio = form.bio.data
        profile.location = form.location.data
        profile.skills = form.skills.data
        profile.experience = form.experience.data
        profile.summary = form.summary.data

        # For simplicity, you can handle photo and background uploads here (URLs, local storage, etc.)

        db.session.add(profile)
        db.session.commit()

        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profileservice.profile'))

    return render_template('profile.html', form=form, profile=profile)

@profile_bp.route('/profile/recommendation', methods=['GET', 'POST'])
@login_required
def add_recommendation():
    form = RecommendationForm()
    
    if not current_user.profile:
        # Flash a message or handle the case where the user does not have a profile
        flash("You need to complete your profile before adding recommendations.", "danger")
        return redirect(url_for('profileservice.view_profile')) 

    if form.validate_on_submit():
        recommendation = Recommendation(
            profile_id=current_user.profile.id,
            recommender_name=form.recommender_name.data,
            recommendation_text=form.recommendation_text.data
        )
        db.session.add(recommendation)
        db.session.commit()

        flash('Recommendation added successfully!', 'success')
        return redirect(url_for('profileservice.profile'))

    return render_template('add_recommendation.html', form=form)


@profile_bp.route('/view', methods=['GET'])
@login_required
def view_profile():
    profile = Profile.query.filter_by(user_id=current_user.id).first()
    form = ProfileForm(obj=profile)
    return render_template('profile.html', form=form,profile=profile)

@profile_bp.route('/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    profile = Profile.query.filter_by(user_id=current_user.id).first()

    if not profile:
        profile = Profile(user_id=current_user.id)

    form = ProfileForm(obj=profile)

    if form.validate_on_submit():
        profile.full_name = form.full_name.data
        profile.bio = form.bio.data
        profile.location = form.location.data
        profile.skills = form.skills.data
        profile.experience = form.experience.data

        db.session.add(profile)
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profileservice.view_profile'))

    return render_template('edit_profile.html', form=form)
