#esercizio8-8
def make_album(artist, title, num_songs=None):
    album = {'artist': artist, 'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

while True:
    artist = input("Scrivi il nome dell'artista (o q per abbandonare): ")
    if artist == "q":
        break

    title = input("Scrivi il nome dell'album: ")
    if title == "q":
        break

    num_songs = input("Scrivi il numero di tracce(o scrivi Enter per saltare): ")
    if num_songs == "q":
        break

    if num_songs:
        album = make_album(artist, title, int(num_songs))
    else:
        album = make_album(artist, title)
    print(album)