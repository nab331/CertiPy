import pygame
from setup import *
import os

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


def center_xy(text,xy):
	fsize_x , fsize_y = PIL_draw.textsize(text,font)
	x = int(xy[0]-float((fsize_x))/2)
	y = int(xy[1]-float((fsize_y))/2)

	#print fsize_x,fsize_y
	return (x,y)

def map_xy((x,y)):

	x = float(x)
	y = float(y)

	#x_scale = float(screen_width)/width
	#y_scale = float(screen_height)/height
	x_scale = scale
	y_scale = scale
	#print x_scale,y_scale


	if y>height/2:
		y*=y_scale
	if y<=height/2:
		y*=y_scale

	if x>width/2:
		x*=x_scale
	if x<=width/2:
		x*=x_scale

	#print x,y
	return (int(x),int(y))

def generate_output(rect_array):

	output_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Output')


	with open("input.csv","rb") as f:
		reader = csv.reader(f)
		count=1

		for row in reader:

			PIL_image = Image.open(filename)
			PIL_draw = ImageDraw.Draw(PIL_image)

			for i in range(len(rect_array)):
				#Mapping it to the original File Size and centering it with the rectangle
				xy = map_xy(rect_array[i].center)
				xy = center_xy(row[i],xy )
				
				PIL_draw.text( xy ,row[i],(28,70,150),font)

				output_name =  os.path.join( output_folder , str(count)+". "+row[0]+" ("+row[1]+")"+".jpg" )
				
			count+=1;	
			PIL_image.save(output_name)


				

			#if count==10:
			#	break

fonts_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts')
font = ImageFont.truetype(os.path.join(fonts_path, 'best_font.otf'), 80)

draw_start = False
to_draw = []

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEMOTION:
			mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = mouse_pos
			draw_start = True

		if event.type == pygame.MOUSEBUTTONUP:
			final_pos = mouse_pos
			draw_start = False
			rect = pygame.Rect(pos,(final_pos[0]- pos[0], final_pos[1]-pos[1]))
			rect.normalize()
			to_draw+=[rect]

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False


			if event.key == pygame.K_RETURN:

				print to_draw[0]

				generate_output(to_draw)				
				
				

			if event.key == pygame.K_BACKSPACE:
				to_draw.pop()

	#Display
	screen.blit(img,(0,0))

	if draw_start:
		pygame.draw.rect(screen,(255,0,0), pygame.Rect(pos, (mouse_pos[0] - pos[0],mouse_pos[1]- pos[1])))
	for item in to_draw:
		pygame.draw.rect(screen,(0,255,0),item)

	#Logic




	#Update
	clock.tick(30)
	pygame.display.update()


