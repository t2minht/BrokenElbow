from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    return render_template("search.html")



if __name__ == "__main__":
    app.run(debug = True)