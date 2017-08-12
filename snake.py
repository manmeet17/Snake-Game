import pygame
from pygame.locals import *
import sys
import random
import time

check_error = pygame.init()
if(check_error[1] != 0):
	print ("Had {0} inititalizing error".format(check_error[1]))
	sys.exit(-1)
playSurface = pygame.display.set_mode((720,460))
pygame.display.set_caption("Snake Game")
time.sleep(5)