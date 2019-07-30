from drawable import Drawable
import pygame

class Line():
  def __init__(self, start_pos, end_pos, color, width):
    self.__start_pos = start_pos
    self.__end_pos = end_pos
    self.__color = color
    self.__width = width

  def draw(self, surface):
    pygame.draw.line(surface, self.__color, self.__start_pos, self.__end_pos, self.__width)

  def get_rect(self):
    return None