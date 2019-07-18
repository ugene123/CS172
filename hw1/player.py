class Player():
  def __init__(self, name):
    self.__name = name
    self.__score = 0

  def getName(self):
    return self.__name

  def getScore(self):
    return self.__score

  def addScore(self, amount):
    self.__score += amount