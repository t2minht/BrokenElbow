from flask import Flask
from search import *

choice = input("Song or Artist Search: (song/artist): ")
if choice == "song":
    songsearch()
elif choice == "artist":
    artistsearch()
