def make_album(artist_nm, album_nm, track_nm=''):
    album_info = {'artist': artist_nm, 'album': album_nm}
    if track_nm:
        album_info['track_nm'] = track_nm
    return album_info

album_data = make_album('bathory', 'hammerheart', '8')
print(album_data)

album_data = make_album('genghis tron', 'dead mountain mouth')
print(album_data)

album_data = make_album('the midnight', 'endless summer', '12')
print(album_data
      )