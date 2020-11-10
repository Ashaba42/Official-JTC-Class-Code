import numpy as np


my_playlist = [{'artist': 'Bilal', 'title': 'Sometimes', 'favorite': False},
               {'artist': 'Chaka Khan', 'title': "I'm Every Woman", 'favorite': False},
               {'artist': 'Chaka Khan', 'title': "Ain't Nobody", 'favorite': False},
               {'artist': 'Parliament',
                   'title': 'Mothership Connection (Star Child)', 'favorite': False},
               {'artist': 'Pink Floyd',
                   'title': 'Another Brick in the Wall', 'favorite': False},
               {'artist': 'Parliament', 'title': 'Unfunky UFO', 'favorite': False},
               {'artist': 'Nina Simone',
                   'title': 'Mississippi Goddamn', 'favorite': False},
               {'artist': 'Nina Simone', 'title': 'Four Women', 'favorite': False},
               {'artist': 'Roberta Flack',
                   'title': 'Killing Me Softly', 'favorite': False},
               {'artist': 'Fugees', 'title': 'Killing Me Softly', 'favorite': False}]

'''
FUNCTIONS BELOW NEED TO BE PSEUDOCODED AND IMPLEMENTED
'''

'''
For Question 1:
function to add songs to a playlist
-takes 2 arguments, playlist (list) and song (dictionary)
-returns nothing
'''


def add_song(playlist, song):
    playlist.append(song)
# append a song to my_playlist

new_song = {'artist': 'Kendrick Lamar', 'title': 'Alright', 'favorite': False}

# Check print to see if the function worked!
print(my_playlist)

'''
For Question 2:
function to search songs by artist
-takes 2 arguments, playlist (list) and artist_name (a string)
-returns a list of songs in the playlist by that artist
'''


def search_by_artist(playlist, artist_name):
    song_artist = []
    for song in playlist:
      if song['artist'] == artist_name:
        song_artist.append(song)
    return(song_artist)   

# pass

# create an empty list
# for each song in playlist, loop over playlist
# if song is by atrist, return list of artist song


# Check print to see if the function worked!
print(search_by_artist(my_playlist, 'Pink Floyd'))

'''
For Question 3:
Function to search songs by title
-takes 2 arguments, playlist (list) and song_title (string)
-returns a list including all the songs with the title searched
'''
def search_by_title(playlist, song_title):
    song_list = []
    for song in playlist:
      if song['title'] == song_title:
        song_list.append(song)
    return(song_list)

# pass

# create an empty list
# for eah title in playlist loop over playlist
# if title is equal song title
# append the song
# return list of song title

# Check print to see if the function worked!
print(search_by_title(my_playlist, 'Killing Me Softly'))

'''
For Question 4
Function to set the favorite status of a song to True
-takes 3 arguments, playlist (list), song_title (string), artist_name (string)
-returns nothing
'''

def favorite_song(playlist, song_title, artist_name):
    for song in playlist:
      if song['title'] == song_title and song['artist'] == artist_name:
        song['favorite'] = True

# pass

# loop through the playlist
# if the song title is equal to the song title & song artist is equal to artist name
# favorite key = true

favorite_song(my_playlist, "Ain't Nobody", 'Chaka Khan')
favorite_song(my_playlist, "Four Women", 'Nina Simone')
# Check print to see if the function worked!
print(my_playlist)


'''
For Question 5
Function to create a favorites playlist based on songs that have been favorited using favorite_song function
-takes 1 argument, playlist (list)
-returns list of favorite songs
'''


def create_favorites_playlist(playlist):
  favorites_playlist = []
  for song in playlist:
    if song['favorite'] == True:
      favorites_playlist.append(song)
  return(favorites_playlist)    
    
# pass

# create an empty list
# loop through the playlist
# check the favorite key
# append the song to favorites list
# return list of favorite songs


# Check print to see if the function worked!
print(create_favorites_playlist(my_playlist))

'''
For Question 6
Function to shuffle a playlist
-takes 1 argument, playlist (list)
-return nothing

Hint: you can use a numpy function to accomplish this!
'''


def play_shuffle(playlist):
  np.random.shuffle(playlist)  


  # pass
  # np.random.shuffle(playlist)
  
  
# Check print to see if the function worked!
play_shuffle(my_playlist)
print(play_shuffle(my_playlist))
