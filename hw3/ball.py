from drawable import Drawable
import pygame

class Ball(Drawable):
  def __init__(self, x, y, radius, color):
    super().__init__(x, y)
    self.__radius = radius
    self.__color = color

  def draw(self, surface):
    loc = self.getLocation()
    
    pygame.draw.circle(surface, self.__color, loc, self.__radius)

  def get_rect(self):
    return None

