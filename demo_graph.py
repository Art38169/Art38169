import pygame
import math
import logging

logging.basicConfig(level = logging.INFO)

logger = logging.getLogger()
logger.info("Program started")


def f(x):
    return x

pygame.init()

w = 600
h = 600

screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Draw Graph")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        
    screen.fill((0,0,0))
    
    # x = -2
    for i in range(w):
        y = f(i)
        screen.set_at((i, w - y), (255, 255, 255))
        # x += 4/100
        
        
    pygame.display.flip()
        
pygame.quit()