# Write a while loop that allows uses to enter an album's artist and title. Once you have that information, call make_album() with the user's input and print the dictionary that's created. Be sure to include a quite value in the while loop.

def make_album(album_artist, album_title):
    album = {
        'artist_album_name': album_artist.title(),
        'artist_title_name': album_title.title(),
    }
    return f'{album}\n'
    
    
while True:
    print("Please tell me your name: ")
    print("(enter 'q' or 'quit' or 'exit' at any time to quit)")
    
    name = input("Enter artist name: ")
    if name == 'q' or name == 'quit' or name == 'exit':
        break
    
    title = input("Enter title name: ")
    if title == 'q' or name == 'quit' or name == 'exit':
        break
        
    formatted_make_album = make_album(name, title)
    print(formatted_make_album)  