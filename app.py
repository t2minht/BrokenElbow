from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/search", methods = ["POST"])
def search_post():
        artistName = request.form.get('artistName')
        songName = request.form.get('songName')
        
        print(artistName, songName)

if __name__ == "__main__":
    app.run(debug = True)