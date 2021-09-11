import azapi

api = azapi.AZlyrics("google", accuracy=0.5)


def song_search():
    a = False
    b = False
    while not(a and b):
        title = input("Song: ")
        artist = input("Artist: ")
        if title != '':
            a = True
            api.title = title
        if artist != '':
            b = True
            api.artist = artist
        if not(a and b):
            print("--------")
            print("MISSING INPUTS. TRY AGAIN")
            print("--------")
    api.getLyrics(save = False, ext = 'txt')

    print("\n" + api.title + " - " + api.artist)
    print(api.lyrics)
    print("\n------------------------")
    print(api.title + " - " + api.artist)


def artist_search():
    artist = input("Artist: ")
    api.artist = artist
    results = api.getSongs()
    print("Songs:\n")
    for title in results:
        album = (results[title])['album']
        year = (results[title])['year']
        print(title)
        if album != '':
            print("\talbum = " + album)
        if year != '':
            print("\tyear = " + year)
        print((results[title])['url'])

    song_search()


