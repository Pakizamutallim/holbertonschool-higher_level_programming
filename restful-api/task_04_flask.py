from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Define the root URL
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Endpoint to return all usernames
@app.route('/data', methods=['GET'])
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)

# Endpoint to return API status
@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})

# Endpoint to return user data based on username
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.json
    username = new_user.get("username")
    if username and username not in users:
        users[username] = new_user
        return jsonify({"message": "User added", "user": new_user}), 201
    else:
        return jsonify({"error": "Username already exists or invalid data"}), 400

if __name__ == "__main__":
    app.run(debug=True)
