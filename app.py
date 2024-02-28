from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the Flask development server if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
