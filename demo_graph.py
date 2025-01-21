import pygame
import math
import logging

logging.basicConfig(level = logging.INFO)

logger = logging.getLogger()
logger.info("Program started")


def f(x):
    return x ** 2

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
    
    x = -2
    for i in range(1001):
        y = f(x)
        screen.set_at((int(150 * x +300), int(600 - 60 * y)), (255, 255, 255))
        x += 4/1000
        
        
    pygame.display.flip()
        
pygame.quit()