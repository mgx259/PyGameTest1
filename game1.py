import sys, pygame
#import copy

from pygame.locals import *
from lib_game1 import *
from Atacker import *
from Player import *
from Weapon import *


### CONSTANTS
cVer = 'v.0.01'
cFPS = 30
cAliens = 4
cAsteroids = 3

cPlayerBeamSpd = 8
cPlayerBeamDmg = 2
cAlienBeamSpd  = -15
cAlienBeamDmg  = 1


msgGO = 'Game Over :('
msgWIN = 'You Win :)'
msgPlrHP = ''
finalMsg = ''

mouse_x, mouse_y = 0, 0

beamsList    = []
atackersList = []
deadList     = []
allObjList   = []


### PYGAME INIT
pygame.init()

fpsClock = pygame.time.Clock()

size = width, height = 1120, 700    #bg.get_size() # 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Invaiders '+cVer)

black = pygame.Color(0, 0, 0)
white = pygame.Color(255,255,255)
red   = pygame.Color(255,0,0)
green = pygame.Color(0, 255, 0)
blue  = pygame.Color(0, 0, 255)


### LOADING RESOURCES
bg, bgRect           = loadImg('Space-2.jpg', 'Backgrounds')
screen_bound = (bgRect.width, bgRect.height)

l_aln1, aln1Rect     = loadImg('alienspaceship_left.png', 'Spaceships')
r_aln1, r_aln1Rect   = loadImg('alienspaceship_right.png', 'Spaceships')
d_aln, d_alnRect     = loadImg('alienspaceship_left_dead.png', 'Spaceships')

alnPrt1, alnPrt1Rect   = loadImg('cockpit.png', 'Spaceships')
alnPrt2, alnPrt2Rect   = loadImg('wing_l1.png', 'Spaceships')
alnPrt3, alnPrt3Rect   = loadImg('wing_r1.png', 'Spaceships')
alnPrt4, alnPrt4Rect   = loadImg('wing_r2.png', 'Spaceships')

station, stationRect = loadImg('Spacestation.png')
astr, astrRect = loadImg('Asteroid_small_1.png')

beam1, beam1Rect     = loadImg('beam1_yellow_2.png', 'Weaporns')
laser1, laser1Rect   = loadImg('laser1_red.png', 'Weaporns')

sndAlien1 = loadSnd('alien-noise-01.wav')
sndLaser1 = loadSnd('laser-01.wav')
sndLaser2 = loadSnd('laser-02.wav')
powerup   = loadSnd('Power-Up.wav')


fntObj    = loadFont('Anita semi square.ttf', 12)
fntGMObj  = loadFont('Anita semi square.ttf', 48)


### CREATING PLAYER OBJECT
plr = Player('MiR', 15, station, stationRect, screen_bound)
plr.rect.x = plr.rect.width + 5
plr.rect.y = (bgRect.height / 2) - (plr.rect.height / 2)

allObjList.append(plr)


# placementRetries = 20
# colisionDetected = True

### POPULATING ATACKERS LIST
for ast_i in range(cAliens):
    a1 = Atacker('Alien_'+str(ast_i), 10, l_aln1, aln1Rect, screen_bound)

    colisionDetected = True
    placementRetries = 10
    while colisionDetected or placementRetries > 0:
        a1.setRndPosition(False, True)
        colisionDetected = checkCollision(a1.rect, allObjList)
        placementRetries -= 1

    if not colisionDetected:
        allObjList.append(a1)
        atackersList.append(a1)
    else:
        print "Cant plase {} after {} attempts".format(a1.name, 10)


### POPULATING ASTEROIDS
for ast_i in range(cAsteroids):
    ast1 = GenObj('Asteroid_'+str(ast_i), 50, astr, astrRect, screen_bound)

    colisionDetected = True
    placementRetries = 10
    # while placementRetries > 0:
    while colisionDetected or placementRetries > 0:
        ast1.setRndPosition()
        colisionDetected = checkCollision(ast1.rect, allObjList)
        placementRetries -= 1

    if not colisionDetected:
        allObjList.append(ast1)
        deadList.append(ast1)
    else:
        print "Cant plase {} after {} attempts".format(a1.name, 10)



########################
#       Main LOOP
########################

while len(finalMsg) == 0:
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
                                     cPlayerBeamDmg, cPlayerBeamSpd, 
                                     plr.rect.x + plr.rect.width + beam1Rect.width +1, 
                                     plr.rect.y + (plr.rect.height / 2),
                                     beam1, beam1Rect, sndLaser1)
            )
    #        print "Beam List size: {}".format(len(beamsList))
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

  #  spdCnt -= 1


