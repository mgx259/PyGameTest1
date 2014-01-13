import sys, pygame
from pygame.locals import *

resPath = './res/'

pygame.init()


size = width, height = 973, 730 #bg.get_size() # 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space KV 1')


speed     = [-2, 2]
speed2    = [-2, 2]

bm1_speed = [5, 0]

black = pygame.Color(0, 0, 0)
white = pygame.Color(255,255,255)
red   = pygame.Color(255,0,0)
green = pygame.Color(0, 255, 0)
blue  = pygame.Color(0, 0, 255)

mouse_x, mouse_y = 0, 0
beam1_x, beam1_y = 0, 0
#beam_x, beam_y = 0, 0

# kv1 = pygame.image.load("kv1.gif")
bg    = pygame.image.load(resPath+"Space-1.jpg").convert()
kv1   = pygame.image.load(resPath+"tank_kv_small.png").convert()
kv1dead   = pygame.image.load(resPath+"tank_kv_dead.png").convert()
station = pygame.image.load(resPath+"Spacestation.png").convert()
beam1 = pygame.image.load(resPath+"beams.png")#.convert()


kv1.set_colorkey(black)
kv1dead.set_colorkey(white)
station.set_colorkey(black)
#beam1.set_colorkey(black)

sndAlien1 = pygame.mixer.Sound(resPath+'snd/alien-noise-01.wav')
sndLaser1 = pygame.mixer.Sound(resPath+'snd/laser-01.wav')

fntObj = pygame.font.Font(resPath+'Fonts/Anita semi square.ttf', 32)
msg = 'Hi there!!!!'
msgGO = 'Game Over'

fpsClock = pygame.time.Clock()


bgRect  = bg.get_rect()

kv1Rect = kv1.get_rect()
kv1Rect.x = bgRect.width - kv1Rect.width

kv2Rect = kv1.get_rect()
kv2Rect.x = bgRect.width - kv2Rect.width
kv2Rect.y = bgRect.height - kv2Rect.height

kv1deadRect = kv1dead.get_rect()
kv2deadRect = kv1dead.get_rect()

beam1Rect = beam1.get_rect()

stationRect = station.get_rect()
stationRect.x = 10
stationRect.y = (bgRect.height / 2) - (stationRect.height / 2)

#beamsList = []
#kv1List   = []

########################

showBeam = False
showDead = False
showDead2 = False
gameOver = False

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
            beam1Rect.x = stationRect.width #    beam1_x #kv1Rect.x
            beam1Rect.y = stationRect.y + (stationRect.height / 2) #    beam1_y #kv1Rect.y
          #  print 'mouse X:Y = '+ str(beam1_x) +':'+ str(beam1_y)
            bm1_speed = (5, 0)
            sndLaser1.play()
         #   beam1Rect.move_ip(beam1_x, beam1_y)
            showBeam = True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            elif event.key == K_UP:
                speed[1] = -speed[1]


    screen.blit(bg, bgRect)
    screen.blit(station, stationRect)

################

    kv1Rect = kv1Rect.move(speed)

    if kv1Rect.left < 0 or kv1Rect.right > width:
        speed[0] = -speed[0]
    if kv1Rect.top < 0 or kv1Rect.bottom > height:
        speed[1] = -speed[1]

    if kv1Rect.x < (bgRect.width * 0.2):
        gameOver = True    

    screen.blit(kv1, kv1Rect)

################

    kv2Rect = kv2Rect.move(speed2)
    if kv2Rect.left < 0 or kv2Rect.right > width:
        speed2[0] = -speed2[0]
    if kv2Rect.top < 0 or kv2Rect.bottom > height:
        speed2[1] = -speed2[1]        

    if kv2Rect.x < (bgRect.width * 0.2):
        gameOver = True    

    screen.blit(kv1, kv2Rect)

 

    if showBeam:
        beam1Rect = beam1Rect.move(bm1_speed)
        screen.blit(beam1, beam1Rect)
        print 'Beam left {}, right {}, top {}, bottom {}'.format(beam1Rect.left, beam1Rect.right, beam1Rect.top, beam1Rect.bottom)

        if (beam1Rect.left > 0 and beam1Rect.right < width and 
            beam1Rect.top > 0 and beam1Rect.bottom < height):
            showBeam = True
        else:
            showBeam = False
            bm1_speed = (0, 0)

        if beam1Rect.colliderect(kv1Rect):
            print "Popal!!!!"
            kv1deadRect.center = kv1Rect.center
            kv1Rect.x = bgRect.width - kv1Rect.width
            bm1_speed = (0, 0)
            showBeam = False
            showDead = True
            sndAlien1.play()
       #     beam1Rect.x = bgRect.height + 1
     
        if beam1Rect.colliderect(kv2Rect):
            print "Popal!!!!"
            kv2deadRect.center = kv2Rect.center
            kv2Rect.x = bgRect.width - kv2Rect.width
            bm1_speed = (0, 0)
            showBeam = False
            showDead2 = True
            sndAlien1.play()

    if showDead :
        screen.blit(kv1dead, kv1deadRect)

    if showDead2 :
        screen.blit(kv1dead, kv2deadRect)


    if gameOver:
        msgScreenObj = fntObj.render(msgGO, False, red)
        msgRect = msgScreenObj.get_rect()
        msgRect.topleft = (bgRect.width/2 - msgRect.width/2, bgRect.height/2 - msgRect.height/2)
        screen.blit(msgScreenObj, msgRect)
        speed = (0, 0)

    pygame.display.flip()

    fpsClock.tick(30)