# Yevgeniy (Eugene) Yakovlev
# yy459 - student id 14153285
# CS172 - Homework 3 Assignment, PyGame
# Summer 2019

from drawable import Drawable
import pygame

class Rectangle(Drawable):

  def __init__(self, x, y, width, height, color):
    super().__init__(x, y)
    self.__width = width
    self.__height = height
    self.__color = color

  def draw(self, surface):
    loc = self.getLocation()
    pygame.draw.rect(surface, self.__color, [loc[0], loc[1], self.__width, self.__height])

  def get_rect(self):
    return None