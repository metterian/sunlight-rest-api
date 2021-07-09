from flask import Flask, jsonify, request


app = Flask(__name__)

# Get
@app.route("/")
def view():
    return jsonify({"key": "28,000"})
