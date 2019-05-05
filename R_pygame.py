import pygame, datetime, os, subprocess, sys, time
import RPi.GPIO as GPIO
#from pygame.locals import *
##import time
##import datetime
##import sys
##import os
##import glob
##import subprocess
i = 230
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, 1)
GPIO.setup(13, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(13, GPIO.RISING)
GPIO.setup(26, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(26, GPIO.RISING)
GPIO.setup(19, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(19, GPIO.RISING)

pygame.display.set_caption("Radiosteuerung")
screen = pygame.display.set_mode((520, 300))
pygame.mouse.set_visible(1)
pygame.key.set_repeat(1, 30)
pygame.font.init()
font = pygame.font.SysFont("lato", 15, 1, 0)
font_color = (   0,   0,   0)
pygame.init()

#skin2 = pygame.image.load("/home/pi/python-GUI/3.bmp")
skin1 = pygame.image.load("2.png")

subprocess.call('mpc volume 0', shell=True)
clock = pygame.time.Clock()
running = 1

def station_pos():
## STATIONS 1
    pygame.draw.rect(screen, (font_color), (5,50,40,10), 1)
    screen.blit(font.render("YouFM", 1, (font_color)), (55,45))
    pygame.draw.rect(screen, (font_color), (45,70,40,10), 1)
    screen.blit(font.render("Radio BOB", 1, (font_color)), (95,65))
    pygame.draw.rect(screen, (font_color), (85,90,40,10), 1)
    screen.blit(font.render("Regenbogen2", 1, (font_color)), (135,85))
    pygame.draw.rect(screen, (font_color), (125,110,40,10), 1)
    screen.blit(font.render("SWR3", 1, (font_color)), (175,105))
    pygame.draw.rect(screen, (font_color), (165,130,40,10), 1)
    screen.blit(font.render("HR3", 1, (font_color)), (215,125))
## STATIONS 2    
    pygame.draw.rect(screen, (font_color), (205,50,40,10), 1)
    screen.blit(font.render("Radio Fritz", 1, (font_color)), (255,45))
    pygame.draw.rect(screen, (font_color), (245,70,40,10), 1)
    screen.blit(font.render("HRinfo", 1, (font_color)), (295,65))
    pygame.draw.rect(screen, (font_color), (285,90,40,10), 1)
    screen.blit(font.render("Deutschlandfunk", 1, (font_color)), (335,85))
    pygame.draw.rect(screen, (font_color), (325,110,40,10), 1)
    screen.blit(font.render("SWR3", 1, (font_color)), (375,105))
    pygame.draw.rect(screen, (font_color), (365,130,40,10), 1)
    screen.blit(font.render("SWR3", 1, (font_color)), (415,125))

##def station_pos end
def stationselector():
    pygame.draw.line(screen, (200,200,200), (i,50),(i,140), 7)
    pygame.draw.line(screen, (125,0,0), (i,50),(i,140), 3)
    pygame.draw.line(screen, (255,0,0), (i,50),(i,140), 1)


        
while running:
##Lade variablen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    clock.tick(30)    
    screen.fill((255, 255, 255))
    current_time = datetime.datetime.now().strftime('%H:%M:%S  %d.%m.%Y')
    time_label = font.render(current_time, 1,(font_color))
    volume = subprocess.check_output('mpc volume', shell=True)
    volume_name = font.render("Lautstärke: ", 1, (font_color))
    volume_label = font.render(volume[7:11], 1, (font_color))
    txtlines = subprocess.check_output('mpc current', shell=True)
    station_txt = font.render(txtlines[0:71], 1, (font_color))
    
    vol0 = volume[7]-48
    if vol0 <= 0:
        vol0 = 0
    vol0 *= 120
    vol1 = volume[8]-48
    if vol1 <= 0:
        vol1 = 0
    vol1 *= 10
    vol2 = volume[9]-48
    if vol2 <= 0:
        vol2 = 0
    vol = vol0+vol1+vol2
    vol *= 5
    
##Lade variablen ende
##-------------------------------------------------
##Bilder einbinden
##    screen.blit(skin1, (0,50))
##Bilder einbinden ende
##-------------------------------------------------
##TextAusgabe
    pygame.draw.rect(screen, (font_color), (0,0,519,18), 2)    
    screen.blit(volume_name,  (  5,  0))
    screen.blit(volume_label, ( 85,  0))
    screen.blit(time_label,   (360,  0))
    
    pygame.draw.rect(screen, (font_color), (0,17,519,24), 2)
    screen.blit(station_txt,  ( 5,20))
    station_pos()
    
    pygame.draw.rect(screen, (font_color), (0,44,519,100), 2)
    
    stationselector()
    pygame.draw.rect(screen, (font_color), (0,147,519,10), 2)
    pygame.draw.rect(screen, (font_color), (0,147,vol,10))
    

##TextAusgabe ende
##-------------------------------------------------##    pygame.draw.rect(screen, (0,0,0), (10,10,50,50), 2)
##Encoder begin
    
    #if Flag_station_select == station_selected:
        #alert_txt = "Normal"
    #else:
        #alert_txt = subprocess.check_output(station_selected, shell=True)
    #Flag_station_select = station_selected
    if GPIO.event_detected(13):
       # alert_txt = "Pin 21"
        i = i-10
        if i <= 10:
            i = 11
        if i >= 400:
            i = 399
        if i >= 5 and i <= 45:
            station_selected = "mpc play 1"
        if i >= 45 and i <= 85:
            station_selected = "mpc play 2"
        if i >= 85 and i <= 125:
            station_selected = "mpc play 3"
        if i >= 125 and i <= 165:
            station_selected = "mpc play 4"
        if i >= 165 and i <= 205:
            station_selected = "mpc play 5"
        if i >= 205 and i <= 245:
            station_selected = "mpc play 6"
        if i >= 245 and i <= 285:
            station_selected = "mpc play 7"
        if i >= 285 and i <= 325:
            station_selected = "mpc play 8"
        if i >= 325 and i <= 365:
            station_selected = "mpc play 9"
        if i >= 365 and i <= 405:
            station_selected = "mpc play 10"
        #alert_txt1 = font.render(station_selected, 1, (fontcolor))
    if GPIO.event_detected(19):
        #alert_txt = "Pin 20"
        i = i+10
        if i <= 10:
            i = 11
        if i >= 400:
            i = 399
        if i >= 5 and i <= 45:
            station_selected = "mpc play 1"
        if i >= 45 and i <= 85:
            station_selected = "mpc play 2"
        if i >= 85 and i <= 125:
            station_selected = "mpc play 3"
        if i >= 125 and i <= 165:
            station_selected = "mpc play 4"
        if i >= 165 and i <= 205:
            station_selected = "mpc play 5"
        if i >= 205 and i <= 245:
            station_selected = "mpc play 6"
        if i >= 245 and i <= 285:
            station_selected = "mpc play 7"
        if i >= 285 and i <= 325:
            station_selected = "mpc play 8"
        if i >= 325 and i <= 365:
            station_selected = "mpc play 9"
        if i >= 365 and i <= 405:
            station_selected = "mpc play 10"
        #alert_txt1 = font.render(station_selected, 1, (fontcolor))
    if GPIO.event_detected(26):
        #alert_txt = "Pin 16"
        i = 200
        if i <= 10:
            i = 11
        if i >= 400:
            i = 399
        if i >= 5 and i <= 45:
            station_selected = "mpc play 1"
        if i >= 45 and i <= 85:
            station_selected = "mpc play 2"
        if i >= 85 and i <= 125:
            station_selected = "mpc play 3"
        if i >= 125 and i <= 165:
            station_selected = "mpc play 4"
        if i >= 165 and i <= 205:
            station_selected = "mpc play 5"
        if i >= 205 and i <= 245:
            station_selected = "mpc play 6"
        if i >= 245 and i <= 285:
            station_selected = "mpc play 7"
        if i >= 285 and i <= 325:
            station_selected = "mpc play 8"
        if i >= 325 and i <= 365:
            station_selected = "mpc play 9"
        if i >= 365 and i <= 405:
            station_selected = "mpc play 10"
        #alert_txt1 = font.render(station_selected, 1, (fontcolor))
        
    
    

##Encoder end
##-------------------------------------------------##    pygame.draw.rect(screen, (0,0,0), (10,10,50,50), 2)
##Button begin
##        #   X + W              X       Y + H              Y
##    if 200+50 > mouse[0] >200 and 100+50 > mouse[1] >100:
##        pygame.draw.rect(screen, (50,50,50), (200,100,50,50))
##        alert_txt1 = "ready"
##        if click[0] == 1:
##            subprocess.check_output('mpc volume +5', shell=True)
##            alert_txt1 = "click"
##    else:
##        pygame.draw.rect(screen, (100,100,100),(200,100,50,50))
##        alert_txt1 = "1"
##  Button end
##-------------------------------------------------
##Quitschleife       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            pygame.event.post(pygame.event.Event(pygame.QUIT))           
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()
                pygame.event.post(pygame.event.Event(pygame.QUIT))
##        if GPIO.event_detected(21):
##            alert_txt = "Pin 21"
##Quitschleife ende
##-------------------------------------------------
##Screenrefresh
    pygame.display.flip()
##Screenrefresh ende