### Processing all Objects
    for at in allObjList:
        decision = None
        at.moveit()



        screen.blit(at.img, at.rect)

        # print object HP if it's alive
        if at.getHP() > 0:
            msgPlrHP = str(at.getHP())
            msgScreenObj = fntObj.render(msgPlrHP, False, red)
            msgRect = msgScreenObj.get_rect()
            msgRect.topleft = (at.rect.x + (at.rect.width/2 - msgRect.width/2), at.rect.y - (msgRect.height + 2))
            screen.blit(msgScreenObj, msgRect)         

        # make some AI decision
        decision = at.ai_decision()

        if 'fire' in decision and decision['fire']:
            laser1Rect.x = at.rect.centerx    
            laser1Rect.y = at.rect.y + (at.rect.height / 2) 
            beamsList.append(Weapon('laser_'+ str(len(beamsList)), 
                                     cAlienBeamDmg, cAlienBeamSpd, 
                                     at.rect.x - (laser1Rect.width + 2), 
                                     at.rect.y + (at.rect.height / 2),
                                     laser1, laser1Rect, sndLaser2)
            )
          
            sndLaser2.play() 

        if 'direction_change' in decision and decision['direction_change']:
            powerup.play()


### Processing BEAMS
    for bm in beamsList:
        targetIdx = 0
        targetObj = None

        bm.rect = bm.rect.move(bm.speed)
        screen.blit(bm.img, bm.rect)

        if (bm.rect.left > 0 and bm.rect.right < width and 
            bm.rect.top > 0 and bm.rect.bottom < height):
            pass
        else:
            beamsList.remove(bm)
            continue

        ### hit object
        targetIdx = bm.rect.collidelist(atackersList)
        if targetIdx > -1:
            targetObj = atackersList[targetIdx]
            print "Popal v {}; HP left: {} isAlive: {}".format(targetObj.name, targetObj.getHP(), targetObj.isAlive())
            targetObj.hit(bm.damage)
            beamsList.remove(bm)
            sndAlien1.play()
            #d_alnRect.center = aln1Rect.center
            if not targetObj.isAlive():
                deadList.append(targetObj)
                atackersList.remove(targetObj)
            continue

        ### hit dead object 
        targetIdx = bm.rect.collidelist(deadList)
        if targetIdx > -1:
            targetObj = deadList[targetIdx]
            print "Popal v "+ targetObj.name + " HP left: "+ str(targetObj.getHP())
            targetObj.hit(bm.damage)
            beamsList.remove(bm)
            sndAlien1.play()
            #d_alnRect.center = aln1Rect.center
            # if not targetObj.isAlive():
            #     deadList.append(targetObj)
            #     atackersList.remove(targetObj)
            continue

        ### hit player
        if bm.rect.colliderect(plr.rect):
            plr.hit(bm.damage)
            beamsList.remove(bm)
            sndAlien1.play()
            continue

    ### process colisions
    for obj in allObjList:
        allObjList.remove(obj)
        targetIdx = obj.rect.collidelist(allObjList)
        if targetIdx > -1:
            obj.moveBack()
            allObjList[targetIdx].moveBack()
        allObjList.append(obj)

    ### player lost
    if plr.getHP() < 1:
        gameOver = True
        finalMsg = msgGO

    ### win if no atckers left
    if len(atackersList) == 0:
        gameWon = True
        finalMsg = msgWIN

    pygame.display.flip()
    fpsClock.tick(cFPS)


### show final message
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN: 
            pygame.quit()
            sys.exit()

    screen.blit(bg, bgRect)


    for at in allObjList:
        decision = None
        screen.blit(at.img, at.rect)

        # print object HP if it's alive
        if at.getHP() > 0:
            msgPlrHP = str(at.getHP())
            msgScreenObj = fntObj.render(msgPlrHP, False, red)
            msgRect = msgScreenObj.get_rect()
            msgRect.topleft = (at.rect.x + (at.rect.width/2 - msgRect.width/2), at.rect.y - (msgRect.height + 2))
            screen.blit(msgScreenObj, msgRect)  



    msgScreenObj = fntGMObj.render(finalMsg, False, red)
    msgRect = msgScreenObj.get_rect()
    msgRect.topleft = (bgRect.width/2 - msgRect.width/2, bgRect.height/2 - msgRect.height/2)
    screen.blit(msgScreenObj, msgRect)

    pygame.display.flip()


pygame.quit()
sys.exit()