#8-6
def city_country(city,country):
    """return city -- country"""
    citycountry = f"{city}, {country}"
    return citycountry.title()

mycity = city_country('wuhan','china')
print(mycity)
mycity = city_country('tokoyo','japan')
print(mycity)
mycity = city_country('soul','koreo')
print(mycity)

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


#8-8
def make_album(singer,album,quantity=None):
    """a dictionary of music album"""
    if quantity:
        makealbum = f"{singer},{album},{quantity}"
    else:
        makealbum = f"{singer},{album}"
    return makealbum
    
while True:
    print("\nPlease input singer name:")
    print("entry 'q' when you want to quit\n")
    n_singer=input("Singer: ")
    if n_singer == 'q':
        break
    n_album = input("Album: ")
    if n_album == 'q':
        break
    n_quality = int(input("Quantity: "))
    musician= make_album(n_singer,n_album,n_quality)
    print(f"\nHello {musician}!")



    

