import pygame
from ball import Ball
from block import Block
from text import Text
from line import Line
from rectangle import Rectangle
import os

# Initialize Pygame Window
pygame.init()
pygame.font.init()
surface = pygame.display.set_mode((400, 400))
pygame.display.set_caption('CS 172 Game by Eugene Yakovlev')
#fpsClock = pygame.time.Clock()

# Set up Reusable Colors
colorRed = (255, 0, 0)
colorBlack = (0, 0, 0)
colorGreen = (0, 255, 0)
colorWhite = (255, 255, 255)

# Game constants
scoreCount = 0
startLoc = (0, 0)
endLoc = (0, 0)
xv = 0
yv = 0
# Delta time, gravity, rebound constant, coefficient of friction
dt = 0.1
g = 6.67
R = 0.7
eta = 0.5

# Create onscreen Drawable Objects
drawables = []

ball = Ball(50, 294, 5, colorRed)
drawables.append(ball)

score = Text(10, 10, "Score: " + str(scoreCount), colorWhite)
drawables.append(score)

ground = Rectangle(0, 301, 400, 100, colorBlack)
drawables.append(ground)

groundLine = Line((0, 300), (400, 300), colorWhite, 1)
drawables.append(groundLine)

current_path = os.path.dirname(__file__) # Where your .py file is located
background = pygame.image.load(os.path.join(current_path, 'background.png'))

# Draw 9 Blocks
for i in range(0, 3):
  for j in range(0, 3):
    block = Block(280 + (i * 30), 210 + (j * 30), 30, colorGreen)
    drawables.append(block)



def intersect(rect1, rect2):
  if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
    return True
  else:
    return False


# Begin Game
run = 1
while True:
  for event in pygame.event.get():
    if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
      pygame.quit()
      exit()

    surface.fill((255, 255, 255))

    if(event.type == pygame.MOUSEBUTTONDOWN):
      startLoc = pygame.mouse.get_pos()
      
    if(event.type == pygame.MOUSEBUTTONUP):
      endLoc = pygame.mouse.get_pos()
      xv = (startLoc[0] - endLoc[0]) * 0.25
      yv = (startLoc[1] - endLoc[1]) * -1 * 0.25

    if(abs(yv) > 0.0001):
      loc = ball.getLocation()

      # Ball is on the ground
      if(loc[1] > 295):
        yv = -R * yv
        xv = eta * xv
      else:
        # Ball is in the air
        yv = yv - g * dt

      newloc = (loc[0] + (dt + xv), loc[1] - (dt + yv))
      ball.setLocation(newloc)
    
    ballObject = drawables[0] 
    
    print("run " + str(run))   
    run += 1

    surface.blit(background, (0, 0))
    for drawable in drawables:
      if(drawable.getVisibility()):
        if(isinstance(drawable, Block)):
          ball_rect = ballObject.get_rect()
          block_rect = drawable.get_rect()
          
          if(intersect(ball_rect, block_rect)):
            print('Set visibility to false')
            drawable.setVisibility(False)
            scoreCount += 1
            drawables[1] = Text(10, 10, "Score: " + str(scoreCount), colorWhite)
          else:
            drawable.draw(surface)
        else:
          drawable.draw(surface)

    pygame.display.update()

    #fpsClock.tick(30)
