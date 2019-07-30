import pygame
from ball import Ball
from block import Block
from text import Text
from line import Line

# Initialize Pygame Window
pygame.init()
pygame.font.init()
surface = pygame.display.set_mode((400, 400))
pygame.display.set_caption('CS 172 Game by Eugene Yakovlev')
fpsClock = pygame.time.Clock()

# Set up Reusable Colors
colorRed = (255, 0, 0)
colorBlack = (0, 0, 0)
colorGreen = (0, 255, 0)

# Create onscreen Drawable Objects
drawables = []

ball = Ball(50, 295, 5, colorRed)
drawables.append(ball)

score = Text(10, 10, "Score: 0", colorBlack)
drawables.append(score)

ground = Line((0, 300), (400, 300), colorBlack, 1)
drawables.append(ground)

# Draw 9 Blocks
for i in range(0, 3):
  for j in range(0, 3):
    block = Block(280 + (i * 30), 210 + (j * 30), 30, colorBlack)
    drawables.append(block)

# Begin Game
while True:
  for event in pygame.event.get():
    if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
      pygame.quit()
      exit()

    if(event.type == pygame.K_SPACE):
      continue
    
    surface.fill((255, 255, 255))

    for drawable in drawables:
      drawable.draw(surface)

    pygame.display.update()

    fpsClock.tick(30)
