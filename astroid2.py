import pygame, random, sys

#initialising pygame and its functions 
pygame.init()
clock=pygame.time.Clock()
# creating game window and title
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Draw Rectangle")

# Display game window 
background_image = pygame.image.load("bg2.jpg").convert()

#.blit() is how you copy the contents of one screen to another.
screen.blit(background_image,[0,0])

#Color or rectangle
BLUE=(0,0,255)
player=pygame.Rect(200,200,30,30)
#Draw Rectangle of blue color [left, top, width, height]

#Draw WHITE Rectangle on given coordinates
WHITE=(255,255,255)
enemy=pygame.Rect(100,100,30,30)
xvel=1
yvel=5


while True:
  screen.fill((0,0,0))
  #event loop to check which key is print
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      
  
  enemy.x=enemy.x + xvel
  enemy.y=enemy.y + yvel 

  if enemy.x < -250 or enemy.x > 650 or enemy.y < -250 or enemy.y > 850:  
      xvel = -1*xvel
      yvel = -1*yvel

  pygame.draw.rect(screen,BLUE,player)
  pygame.draw.rect(screen,WHITE,enemy)

  pygame.display.update()
  clock.tick(30)
