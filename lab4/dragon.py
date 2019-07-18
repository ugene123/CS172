from monster import monster

class Dragon(monster):

  def __init__(self):
    self.__health = 20
    self.__name = 'Mario'
    self.__description = 'the famous Mario the Dragon'

  def getName(self):
    return self.__name 
	
  def getDescription(self):
	  return self.__description

  def basicAttack(self,enemy):
	  enemy.doDamage(5)
  	
  def basicName(self):
    return 'Fire Breath'
		
  def defenseAttack(self,enemy):
    enemy.doDamage(4)
		
  def defenseName(self):
    return 'Swinged Wing'
		
  def specialAttack(self,enemy):
    enemy.doDamage(5)
		
  def specialName(self):
    return 'Lava'
		
  def getHealth(self):
    return self.__health
		
  def doDamage(self,damage):
    self.__health -= damage 

  def resetHealth(self):
    self.__health = 20
	