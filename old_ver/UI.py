import pygame
from pygame.locals import QUIT
import sys
import time
pygame.init()
window_surface = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Basball Trace Drawer')
window_surface.fill((255, 255, 255))

font = pygame.font.SysFont("comicsansms", 20)
midFont = pygame.font.SysFont("comicsansms", 30)
biggerFont = pygame.font.SysFont('comicsansms', 40)

# initialize the machine
initial = font.render("First, initailize the machine.", True, (100, 100, 100))
press = font.render("press any key to start initalize", True, (100, 100, 100))

window_surface.blit(initial, (150, 0))
window_surface.blit(press, (130, 20))
pygame.display.update()

stop = False
while(not stop):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            stop = True
            break
window_surface.fill((255, 255, 255))
countDown = font.render("Count down from ", True, (100, 100, 100))
window_surface.blit(countDown, (150, 20))
for i in range(4):
    color = (255, 255, 255)
    time.sleep(1)
    pygame.draw.rect(window_surface, color, pygame.Rect(400, 28, 50, 35))
    countNum = biggerFont.render(str(3-i), True, (20, 3, 200))
    window_surface.blit(countNum, (400, 13))
    pygame.display.update()

window_surface.fill((255, 255, 255))
finish = biggerFont.render("finish initialize!", True, (100, 100, 100))
window_surface.blit(finish, (140, 0))
pygame.display.update()


window_surface.fill((255, 200, 255))
pressToStart = font.render("press any key and throw the ball", True, (100, 100, 100))
window_surface.blit(pressToStart, (120, 30)) 
pygame.display.update()

stop = False
while(not stop):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            stop = True
            break
# press the buttom and throw the ball
window_surface.fill((200, 255, 255))
countDown = midFont.render("count down ", True, (100, 100, 100))
window_surface.blit(countDown, (150, 50))
pygame.display.update()
for i in range(4):
    color = (200, 255, 255)
    time.sleep(1)
    pygame.draw.rect(window_surface, color, pygame.Rect(400, 50, 50, 60))
    countNum = biggerFont.render(str(3-i), True, (20, 3, 200))
    window_surface.blit(countNum, (400, 50))
    pygame.display.update()
launch = midFont.render("Launch!", True, (100, 100, 200))
window_surface.blit(launch, (220, 130))
pygame.display.update()


stop = False
while(not stop):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            stop = True
            break
pygame.quit()
sys.exit()           