# Yevgeniy (Eugene) Yakovlev
# yy459 - student id 14153285
# CS172 - Homework 3 Assignment, PyGame
# Summer 2019

from drawable import Drawable
import pygame

class Text(Drawable):
  def __init__(self, x, y, text, color, size):
    super().__init__(x, y)
    self.__text = text
    self.__color = color
    self.__size = size

  def draw(self, surface):
    loc = self.getLocation()
    myfont = pygame.font.SysFont('Comic Sans MS', self.__size)
    textSurface = myfont.render(self.__text, True, self.__color)
    surface.blit(textSurface, loc)

  def get_rect(self):
    return None