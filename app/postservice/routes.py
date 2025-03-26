from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.postservice.models import  Post, Comment, Like
from app.postservice.forms import PostForm, CommentForm
from app import db
from app.postservice import postservice_bp

# @postservice_bp.route('/')
# @login_required
# def home():
#     posts = Post.query.all()
#     return render_template('home.html', posts=posts)

@postservice_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create.html', form=form)


@postservice_bp.route('/post/post/<int:post_id>/like', methods=['GET', 'POST'])
def like_post(post_id):
    if request.method == 'POST':
        post = Post.query.get(post_id)
        if post:
            new_like = Like(user_id=current_user.id, post_id=post_id)
            db.session.add(new_like)
            db.session.commit()
            return redirect(url_for('main.index'))
        
    # Optionally, handle GET requests (e.g., for pre-loading or displaying the like button)
    return redirect(url_for('main.index'))

# @postservice_bp.route('/post/<int:post_id>/like')
# @login_required
# def like(post_id):
#     like = Like.query.filter_by(user_id=current_user.id, post_id=post_id).first()
#     if like:
#         db.session.delete(like)
#     else:
#         db.session.add(Like(user_id=current_user.id, post_id=post_id))
#     db.session.commit()
#     return redirect(url_for('main.index'))

@postservice_bp.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def comment(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, user_id=current_user.id, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('main.index'))
