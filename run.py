# from app import create_app
# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0',port=5001)

from app import create_app, db  
from app.authservice.models import User

# Create the Flask app
app = create_app()

# Use the app context explicitly
with app.app_context():
    # Here you can run your commands, e.g., flask db commands
    from flask_migrate import upgrade, init, migrate

    # Initialize database migrations
    try:
        print("Initializing migrations...")
        init()
    except Exception as e:
        print(f"Error initializing migrations: {e}")
    
    # Perform migration
    try:
        print("Running migrations...")
        migrate()
    except Exception as e:
        print(f"Error running migrations: {e}")
    
    # Apply the migration
    try:
        print("Upgrading the database...")
        upgrade()
    except Exception as e:
        print(f"Error upgrading the database: {e}")

