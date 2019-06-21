import sys, pygame
from pygame.locals import *
import time
import subprocess
import os
import glob
pygame.init()

def refresh_menu_screen():
#set up the fixed items on the menu
	screen.fill(white) #change the colours if needed
	font=pygame.font.Font(None,24)
	title_font=pygame.font.Font(None,34)
	station_font=pygame.font.Font(None,20)
	label=title_font.render("MPC RADIO", 1, (blue))
	label2=font.render("Streaming Internet Radio", 1, (red))
	screen.blit(label,(105, 15))
	screen.blit(label2,(88, 45))
# draw the main elements on the screen
	screen.blit(play,(20,80))	
	screen.blit(pause,(80,80))
	pygame.draw.rect(screen, red, (8, 70, 304, 108),1)
	pygame.draw.line(screen, red, (8,142),(310,142),1)
	pygame.draw.rect(screen, cream, (10, 143, 300, 33),0)
###### display the station name and split it into 2 parts : 
	station = subprocess.check_output("mpc current", shell=True )
	lines=station.split(":")
	length = len(lines) 
	if length==1:
		line1 = lines[0]
		line1 = line1[:-1]
		line2 = "No additional info: "
	else:
		line1 = lines[0]
		line2 = lines[1]

	line2 = line2[:42]
	line2 = line2[:-1]
	#trap no station data
	if line1 =="":
		line2 = "Press PLAY or REFRESH"
		station_status = "stopped"
		status_font = red
	else:
		station_status = "playing"
		status_font = green
	station_name=station_font.render(line1, 1, (red))
	additional_data=station_font.render(line2, 1, (blue))
	station_label=title_font.render(station_status, 1, (status_font))
	screen.blit(station_label,(175,100))
	screen.blit(station_name,(13,145))
	screen.blit(additional_data,(12,160))
######## add volume number
	volume = subprocess.check_output("mpc volume", shell=True )
	volume = volume[8:]
	volume = volume[:-1]
	volume_tag=font.render(volume, 1, (black))
	screen.blit(volume_tag,(175,75))
####### check to see if the Radio is connected to the internet
	IP = subprocess.check_output("hostname -I", shell=True )
	IP=IP[:3]
	if IP =="192":
		network_status = "online"
		status_font = green

	else:
		network_status = "offline"
		status_font = red

	network_status_label = font.render(network_status, 1, (status_font))
	screen.blit(network_status_label, (215,75))
	pygame.display.flip()

def main():
        while 1:
		for event in pygame.event.get():
#ensure there is always a safe way to end the program if the touch screen fails
	if event.type == KEYDOWN:
		if event.key == K_ESCAPE:
			sys.exit()
	time.sleep(0.2)        
	pygame.display.update()


#################### EVERTHING HAS NOW BEEN DEFINED ###########################

#set size of the screen
size = width, height = 320, 240
screen = pygame.display.set_mode(size)

#define colours
blue = 26, 0, 255
cream = 254, 255, 25
black = 0, 0, 0
white = 255, 255, 255
yellow = 255, 255, 0
red = 255, 0, 0
green = 0, 255, 0
refresh_menu_screen()  #refresh the menu interface 
main() #check for key presses and start emergency exit
station_name()

