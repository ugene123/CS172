class Player:
  def __init__(self, name):
    self.__name = name

  def __add__(self, otherPlayer):
    return Player(self.__name + otherPlayer.__name)

  def __str__(self):
    return self.__name

player1 = Player('Player 1')
player2 = Player('Player 2')

newPlayer = player1 + player2

print(newPlayer)
