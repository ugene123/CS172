# Yevgeniy (Eugene) Yakovlev
# yy459 - student id 14153285
# CS172 - Homework 3 Assignment, PyGame
# Summer 2019

import pygame
import abc

class Drawable(metaclass = abc.ABCMeta):
  def __init__(self, x = 0, y = 0):
    self.__x = x
    self.__y = y
    self.__visible = True

  def getLocation(self):
    return (self.__x, self.__y)

  def setLocation(self, cord):
    self.__x = cord[0]
    self.__y = cord[1]

  def setVisibility(self, visible):
    self.__visible = visible

  def getVisibility(self):
    return self.__visible

  @abc.abstractmethod
  def draw(self, surface):
    pass

  @abc.abstractmethod
  def get_rect(self):
    pass

