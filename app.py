from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/convert", methods=['POST'])    
def convert():
    print("helloooo")
    print(request.args)

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)