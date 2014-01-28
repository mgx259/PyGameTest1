import sys, pygame
from pygame.locals import *
from lib_game1 import *
from Atacker import *
from Player import *


############
#   MAIN 
############


### VARIABLES
ver = 'v.0.01'
cFPS = 30

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

cSpdChangeCounter = 100
spdCnt = cSpdChangeCounter


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
aln2Rect.y = bgRect.height - aln2Rect.height - 1

aln3Rect   = aln1Rect.copy() 
aln3Rect.y = bgRect.height - aln3Rect.height - 1



### POPULATING ATACKERS LIST
randint(1,3)
a1 = Atacker('KV1', getRndSpeed(), 10, l_aln1, r_aln1, aln1Rect, (bgRect.width, bgRect.height))
a2 = Atacker('KV2', getRndSpeed(), 10, l_aln1, r_aln1, aln2Rect, (bgRect.width, bgRect.height))
a3 = Atacker('KV3', getRndSpeed(), 10, l_aln1, r_aln1, aln3Rect, (bgRect.width, bgRect.height))

atackersList.append(a1)
atackersList.append(a2)
atackersList.append(a3)



plr = Player('MiR', 10, station, stationRect, (bgRect.width, bgRect.height))

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
            beam1Rect.x = plr.rect.centerx    
            beam1Rect.y = plr.rect.y + (plr.rect.height / 2) 
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
            elif event.key == K_w:
                print 'W'
                plr.changeSpeed([0, -2])
            elif event.key == K_s:
                print 'S'
                plr.changeSpeed([0, 2])
            elif event.key == K_a:
                print 'A'
                plr.changeSpeed([-2, 0])
            elif event.key == K_d:
                print 'D'
                plr.changeSpeed([2, 0])


    screen.blit(bg, bgRect)

    spdCnt -= 1

### Processing Atackers
    for at in atackersList:
        at.rect = at.rect.move(at.speed)
        at.checkBound()
        screen.blit(at.img, at.rect)
        if spdCnt < 0:
            at.move(getRndSpeed())
        # print "--> moving: " + at.name + " with speed: "+ str(at.speed)
       # at.move()
 
    # reseting speed change counter
    if spdCnt < 0:
        spdCnt = cSpdChangeCounter


### Processing Player
    plr.rect = plr.rect.move(plr.speed)
    plr.checkBound()
    screen.blit(plr.img, plr.rect)


### Processing BEAMS
    for bm in beamsList:
        targetIdx = 0
        targetObj = None

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

#            if bm['rect'].colliderect(aln1Rect):
            targetIdx = bm['rect'].collidelist(atackersList)
            if targetIdx > -1:
                targetObj = atackersList[targetIdx]
                print "Popal v "+ targetObj.name + " HP left: "+ str(targetObj.getHP())
                targetObj.hit(bm['damage'])
                d_alnRect.center = aln1Rect.center

                bm['visible'] = False
                bm['speed'] = (0, 0)
                beamsList.remove(bm)
                showDead = True
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
        speed = (0, 0)



    pygame.display.flip()
    fpsClock.tick(cFPS)


sys.exit()