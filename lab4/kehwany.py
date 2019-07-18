from monster import monster

class Kehwany(monster):
    def __init__(self):
        self.__health = 20
        self.__name = "Kehwany"
        self.__description = "I am Kehwany from h-town."

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def basicAttack(self, enemy):
        enemy.doDamage(2)

    def basicName(self):
        return "bomb shiz"

    def defenseAttack(self, enemy):
        enemy.doDamage(3)

    def defenseName(self):
        return "protection!"

    def specialAttack(self, enemy):
        enemy.doDamage(4)

    def specialName(self):
        return "shock!"

    def getHealth(self):
        return self.__health

    def doDamage(self, damage):
        self.__health -= damage

    def resetHealth(self):
        self.__health = 20


