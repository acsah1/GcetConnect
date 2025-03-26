from flask import render_template
from app.main import main_bp
from app.postservice.models import Post
from app.postservice.forms import CommentForm

@main_bp.route('/')
def index():
    comment_form = CommentForm()  # Create a new instance of the form
    posts = Post.query.all()  # Fetch posts from the database
    return render_template('index.html', posts=posts, comment_form=comment_form)

    

@main_bp.route('/dashboard')
def dashboard():
    return render_template('index.html')  # Example of protected route after login


# 404 error handler
@main_bp.errorhandler(404)
def page_not_found(error):
    # Render the custom 404 error page
    return render_template('404.html'), 404

# 500 error handler
@main_bp.errorhandler(500)
def internal_server_error(error):
    # Render the custom 500 error page
    return render_template('500.html'), 500

# 400 error handler (Bad Request)
@main_bp.errorhandler(400)
def bad_request(error):
    # Render the custom error page for bad requests
    return render_template('other_errors.html'), 400

# 403 error handler (Forbidden)
@main_bp.errorhandler(403)
def forbidden(error):
    # Render the custom error page for forbidden access
    return render_template('other_errors.html'), 403

@main_bp.errorhandler(Exception)
def handle_exception(error):
    # For unhandled exceptions, we log the error and show the generic error page
    main_bp.logger.error(f"An error occurred: {error}")
    return render_template('other_errors.html'), 500

