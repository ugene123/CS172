# Yevgeniy (Eugene) Yakovlev
# Student ID - 14153285
# Purpose: Program that simulates a media library. 
# Library has three types of media: pictures, music, and movies.  

from media import Picture, Movie, Song

# Create a Media Library
library = []

# Create and Add Images to media library
library.append(Picture('AirBaloon', 4, 560))
library.append(Picture('Cake', 5, 1024))
library.append(Picture('ProfilePicture', 2, 720))
library.append(Picture('Avatar', 3, 960))

# Create and Add Movies to media library
library.append(Song('Venom', 4, 'Eminem', 'Kamikaze'))
library.append(Song('WHY', 5, 'NF', 'WHY'))
library.append(Song('21 Guns', 5, 'Green Day', '21st Century Breakdown'))
library.append(Song('Bounce', 2, 'Logic', 'Under Pressure'))

# Create and Add Songs to media library
library.append(Movie('Narnia', 5, 'CS Lewis', 160))
library.append(Movie('Lion King', 4, 'Jon Favreau', 98))
library.append(Movie('Toy Story 4', 3, 'Josh Cooley', 100))
library.append(Movie('Aladdin', 5, 'Guy Ritchie', 130))

print('>>----------<<<[ Welcome to the Media Library ]>>>----------<<')
quit = False

while(not quit):
  print('\nPlease SELECT a command or ENTER the name of the media that you would like to play to continue!')
  print('\na - display all items in the media library')
  print('s - display only songs')
  print('m - display only movies')
  print('p - display only pictures')
  print('q - quit the program')

  user_input = str(input("\nEnter command OR media name: ")).lower()

  # Check if user passed a command
  if(user_input in ['a', 's', 'm', 'p', 'q']):
    if(user_input == 'q'):
        quit = True
    else:
      for media in library:
        # User selects only songs
        if(user_input == 's' and media.getType() == 'Song'):
          print(media)
        # User selects only movies
        elif(user_input == 'm' and media.getType() == 'Movie'):
          print(media)
        # User selects only pictures
        elif(user_input == 'p' and media.getType() == 'Picture'):
          print(media)
        # Display all items in media
        elif(user_input == 'a'):
          print(media)
  else:
    # User searching for specific media name
    matched_media = None
    for media in library:
      if(media.getName().lower() == user_input):
        matched_media = media
    
    if(matched_media is not None):
      if(matched_media.getType() in ['Song', 'Movie']):
        matched_media.play()
      else:
        matched_media.show()
    else:
      # Media name not found!
      print('\n############## ERROR 404 - NOT FOUND ################')
      print('\nFilename <<' + user_input + '>> not found in Media Library. \nTry command \'a\' to view all items in the library')
      print('\n#####################################################')