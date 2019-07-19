class Media():
  def __init__(self, mtype, name, rating):
    self.__type = mtype
    self.__name = name
    self.__rating = rating

  def __str__(self):
    description = '------ Generic Media Information ------'
    description += '\nMedia Type: ' + self.__type
    description += '\nName: ' + self.__name
    description += '\nRating: ' + self.__rating
    return description

  def getType(self):
    return self.__type
  
  def getName(self):
    return self.__name
  
  def getRating(self):
    return self.__rating
  
  def setType(self, mtype):
    self.__type = mtype
  
  def setName(self, name):
    self.__name = name
  
  def setRating(self, rating):
    self.__rating = rating


class Movie(Media):

  def __init__(self, name, rating, director, length):
    super().__init__('Movie', name, rating)
    self.__director = director
    self.__length = length

  def __str__(self):
    description = '\n------ Movie Information ------'
    description += '\nMedia Type: ' + super().getType()
    description += '\nName: ' + super().getName()
    description += '\nRating: ' + str(super().getRating())
    description += '\nDirector: ' + self.__director
    description += '\nRunning Time: ' + str(self.__length)
    description += '\n-------------------------------'
    return description

  def getDirector(self):
    return self.__director

  def getLength(self):
    return self.__length

  def setDirector(self, director):
    self.__director  = director 

  def setLength(self, length):
    self.__length  = length 

  def play(self):
    print('\n------------ MOVIE PLAYING ------------')
    print('\n<<' + super().getName() + '>> is now playing')
    print('\n--------------------------------------')



class Picture(Media):

  def __init__(self, name, rating, resolution):
    super().__init__('Picture', name, rating)
    self.__resolution = resolution

  def __str__(self):
    description = '\n------ Picture Information ------'
    description += '\nMedia Type: ' + super().getType()
    description += '\nName: ' + super().getName()
    description += '\nRating: ' + str(super().getRating())
    description += '\nResolution: ' + str(self.__resolution)
    description += '\n----------------------------------'
    return description

  def getResolution(self):
    return self.__resolution

  def setResolution(self, resolution):
    self.__resolution  = resolution 

  def show(self):
    print('\n------------ DISPLAYING PICTURE ------------')
    print('\nShowing <<' + super().getName() + '.jpg>>')
    print('\n--------------------------------------------')
    

class Song(Media):

  def __init__(self, name, rating, artist, album):
    super().__init__('Song', name, rating)
    self.__artist = artist
    self.__album = album

  def __str__(self):
    description = '\n------ Song Information ------'
    description += '\nMedia Type: ' + super().getType()
    description += '\nName: ' + super().getName()
    description += '\nRating: ' + str(super().getRating())
    description += '\nArtist: ' + self.__artist
    description += '\nAlbum: ' + self.__album
    description += '\n------------------------------'
    return description

  def getArtist(self):
    return self.__artist

  def getAlbum(self):
    return self.__album

  def setArtist(self, artist):
    self.__artist  = artist 
  
  def setAlbum(self, album):
    self.__album  = album 

  def play(self):
    print('\n------------ SONG PLAYING ------------')
    print('\n<<' + super().getName() + '>> by <<' + self.__artist + '>> is now playing')
    print('\n--------------------------------------')