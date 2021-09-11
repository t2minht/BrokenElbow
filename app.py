from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods = ["POST", "GET"])
def search():
    if request.method == "POST":
        userArtist = request.form.get['userArtist']
        userSong = request.form.get['userSong']
        print(userArtist, userSong)
    return render_template("search.html")
if __name__ == "__main__":
    app.run(debug = True)