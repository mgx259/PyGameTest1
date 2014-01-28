import os, pygame
import random
from random import randint, choice


def newBeam(nr, rect):
    newBeam = {'name': 'beam_'+str(nr), 
               'speed': [5,0], 
               'visible' : True,
               'rect' : rect,
               'damage' : 2
             }
    return newBeam


def loadImg(file_name, img_type=''):
    """Loading image file"""
    full_name = os.path.join('res','Img', img_type, file_name)
    try:
        img = pygame.image.load(full_name)
    except pygame.error, message:
        print 'Cant load image: ', full_name
        raise SystemExit, message

    img = img.convert_alpha()

    return img, img.get_rect()

def loadSnd(file_name):
    """Loading sound file"""    
    class NoSnd:
        """No Sound class"""
        def play(self):
            pass
            
    if not pygame.mixer or not pygame.mixer.get_init():
       return NoSnd()

    full_name = os.path.join('res', 'Snd', file_name)
    try:
        snd = pygame.mixer.Sound(full_name)
    except pygame.error, message:
        print 'Cant load sound: ', full_name
        #raise SystemExit, message  
        return NoSnd()

    return snd  


def loadFont(file_name, font_size):
    full_name = os.path.join('res', 'Fonts', file_name)
    try:
        fnt = pygame.font.Font(full_name, font_size)
    except pygame.error, message:
        print 'Cant load font: ', full_name
        raise SystemExit, messag


def getRndSpeed():
    spd1 = choice((-2, -1, 1, 2))
    spd2 = choice((-3, -2, -1, 1, 2, 3))
#    spd2 = randint(-3,3)
    return [spd1, spd2]

