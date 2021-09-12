from flask import Flask
from search import *

choice = input("Song or Artist Search: (song/artist): ")
if choice == "song":
    song_search()
elif choice == "artist":
    artist_search()
