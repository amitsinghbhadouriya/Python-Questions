# Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.
# Use none to add an optional parameter to make_album() that allows you to store the number os songs on an album. If the calling line includes a value for the number of songs, add that value to the album's dictionary. Make at least one new function call that includes that number of songs on an album.

def make_album(album_name, album_title, no_of_songs=None):
    album = {
        'album_name': album_name,
        'album_title': album_title,
    }
    if no_of_songs:
        album['Number_of_Songs'] = no_of_songs
    return album

print(make_album('Thriller','Michael Jackson'))
print(make_album('Scorpion','Drake'))
print(make_album('After Hours','The Weekend', 5))
