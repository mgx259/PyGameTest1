import sys, pygame
import copy

from pygame.locals import *
from lib_game1 import *
from Atacker import *
from Player import *
from Weapon import *


### VARIABLES
ver = 'v.0.01'
cFPS = 30
cAICooldown = 50


spdCnt = cAICooldown


msg = 'Hi there!!!!'
msgGO = 'Game Over'
msgPlrHP = ''


mouse_x, mouse_y = 0, 0

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
l_aln1, aln1Rect     = loadImg('alienspaceship_left.png', 'Spaceships')
r_aln1, r_aln1Rect   = loadImg('alienspaceship_right.png', 'Spaceships')
d_aln, d_alnRect     = loadImg('alienspaceship_left_dead.png', 'Spaceships')
station, stationRect = loadImg('Spacestation.png')
beam1, beam1Rect     = loadImg('beam1_yellow_right.png', 'Weaporns')
laser1, laser1Rect   = loadImg('laser1_red.png', 'Weaporns')

sndAlien1 = loadSnd('alien-noise-01.wav')
sndLaser1 = loadSnd('laser-01.wav')
sndLaser2 = loadSnd('laser-02.wav')
powerup   = loadSnd('Power-Up.wav')


fntObj  = loadFont('Anita semi square.ttf', 12)
#fntGMObj  = loadFont('Anita semi square.ttf', 32)


### SETTING COORDINATES

aln1Rect.x = bgRect.width - aln1Rect.width - 1
aln1Rect.y = aln1Rect.height + 1


aln2Rect   = aln1Rect.copy() 
aln2Rect.y = bgRect.height - aln2Rect.height - 1

aln3Rect   = aln1Rect.copy() 
aln3Rect.y = bgRect.height - aln3Rect.height - 1



### POPULATING ATACKERS LIST

screen_bound = (bgRect.width, bgRect.height)

a1 = Atacker('KV1', 10, l_aln1, r_aln1, aln1Rect, screen_bound)
a2 = Atacker('KV2', 10, l_aln1, r_aln1, aln2Rect, screen_bound)
a3 = Atacker('KV3', 10, l_aln1, r_aln1, aln3Rect, screen_bound)

atackersList.append(a1)
atackersList.append(a2)
atackersList.append(a3)


### CREATING PLAYER OBJECT

plr = Player('MiR', 15, station, stationRect, screen_bound)

plr.rect.x = plr.rect.width + 5
plr.rect.y = (bgRect.height / 2) - (plr.rect.height / 2)

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
            #plr.move_mouse((plr.rect.width + 5, mouse_y))
        elif event.type == MOUSEBUTTONUP:
          #  beam1_x, beam1_y = event.pos
            beamsList.append(Weapon('beam_'+ str(len(beamsList)), 
                                     2, 5, 
                                     plr.rect.centerx, plr.rect.y + (plr.rect.height / 2),
                                     beam1, beam1Rect, sndLaser1)
            )

            print "Beam List size: {}".format(len(beamsList))
            sndLaser1.play()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            elif event.key == K_w:
               # print 'W'
                plr.changeSpeed([0, -2])
            elif event.key == K_s:
              #  print 'S'
                plr.changeSpeed([0, 2])
            elif event.key == K_a:
              #  print 'A'
                plr.changeSpeed([-2, 0])
            elif event.key == K_d:
              #  print 'D'
                plr.changeSpeed([2, 0])


    screen.blit(bg, bgRect)

    spdCnt -= 1

### Processing Atackers
    for at in atackersList:
        decision = None
        at.rect = at.rect.move(at.speed)
        at.checkBound()
        screen.blit(at.img, at.rect)

        msgPlrHP = str(at.getHP())
        msgScreenObj = fntObj.render(msgPlrHP, False, red)
        msgRect = msgScreenObj.get_rect()
        msgRect.topleft = (at.rect.x + (at.rect.width/2 - msgRect.width/2), at.rect.y - (msgRect.height + 2))
        screen.blit(msgScreenObj, msgRect)         

        # make some AI decision
        if spdCnt < 0:
            decision = at.ai_decision()

            if decision['fire']:
                laser1Rect.x = at.rect.centerx    
                laser1Rect.y = at.rect.y + (at.rect.height / 2) 
                beamsList.append(Weapon('laser_'+ str(len(beamsList)), 
                                         1, -7, 
                                         at.rect.x - (laser1Rect.width + 2), 
                                         at.rect.y + (at.rect.height / 2),
                                         laser1, laser1Rect, sndLaser2)
                )
              
                sndLaser2.play() 

            if decision['direction_change']:
                powerup.play()

    # reseting speed change counter
    if spdCnt < 0:
        spdCnt = cAICooldown


### Processing Player
    plr.rect = plr.rect.move(plr.speed)
    plr.checkBound()
    screen.blit(plr.img, plr.rect)

    # printing Player HP
    msgPlrHP = str(plr.getHP())
    msgScreenObj = fntObj.render(msgPlrHP, False, red)
    msgRect = msgScreenObj.get_rect()
    msgRect.topleft = (plr.rect.x + (plr.rect.width/2 - msgRect.width/2), plr.rect.y - (msgRect.height + 2))
    screen.blit(msgScreenObj, msgRect)    


### Processing BEAMS
    for bm in beamsList:
        targetIdx = 0
        targetObj = None

  #      print "BEAM: "+ bm.name + "  xy: "+ str(bm.pos) + " spd: "+str(bm.speed)
  #      print "rect: "+ str(bm.rect.left) + " - "+ str(bm.rect.right) +" - "+ str(bm.rect.top) + " - "+ str(bm.rect.bottom)

        bm.rect = bm.rect.move(bm.speed)
        screen.blit(bm.img, bm.rect)

        if (bm.rect.left > 0 and bm.rect.right < width and 
            bm.rect.top > 0 and bm.rect.bottom < height):
          #  bm.visible = True
            pass
        else:
            beamsList.remove(bm)

        targetIdx = bm.rect.collidelist(atackersList)
        if targetIdx > -1:
            targetObj = atackersList[targetIdx]
            print "Popal v "+ targetObj.name + " HP left: "+ str(targetObj.getHP())
            targetObj.hit(bm.damage)
            d_alnRect.center = aln1Rect.center
            beamsList.remove(bm)
 #           showDead = True
            sndAlien1.play()


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


    pygame.display.flip()
    fpsClock.tick(cFPS)


sys.exit()