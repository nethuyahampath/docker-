# import the necessary python packages 
from flask import Flask, jsonify, request
from datadog import initialize, api
import json

# import the python CORS for flask
from flask_cors import CORS

# Flask constructor takes the name of current module as argument 
app = Flask(__name__)
CORS(app)

# specified port that the server is running 
PORT = 8083

# the core api endoint to test the server funcationality 
@app.route("/")
def hello_world():
    return "Welcome"

# main function for the server.js with specified host and port values 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)