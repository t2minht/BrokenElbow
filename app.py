from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        userInput = request.form["nm"]
        print(userInput)
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug = True)