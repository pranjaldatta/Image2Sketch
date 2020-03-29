from flask import Flask, render_template, request, jsonify
import sys
from server.action import action
import os


app = Flask(__name__)
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/convert", methods=['POST'])    
def convert():
    file = request.files['image'].read()
    resp = action(file)
    return resp

@app.route("/test", methods=['POST', 'GET'])
def test():
    print("Success")
    return jsonify({'status': 'success'})   

@app.route("/")
def index():
    return render_template("index.html")

@app.after_request
def after_request(response):
    print("log: setting cors" , file = sys.stderr)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
"""