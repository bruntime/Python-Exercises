import random, copy, sys, pygame
from pygame.locals import *

BOARDWIDTH = 7
BOARDHEIGHT = 6
assert BOARDWIDTH >= 4 and BOARDHEIGHT >=4

SPACESIZE = 50 # size of tokens and board spaces

FPS = 30 # updating the screen
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

XMARGIN = int((WINDOWWIDTH = BOARDWIDTH * SPACESIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - BOARDHEIGHT * SPACESIZE) / 2)

BRIGHTBLUE = (0, 50, 255)
WHITE = (255, 255, 255)

BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

RED = 'red'
BLACK = 'black'
EMPTY = None
Human = 'human'
COMPUTER = 'computer'

def main():
	global FPSCLOCK, DISPLAYSURF, REDPILERECT, BLACKPILERECT, REDTOKENIMG
	global BLACKTOKENIMG, BOARDIMG, ARROWIMG, ARRORECT, HUMANWINNERIMG
	global COMPUTERWINNERIMG, WINNERRECT, TIEWINNERIMG
	
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	pygame.display.set_caption('Four in a Row')
	
	REDPILERECT = pygame.Rect(int(SPACESIZE / 2), WINDOWHEIGHT - int(3 * SPACESIZE) /2, SPACESIZE, SPACESIZE)
	
	REDTOKENIMG = pygame.image.load('4row_red.png')
	
#Working through Connect Four tutorial from Making Games with Python and Pygames (Sweigart)
