import pygame
from Rectangle import Rectangle
from Snowflake import Snowflake
import random

pygame.init()
surface = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Snowflake Background')

fpsClock = pygame.time.Clock()


drawables = []
grass = Rectangle(0, 200, 400, 100, (50, 205, 50))
drawables.append(grass)

sky = Rectangle(0, 0, 400, 200, (135, 206, 250))
drawables.append(sky)

enable = False

while True:
  for event in pygame.event.get():
    if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
      pygame.quit()
      exit()

    if(event.type == pygame.K_SPACE):
      continue
    
    surface.fill((255, 255, 255))

    startX = random.randint(0, 400)
    maxY = random.randint(200, 300)
    snowflake = Snowflake(startX, maxY)
    drawables.append(snowflake)

    for drawable in drawables:
      if(isinstance(drawable, Snowflake)):
        loc = drawable.getLoc()
        if(loc[1] != drawable.getMaxY()):
          drawable.moveDown()

      drawable.draw(surface)

    pygame.display.update()

    fpsClock.tick(30)
