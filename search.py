import azapi

api = azapi.AZlyrics("google", accuracy=0.5)


def songsearch():
    title = input("Song:")
    api.title = title
    api.getLyrics(save = True, ext = 'txt')


def artistsearch():
    artist = input("Artist:")
    api.artist = artist
    print(api.getSongs())


