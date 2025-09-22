from flask import Flask  # type: ignore
from flask_cors import CORS  # type: ignore

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello, GG!"

@app.route('/api/users')
def get_users():
    return {"users": ["Alice", "Bob", "Charlie"]}

@app.route('/api/fruits')
def get_fruits():
    return ["Apple", "Banana", "Cherry"]

if __name__ == '__main__':
    app.run(debug=True)
