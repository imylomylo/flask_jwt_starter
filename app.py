from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt, create_refresh_token
from flask_cors import CORS, cross_origin

# Create a Flask app instance
app = Flask(__name__)
cors = CORS(app)

# Set up JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to your own secret key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 5  # Expiration time in seconds (60 = 1 minute)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 3600  # Refresh token expiration time in seconds (1 hour)

# set up cors
app.config['CORS_HEADERS'] = 'Content-Type'


jwt = JWTManager(app)

# Mock user database
users = {
    'user1': 'password1',
    'user2': 'password2'
}

# Authentication endpoint
@app.route('/login', methods=['POST'])
@cross_origin()
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
@cross_origin()
def logout():
    jti = get_jwt()['jti']  # JWT ID
    return jsonify({"message": "Successfully logged out"}), 200

# Token refresh endpoint
@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
@cross_origin()
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
@cross_origin()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


# Define a route and a view function
@app.route('/')
@cross_origin()
def hello():
    return 'Hello, World!'

# Run the Flask development server if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
