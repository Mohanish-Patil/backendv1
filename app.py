
from flask import Flask
from extensions import db, migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+mysqlconnector://root:mohanish@localhost/grocerystore"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

# Initialize database and migrations exactly once
db.init_app(app)
migrate.init_app(app, db)

# Import models so Flask-Migrate detects them
from models.user import User

# Register the controller after creating the app
from controllers.users_controller import users_bp

app.register_blueprint(users_bp, url_prefix="/api")


if __name__ == "__main__":
    app.run(debug=True)
