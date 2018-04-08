import os
import sys
import gtk, pygtk
import pygame
import csv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

try:
	filename = sys.argv[1]

except:
	print

while True:
	try:
		img=pygame.image.load(filename)

	except:
		filename = raw_input("File not available (Format : name.extention)\nTry again : ") 

	else:
		break






screen_height, screen_width = gtk.Window().get_screen().get_height(), gtk.Window().get_screen().get_width()

width,height = img.get_rect().size
scale = 1


while width>screen_width or height>screen_height:
	width/=2
	height/=2
	scale*=2
	#print screen_width, width,"\n", screen_height, height
	
img = pygame.transform.scale(img,(width,height))

PIL_image = Image.open(filename)
PIL_draw = ImageDraw.Draw(PIL_image)

clock = pygame.time.Clock()
background_colour = (0,0,0)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('CertiPy')


running = True