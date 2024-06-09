from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
      "user1": {"username": "user1", "password": "<hashed_password>", "role": "user"},
      "admin1": {"username": "admin1", "password": "<hashed_password>", "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username

# Basic Auth protected route
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

if __name__ == "__main__":
    app.run(debug=True)
