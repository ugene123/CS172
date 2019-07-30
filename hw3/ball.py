from drawable import Drawable
import pygame

class Ball(Drawable):
  def __init__(self, x, y, radius, color):
    super().__init__(x, y)
    self.__radius = radius
    self.__color = color

  def draw(self, surface):
    loc = self.getLocation()
    intLoc = (int(loc[0]), int(loc[1]))
    
    pygame.draw.circle(surface, self.__color, intLoc, self.__radius)

  def get_rect(self):
    loc = self.getLocation()
    return pygame.Rect(loc[0] - self.__radius, loc[1] - self.__radius, self.__radius, self.__radius)

