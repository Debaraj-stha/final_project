from flask import Blueprint,request,jsonify,redirect


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


auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return "GET request received: Render register page"
    
    if request.method == 'POST':
        try:
            data = request.json  
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
          
            if not all([username, email, password]):
                return jsonify({"error": "Missing fields"}), 400
            create_user(username, email, password)
            return jsonify({"message": "User created successfully"}), 201
        except Exception as e:
            return jsonify({"error": f"Error creating user: {str(e)}"}), 500
        

@auth('/login',methods=["GET","POST"])
def login():
    try:
        data=request.json
        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            return jsonify({"error": "Missing fields"}), 400
        
        user = User.query.filter_by(email=email).first()
        if user and User.check_password(user.password):
            return jsonify({"message": "Logged in successfully"}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": f"Error logging in: {str(e)}"}), 500
        






    
