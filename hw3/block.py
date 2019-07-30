from drawable import Drawable
import pygame

class Block(Drawable):
  def __init__(self, x, y, length, color):
    super().__init__(x, y)
    self.__length = length
    self.__color = color

  def draw(self, surface):
    loc = self.getLocation()
    side = self.__length
    rect =  pygame.Rect(loc[0], loc[1], side, side)
    pygame.draw.rect(surface, self.__color, rect)

  def get_rect(self):
    loc = self.getLocation()
    return pygame.Rect(loc[0], loc[1], self.__length, self.__length)