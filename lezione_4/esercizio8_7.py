#esercizio8-7
def make_album (artist, title, num_song = None):
    album =  {"artist": artist, "name": title}
    if num_song:
        album['num. songs'] = num_song
    return album

album1 = make_album("thasup", 236451, 20)
album2 = make_album("sfera ebbasta", "X2VR")
album3 = make_album("lazza", "LOCURA")
print (album1)
print (album2)
print (album3)