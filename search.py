import azapi

api = azapi.AZlyrics("google", accuracy=0.5)


def songsearch():
    title = input("Song: ")
    artist = input("Artist (Optional): ")
    api.title = title
    if artist != '':
        api.artist = artist
    api.getLyrics(save = False, ext = 'txt')

    print("\n" + api.title + " - " + api.artist)
    print(api.lyrics)
    print("\n------------------------")
    print(api.title + " - " + api.artist)

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


