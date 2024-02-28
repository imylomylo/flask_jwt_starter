from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Create a Flask app instance
app = Flask(__name__)

# Set up JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to your own secret key
jwt = JWTManager(app)

# Mock user database
users = {
    'user1': 'password1',
    'user2': 'password2'
}

# Authentication endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401


# Protected endpoint
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


# Define a route and a view function
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the Flask development server if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
