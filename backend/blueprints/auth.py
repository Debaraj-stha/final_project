from flask import Blueprint

from app import db,User
auth = Blueprint('auth', __name__)
def create_user(username, email, password):
    new_user = User(
        username=username,
        email=email
    )
    new_user.set_password(password)
    db.session.add(new_user)      
    db.session.commit()              
    return new_user
@auth.route('/login', methods=['GET', 'POST'])
def login():
    try:
        create_user("jhon","jhon@gmail.com","jhon122")
        return "user created"
    except Exception as e:
        return "Error creating user: " + e.message
    
