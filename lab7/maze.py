class Maze:

  def __init__(self, st = None, ex = None):
    self.__start_room = st
    self.__exit_room = ex
    self.__current = st

  def getCurrrent(self):
    return self.__current

  def setRoomIfNotNone(self, door):
    if(door is not None):
      self.__current = door
      return True
    else:
      return False

  def moveNorth(self):
    door = self.__current.getNorth()
    roomExists = self.setRoomIfNotNone(door)
    return roomExists

  def moveSouth(self):
    door = self.__current.getSouth()
    roomExists = self.setRoomIfNotNone(door)
    return roomExists

  def moveEast(self):
    door = self.__current.getEast()
    roomExists = self.setRoomIfNotNone(door)
    return roomExists

  def moveWest(self):
    door = self.__current.getWest()
    roomExists = self.setRoomIfNotNone(door)
    return roomExists

  def atExit(self):
    if(self.__current == self.__exit_room):
      return True
    else:
      return False

  def reset(self):
    self.__current = self.__start_room



    
