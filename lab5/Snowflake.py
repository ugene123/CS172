from Drawable import Drawable
import pygame

class Snowflake(Drawable):

  def __init__(self, x, maxY):
    super().__init__(x, 0)
    self.__maxY = maxY

  def getMaxY(self):
    return self.__maxY
    
  def moveDown(self):
    origin = self.getLoc()
    destination = (origin[0], origin[1] + 1)
    self.setLoc(destination)

  def draw(self, surface):
    white = (255, 255, 255)
    loc = self.getLoc()
    x = loc[0]
    y = loc[1]

    pygame.draw.line(surface, white, (x - 5, y), (x + 5, y), 1)
    pygame.draw.line(surface, white, (x, y - 5), (x, y + 5), 1)
    pygame.draw.line(surface, white, (x - 5, y - 5), (x + 5, y + 5), 1)
    pygame.draw.line(surface, white, (x - 5, y + 5), (x + 5, y - 5), 1)