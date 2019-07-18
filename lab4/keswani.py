from monster import monster

class Keswani(monster):
    def __init__(self):
        self.__health = 17
        self.__name = "Keswani"
        self.__description = "The mighty green monster from Dubai."

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def basicAttack(self, enemy):
        enemy.doDamage(4)

    def basicName(self):
        return "Boom boom pow!"

    def defenseAttack(self, enemy):
        enemy.doDamage(4)

    def defenseName(self):
        return "Yikes!"

    def specialAttack(self, enemy):
        enemy.doDamage(3)

    def specialName(self):
        return "Woop, there it is."

    def getHealth(self):
        return self.__health

    def doDamage(self, damage):
        self.__health -= damage

    def resetHealth(self):
        self.__health = 20



