import random
from random import randint, choice

class GenObj():
    """General space object class"""

    __Speed = [0,0]
    __HP = 10
    __Alive = True
    __Weight = 100
    __moveCooldown = 50
    __fireCooldown = 20

    def __init__(self, name, hp, img, rect, boundries):
      #  self.__Speed = speed
        self.__HP = hp

        self.name = name
        self.hp = hp
        self.img = img
        self.rect = rect.copy()
        self.bound = boundries
        self.speed = [0,0]

    def stop(self):
        self.speed = [0,0]

    def start(self):
        self.speed = self.__Speed

    def fire(self):
        isChanged = False
        if self.__fireCooldown < 1:
            rnd = randint(1,10)

            if rnd > 3:
                isChanged = True
        return isChanged


    def hit(self, damage):
        self.hp -= damage
        if (self.hp < 1):
            self.stop()
            self.__Alive = False

    def checkBound(self):
        if self.rect.left < 0 or self.rect.right > self.bound[0]:
            self.speed[0] = self.speed[0] * -1
        if self.rect.top < 0 or self.rect.bottom > self.bound[1]:
            self.speed[1] = self.speed[1] * -1      

    def getHP(self):
        return self.hp

    def moveit(self):
        # if self.speed[0] == 0 and self.speed[1] == 0:
        #     return 1
        self.rect = self.rect.move(self.speed)
        self.checkBound()
        self.processCooldowns()
        self.ai_decision()


    def changeDirection(self):
        isChanged = False
        if self.__moveCooldown < 1:
            rnd = randint(1,10)

            if rnd > 5:
                self.speed = self.getRndSpeed()
                isChanged = True
        return isChanged


    def initMove(self):
        self.speed = self.getRndSpeed()

    def moveBack(self):
        self.speed[0] = self.speed[0] * -1 
        self.speed[1] = self.speed[1] * -1 


    def getRndSpeed(self):
        spd1 = choice((-2, -1, 1, 2))
        spd2 = choice((-3, -2, -1, 1, 2, 3))
        return [spd1, spd2]        

    def isAlive(self):
        return self.__Alive

    def setRndPosition(self, only_x=False, only_y=False):
        if not only_y:
            x = randint(0, self.bound[0] - self.rect.width)
            self.rect.x = x

        if not only_x:
            y = randint(0, self.bound[1] - self.rect.height)
            self.rect.y = y

    def ai_decision(self):
        #decision = {}
        return {}

    def setFireCooldown(self, cool=None):
        if cool:
            self.__fireCooldown = cool
        else:
            self.__fireCooldown = randint(20, 50)

    def setMoveCooldown(self, cool=None):
        if cool:
            self.__moveCooldown = cool
        else:
            self.__moveCooldown = randint(30, 70)

    def processCooldowns(self):
        self.__fireCooldown -= 1
        self.__moveCooldown -= 1

        if self.__moveCooldown == -1:
            self.setMoveCooldown()

        if self.__fireCooldown == -1:
            self.setFireCooldown()

