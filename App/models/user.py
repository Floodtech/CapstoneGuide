from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db


class User(db.Model, UserMixin):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)

    def __init__(self, username, password, email, first_name, last_name):
        self.username = username.lower()
        self.first_name = first_name.capitalize() 
        self.last_name = last_name.capitalize()
        self.set_password(password.lower())
        self.email = email.lower()

    def get_json(self):
        return {
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True
