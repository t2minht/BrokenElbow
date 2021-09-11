import azapi

api = azapi.AZlyrics("google", accuracy=0.5)


def songsearch():
    title = input("Song: ")
    api.title = title
    api.getLyrics(save = False, ext = 'txt')
    print(api.lyrics)

def artistsearch():
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

    songsearch()


