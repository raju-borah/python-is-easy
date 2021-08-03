"""
Homework #2 : Functions
using function
submitted by: Raju Moni Borah
"""
# function return song name in string value
def songName():
    return "Best Day Of My Life"
# function return artist name in string value
def artistName():
    return "American Authors"
# function return duration of songs in float value
def duration():
    return 3.14
# function return Boolean value 
def isThisMyFavSong():
    return True

# calling the function to return my favorate song
Song = songName()
# calling the function to return artist of the song
Artist = artistName()
# calling the function to return length of the song
LengthInMinutes = duration()
# calling the function return Boolean value 
isFav = isThisMyFavSong()

"""
Printing out all the variable that are created above.
"""
print("Song : ", Song)
print("Artist : ", Artist)
print("Duration(in minutes) : ", LengthInMinutes)
print("Is This My favorite Song : ", isFav)