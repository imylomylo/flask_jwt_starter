from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt, create_refresh_token

# Create a Flask app instance
app = Flask(__name__)

# Set up JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to your own secret key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 5  # Expiration time in seconds (1 minute)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 3600  # Refresh token expiration time in seconds (1 hour)

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
        refresh_token = create_refresh_token(identity=username)
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

# Logout endpoint
@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']  # JWT ID
    return jsonify({"message": "Successfully logged out"}), 200

# Token refresh endpoint
@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    refresh_token = request.headers.get('Authorization').split()[1]
    try:
        new_access_token = create_access_token(identity=get_jwt_identity())
        new_refresh_token = create_refresh_token(identity=get_jwt_identity())
        return jsonify(access_token=new_access_token, refresh_token=new_refresh_token), 200
    except:
        return jsonify({"error": "Invalid refresh token"}), 401

# Custom handler for expired tokens
@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

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
