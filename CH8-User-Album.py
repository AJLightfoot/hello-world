def make_album(artist_nm, album_nm):
    album_info = {'artist': artist_nm, 'album': album_nm}
    return album_info

while True:
    print("\nPlease Enter an music artist and album title:")
    print("(you can quit by entering q at anytime)")
    artist_name = input("Artist: ")
    if artist_name == 'q':
        break

    album_name = input("Album Title: ")
    if album_name == 'q':
        break

    formatted_name = make_album(artist_name, album_name)
    print(formatted_name)