from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random
import string
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

def gen_secret_key():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = gen_secret_key()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from blueprints import auth, view
        app.register_blueprint(view, url_prefix="")
        app.register_blueprint(auth, url_prefix="/auth")

        db.create_all()

    return app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }
