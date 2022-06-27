###Imports
import pygame, os, time, random
from pygame.locals import *

###Function
def aperol_sprites(x, xscreen, yscreen, colour):
    #variables
    global counter

    #functions
    def counter_break(x):
        counter_break.list = []
        for i in str(x):
            counter_break.list.append(i)

    def display(x, y, xinit):
        for pos in x:
            pos = int(pos)
            current_number = y[pos]
            screen.blit(current_number, (xinit, 100))
            xinit = xinit + 32

    counter_break(counter)
    current_score = counter_break.list

    for i in x:
        screen.fill(colour)
        display(current_score, numbers, 100)
        screen.blit(i, (xscreen, yscreen))
        time.sleep(0.2)
        pygame.display.flip()
        

def format_bitch(x):
    frame_number = 0
    format_bitch.gif = []
    for frame in x:
        frame_number = frame_number + 1
        current_frame = 'frame' + str(frame_number) 
        current_frame = pygame.image.load(frame)
        format_bitch.gif.append(current_frame)

def six_frames_static(x):
    counter = 0
    six_frames_static.gif = []
    while counter < 6:
        six_frames_static.gif.append(x)
        counter = counter + 1

def score(numbers):
    #variables
    global counter

    #functions
    def counter_break(x):
        counter_break.list = []
        for i in str(x):
            counter_break.list.append(i)

    def display(x, y, xinit):
        for pos in x:
            pos = int(pos)
            current_number = y[pos]
            screen.blit(current_number, (xinit, 100))
            xinit = xinit + 32
            pygame.display.flip()

    counter_break(counter)
    current_score = counter_break.list
    display(current_score, numbers, 100)

#initial variables
counter = 0
colour = (255, 255, 0)

###Setup
#making the screen
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
screen.fill(colour)


#gifs
push_up_list = ['eric dong a push up-1.png', 'eric dong a push up-2.png', 'eric dong a push up-3.png', 'eric dong a push up-4.png', 'eric dong a push up-5.png', 'eric dong a push up-6.png']
format_bitch(push_up_list)
push_up_gifs = format_bitch.gif

six_frames_static('eric dong a push up-1.png')
eric_idle = six_frames_static.gif
format_bitch(eric_idle)
idle_eric_gif = format_bitch.gif

numbers_list = ['numbers for game-0.png', 'numbers for game-1.png', 'numbers for game-2.png', 'numbers for game-3.png', 'numbers for game-4.png', 'numbers for game-5.png', 'numbers for game-6.png', 'numbers for game-7.png', 'numbers for game-8.png', 'numbers for game-9.png']
format_bitch(numbers_list)
numbers = format_bitch.gif

###Main Event
while True:

    score(numbers)
    #checking for trigger or events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                aperol_sprites(push_up_gifs,  width/2, height/2, colour)
                counter = counter + 1
                screen.fill(colour)

    aperol_sprites(idle_eric_gif, width/2, height/2, colour)
    #score(numbers)
    pygame.display.flip()
    