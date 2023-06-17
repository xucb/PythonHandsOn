#8-7
def make_album(singer,album,quantity=None):
    """a dictionary of music album"""
    if quantity:
        makealbum = {'singer':singer,'album':album,'quantity':quantity}
    else:
        makealbum = {'singer':singer,'album':album}
    return makealbum

musiciana = make_album('singer1','album1')
print(musiciana)

musicianb = make_album('singer2','album2',quantity=3)
print(musicianb)

musicianc = make_album('singer3','album3')
print(musicianc)
for singer,album in musicianc.items():
    print(f"singer is {singer.upper()} has album {album.upper()}")

