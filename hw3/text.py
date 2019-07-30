from drawable import Drawable
import pygame

class Text(Drawable):
  def __init__(self, x, y, text, color):
    super().__init__(x, y)
    self.__text = text
    self.__color = color

  def draw(self, surface):
    loc = self.getLocation()
    myfont = pygame.font.SysFont('Comic Sans MS', 24)
    textSurface = myfont.render(self.__text, True, self.__color)
    surface.blit(textSurface, loc)

  def get_rect(self):
    return None