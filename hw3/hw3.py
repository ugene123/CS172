# Yevgeniy (Eugene) Yakovlev
# yy459 - student id 14153285
# CS172 - Homework 3 Assignment, PyGame
# Summer 2019

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
pygame.display.set_caption('CS172 Game by Eugene Yakovlev')

# Set up Reusable Colors
colorRed = (255, 0, 0)
colorBlack = (0, 0, 0)
colorGreen = (0, 255, 0)
colorWhite = (255, 255, 255)

# Game constants: X-Velocity, Y-Velocity, Delta time, gravity, rebound constant, coefficient of friction
score = 0
xv = 0
yv = 0
dt = 0.1
g = 6.67
R = 0.7
eta = 0.5

def setupScene(drawables):
  ground = Rectangle(0, 301, 400, 100, colorBlack)
  drawables.append(ground)

  groundLine = Line((0, 300), (400, 300), colorWhite, 1)
  drawables.append(groundLine)

  ball = Ball(50, 294, 5, colorRed)
  drawables.append(ball)

  scoreText = Text(10, 10, "Score: " + str(score), colorWhite, 24)
  drawables.append(scoreText)

  for i in range(0, 10):
    for j in range(0, 10):
      block = Block(280 + (i * 10), 200 + (j * 10), 10, colorGreen)
      drawables.append(block)

def intersect(rect1, rect2):
  if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y):
    return True
  else:
    return False

# Create onscreen Drawable Objects
drawables = []
setupScene(drawables)

current_path = os.path.dirname(__file__) # Where your .py file is located
background = pygame.image.load(os.path.join(current_path, 'background.png'))

ballMoved = False
gameOver = False


def showGameOver():
  gameoverText = Text(80, 320, "Game Over! Your final score is " + str(score), colorWhite, 24)
  drawables.append(gameoverText)
  continueText = Text(115, 350, "Press ENTER to play again", colorWhite, 20)
  drawables.append(continueText)

# Begin Game
while True:

  # Check if Ball is moving (y velocity)
  if(abs(yv) > 0.0001):
    ball = drawables[2]
    loc = ball.getLocation()

    # Check that ball is inside the window dimensions
    if(loc[0] > 0 and loc[0] < 400):
      
      # Ball is on the ground
      if(loc[1] > 296):
        yv = -R * yv
        xv = eta * xv
      else:
        # Ball is in the air
        yv = yv - g * dt

      # Relocate ball location based on game physics
      ballMoved = True
      newloc = (loc[0] + (dt + xv), loc[1] - (dt + yv))
      ball.setLocation(newloc)

    elif(not gameOver):
      # Ball is outside of the window dimensions
      gameOver = True
      showGameOver()

  elif(ballMoved and not gameOver):
    # Ball moved and it stopped in motion, End Game
    gameOver = True
    showGameOver()

  # Add background to surface
  surface.blit(background, (0, 0))

  # Loop through drawable objects to draw on surface
  for drawable in drawables:

    # Check if object is visible
    if(drawable.getVisibility()):

      # Check if drawable is Block to check for collision with ball 
      if(isinstance(drawable, Block)):
        ballObject = drawables[2] 
        ball_rect = ballObject.get_rect()
        block_rect = drawable.get_rect()

        # Check if Block object intersects with ball objeect
        if(intersect(ball_rect, block_rect)):

          # Handle intersection (collision) between ball and block 
          drawable.setVisibility(False)
          # Increment score by 1 per collision
          score += 1
          drawables[3] = Text(10, 10, "Score: " + str(score), colorWhite, 24)
        else:
          # Drawable Block did not intersect with ball
          drawable.draw(surface)
      else:
        # Drawable is not a Block, draw w/o checking for collision
        drawable.draw(surface)

  pygame.display.update()

  # Handle game events
  for event in pygame.event.get():
    # Quit Game
    if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
      pygame.quit()
      exit()

    # Mouse Pressed Down
    if(event.type == pygame.MOUSEBUTTONDOWN):
      if(not ballMoved):
        startLoc = pygame.mouse.get_pos()
      else:
        continue
      
    # Mouse Released 
    if(event.type == pygame.MOUSEBUTTONUP):
      if(not ballMoved):
        endLoc = pygame.mouse.get_pos()
        xv = (startLoc[0] - endLoc[0]) * 0.25
        yv = (startLoc[1] - endLoc[1]) * -1 * 0.25
      else: 
        continue

    # Enter Key Pressed
    if(event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_RETURN):
      
      # Reset variables
      yv = 0 
      xv = 0
      score = 0
      
      # Reset scene and objects
      drawables = []
      setupScene(drawables)
    
      gameOver = False
      ballMoved = False