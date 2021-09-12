from flask import Flask, redirect, url_for, render_template, request
from search import *

app = Flask(__name__)

lyrics = azapi.AZlyrics("google", accuracy=0.5)

@app.route("/")
def search():
    return render_template("search.html")


@app.route("/", methods=["POST"])
def search_post():
    artistName = request.form.get('artistName')
    songName = request.form.get('songName')

    lyrics.artist = artistName
    lyrics.title = songName

    lyrics.getLyrics(save = False, ext = 'txt')

    return redirect(url_for('results'))


@app.route("/results")
def results():
    return render_template("results.html", text=lyrics.lyrics.split("\n"))


if __name__ == "__main__":
    app.run(debug=True)
