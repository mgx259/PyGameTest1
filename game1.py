import sys, pygame
import random, os
from pygame.locals import *
from random import randint, choice
from lib_game1 import *


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


############
#   MAIN 
############


### VARIABLES
ver = 'v.0.01'

msg = 'Hi there!!!!'
msgGO = 'Game Over'


speed     = [-2, 2]
speed2    = [-3, -3]

alien_speed1   = [-3, -3]
alien_speed2   = [-2, 2]
bm1_speed      = [5, 0]
laser1_speed   = [10, 0]


mouse_x, mouse_y = 0, 0
#beam1_x, beam1_y = 0, 0
#beam_x, beam_y = 0, 0

beamsList    = []
atackersList = []

showBeam   = False
showLaser  = False
showDead   = False
#showDead2 = False
gameOver   = False


### PYGAME INIT

pygame.init()

fpsClock = pygame.time.Clock()

size = width, height = 1120, 700    #bg.get_size() # 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Invaiders '+ver)

black = pygame.Color(0, 0, 0)
white = pygame.Color(255,255,255)
red   = pygame.Color(255,0,0)
green = pygame.Color(0, 255, 0)
blue  = pygame.Color(0, 0, 255)


### LOADING RESOURCES

bg, bgRect           = loadImg('Space-2.jpg', 'Backgrounds')
l_aln1, aln1Rect   = loadImg('alienspaceship_left.png', 'Spaceships')
r_aln1, r_aln1Rect   = loadImg('alienspaceship_right.png', 'Spaceships')
d_aln, d_alnRect     = loadImg('alienspaceship_left_dead.png', 'Spaceships')
station, stationRect = loadImg('Spacestation.png')
beam1, beam1Rect     = loadImg('beam1_yellow_right.png', 'Weaporns')
lser1, laser1Rect    = loadImg('laser1_red.png', 'Weaporns')

sndAlien1 = loadSnd('alien-noise-01.wav')
sndLaser1 = loadSnd('laser-01.wav')

fntObj  = loadFont('Anita semi square.ttf', 32)



### SETTING COORDINATES

aln1Rect.x = bgRect.width - aln1Rect.width - 1
aln1Rect.y = aln1Rect.height + 1


aln2Rect   = aln1Rect.copy() 
#aln2Rect.x = bgRect.width - aln2Rect.width - 1
aln2Rect.y = bgRect.height - aln2Rect.height - 1

# aln3Rect   = aln1Rect.copy() 
# aln3Rect.x = bgRect.width - aln3Rect.width - 1
# aln3Rect.y = bgRect.height - aln3Rect.height - 1

stationRect.x = 10
stationRect.y = (bgRect.height / 2) - (stationRect.height / 2)


### POPULATING ATACKERS LIST
randint(1,3)
a1 = Atacker('KV1', getRndSpeed(), 10, l_aln1, r_aln1, aln1Rect, (bgRect.width, bgRect.height))
a2 = Atacker('KV2', getRndSpeed(), 10, l_aln1, r_aln1, aln2Rect, (bgRect.width, bgRect.height))
# a3 = Atacker('KV3', alien_speed1, 10, aln3Rect, (bgRect.width, bgRect.height))


atackersList.append(a1)
atackersList.append(a2)




########################
#       Main LOOP
########################

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            stationRect.y = mouse_y
        elif event.type == MOUSEBUTTONUP:
          #  beam1_x, beam1_y = event.pos
            beam1Rect.x = stationRect.width #    beam1_x #aln1Rect.x
            beam1Rect.y = stationRect.y + (stationRect.height / 2) #    beam1_y #aln1Rect.y
            beamsList.append(newBeam(len(beamsList), beam1Rect))
            print "Beam List size: {}".format(len(beamsList))
          #  print 'mouse X:Y = '+ str(beam1_x) +':'+ str(beam1_y)
          #  bm1_speed = (5, 0)
            sndLaser1.play()
         #   beam1Rect.move_ip(beam1_x, beam1_y)
         #   showBeam = True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            elif event.key == K_UP:
                speed[1] = -speed[1]


    screen.blit(bg, bgRect)
    screen.blit(station, stationRect)

### Processing Atackers

    # aln1Rect = aln1Rect.move(speed)

    # if aln1Rect.left < 0 or aln1Rect.right > width:
    #     speed[0] = -speed[0]
    # if aln1Rect.top < 0 or aln1Rect.bottom > height:
    #     speed[1] = -speed[1]

    # if aln1Rect.x < (bgRect.width * 0.2):
    #     gameOver = True    

    # screen.blit(kv1, aln1Rect)

################

    # aln2Rect = aln2Rect.move(speed2)
    # if aln2Rect.left < 0 or aln2Rect.right > width:
    #     speed2[0] = -speed2[0]
    # if aln2Rect.top < 0 or aln2Rect.bottom > height:
    #     speed2[1] = -speed2[1]        

    # if aln2Rect.x < (bgRect.width * 0.2):
    #     gameOver = True    

    # screen.blit(kv1, aln2Rect)
    for at in atackersList:
        print "--> moving: " + at.name + " with speed: "+ str(at.speed)
       # at.move()
        at.rect = at.rect.move(at.speed)
        at.checkBound()
        screen.blit(at.img, at.rect)
 

### Processing BEAMS
    for bm in beamsList:
        if bm['visible']:
            bm['rect'] = bm['rect'].move(bm['speed'])
            screen.blit(beam1, bm['rect'])
 #           beam1Rect = beam1Rect.move(bm1_speed)
#            screen.blit(beam1, beam1Rect)
     #       print 'Beam left {}, right {}, top {}, bottom {}'.format(beam1Rect.left, beam1Rect.right, beam1Rect.top, beam1Rect.bottom)

            if (bm['rect'].left > 0 and bm['rect'].right < width and 
                bm['rect'].top > 0 and bm['rect'].bottom < height):
                bm['visible'] = True
            else:
                bm['visible'] = False
                bm['speed'] = (0, 0)
                beamsList.remove(bm)

            if bm['rect'].colliderect(aln1Rect):
                print "Popal!!!!"
                d_alnRect.center = aln1Rect.center

                aln1Rect.x = bgRect.width - aln1Rect.width
                bm['visible'] = False
                bm['speed'] = (0, 0)
                beamsList.remove(bm)
                showDead = True
                sndAlien1.play()
           #     beam1Rect.x = bgRect.height + 1
         
            # if beam1Rect.colliderect(aln2Rect):
            #     print "Popal!!!!"
            #     kv2deadRect.center = aln2Rect.center
            #     aln2Rect.x = bgRect.width - aln2Rect.width
            #     bm1_speed = (0, 0)
            #     showBeam = False
            #     showDead2 = True
            #     sndAlien1.play()


###########
    if showDead :
        screen.blit(d_aln, d_alnRect)

    # if showDead2 :
    #     screen.blit(kv1dead, kv2deadRect)

######

    if gameOver:
        msgScreenObj = fntObj.render(msgGO, False, red)
        msgRect = msgScreenObj.get_rect()
        msgRect.topleft = (bgRect.width/2 - msgRect.width/2, bgRect.height/2 - msgRect.height/2)
        screen.blit(msgScreenObj, msgRect)
        speed = (0, 0)



    pygame.display.flip()
    fpsClock.tick(30)


