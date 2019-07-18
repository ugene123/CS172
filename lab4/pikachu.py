from monster import monster

class Pikachu(monster):

  def __init__(self):
    self.__health = 15
    self.__name = 'Pika'
    self.__description = 'Furry, yellow, and full of energy little guy'

  def getName(self):
    return self.__name 
	
  def getDescription(self):
	  return self.__description

  def basicAttack(self,enemy):
	  enemy.doDamage(3)
  	
  def basicName(self):
    return 'Electric Shock'
		
  def defenseAttack(self,enemy):
    enemy.doDamage(2)
		
  def defenseName(self):
    return 'Electric Shock'
		
  def specialAttack(self,enemy):
    enemy.doDamage(5)
		
  def specialName(self):
    return 'Lightning Bolt Strike'
		
  def getHealth(self):
    return self.__health
		
  def doDamage(self,damage):
    self.__health -= damage 

  def resetHealth(self):
    self.__health = 15
	