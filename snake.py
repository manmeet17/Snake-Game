import pygame
from pygame.locals import *
import sys
import random
import time

check_error = pygame.init()
if(check_error[1] != 0):
	print ("Faced {0} inititalizing error".format(check_error[1]))
	sys.exit(-1)
playSurface = pygame.display.set_mode((720,460))
pygame.display.set_caption("Snake Game")

red=pygame.Color(255,0,0)
green=pygame.Color(0,255,0)
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
brown=pygame.Color(165,42,42)

# FPS controller
fpsController=pygame.time.Clock()

# Variables
snakePos=[100,50]
snakeBody=[[100,50],[90,50],[80,50]]
foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn=True

direct='RIGHT'
changeTo=direct

def gameOver():
	font=pygame.font.SysFont('monaco',72)
	GOsurf=font.render('Game Over!', True, red)
	Gorect=GOsurf.get_rect()
	Gorect.midtop=(360,20)
	playSurface.blit(GOsurf,Gorect)
	pygame.display.flip()

gameOver()

time.sleep(10)
