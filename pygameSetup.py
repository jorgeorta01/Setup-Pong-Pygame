import pygame, sys

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Setting Up Main Window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

while True:
    #Handling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#updateing the window 
pygame.display.flip()
clock.tick(60)