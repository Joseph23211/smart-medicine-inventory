
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Smart Medicine Inventory System</h1>
    <h2>ABC-VED Based Inventory Management</h2>
    <p>Flask application is running successfully!</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
