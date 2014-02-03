import sys, pygame
from pygame.locals import *

from lib_game1 import *
from random import *
from Atacker import *
from GenObj import *

#fpsClock = 30
cFPS = 30


pygame.init()

fpsClock = pygame.time.Clock()

size = width, height = 1120, 700    #bg.get_size() # 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Testing')

bg, bgRect           = loadImg('Space-3.jpg', 'Backgrounds')
screen_bound = (600, 400)

l_aln1, aln1Rect     = loadImg('alienspaceship_left.png', 'Spaceships')
#r_aln1, r_aln1Rect   = loadImg('alienspaceship_right.png', 'Spaceships')
d_aln, d_alnRect     = loadImg('alienspaceship_left_dead.png', 'Spaceships')

astr, astrRect = loadImg('Asteroid_small_1.png')

alnPrt1, alnPrt1Rect   = loadImg('cockpit.png', 'Spaceships')
alnPrt2, alnPrt2Rect   = loadImg('wing_l1.png', 'Spaceships')
alnPrt3, alnPrt3Rect   = loadImg('wing_r1.png', 'Spaceships')
alnPrt4, alnPrt4Rect   = loadImg('wing_r2.png', 'Spaceships')


bombs = []

for i in range(1,10):
    bomb1, bomb1Rect = loadImg('aliendropping000'+ str(i) +'.png', 'Alien-Bomb')
    bombs.append([bomb1, bomb1Rect])

bomb1Rect.x = 300
bomb1Rect.y = 1


a1 = Atacker('Alien_test1', 10, l_aln1, aln1Rect, screen_bound)
a1.__Alive = False
a1.speed = [5, 0]

ast1 = GenObj('Asteroid_1', 50, astr, astrRect, screen_bound)

#print "is alive {}".format(a1.__Alive)


bCnt = 0
newPicCnt = 0

print "Bombs len = {}".format(len(bombs))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))     
            if event.key == K_a:  
                a1.img = pygame.transform.flip(a1.img, True, False)

    a1.__Alive = False
    a1.moveit()

    screen.blit(bg, bgRect)
    screen.blit(a1.img, a1.rect)


 #   for bb in bombs
    bomb1Rect = bomb1Rect.move([0, 3])
    print "bcnt = {}".format(bCnt)
    screen.blit(bombs[bCnt][0], bomb1Rect)

    if newPicCnt > 5:
        print "inc"
        bCnt += 1
        if bCnt > len(bombs)-1:
            bCnt = 0
        newPicCnt = 1

    newPicCnt +=1





    pygame.display.flip()
    fpsClock.tick(cFPS)