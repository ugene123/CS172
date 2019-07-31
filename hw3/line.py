# Yevgeniy (Eugene) Yakovlev
# yy459 - student id 14153285
# CS172 - Homework 3 Assignment, PyGame
# Summer 2019

from drawable import Drawable
import pygame

class Line(Drawable):
  def __init__(self, start_pos, end_pos, color, width):
    super().__init__(start_pos[0], start_pos[1])
    self.__start_pos = start_pos
    self.__end_pos = end_pos
    self.__color = color
    self.__width = width

  def draw(self, surface):
    pygame.draw.line(surface, self.__color, self.__start_pos, self.__end_pos, self.__width)

  def get_rect(self):
    return None