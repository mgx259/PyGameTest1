import random
from random import randint, choice

class GenObj():
    """General space object class"""

    __Speed = [0,0]
    __HP = 10
    __Alive = True
    __Weight = 100

    def __init__(self, name, hp, img, rect, boundries):
      #  self.__Speed = speed
        self.__HP = hp

        self.name = name
        self.hp = hp
        self.img = img
        self.rect = rect
        self.bound = boundries

    def stop(self):
        self.speed = [0,0]

    def start(self):
        self.speed = self.__Speed

    def fire(self):
        rnd = randint(1,10)
        isChanged = False

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

    # def move(self, new_speed):
    #     self.speed = new_speed
    #     #print "Speed of "+ self.name + " changed to "+ str(new_speed)


    def changeDirection(self):
        rnd = randint(1,10)
        isChanged = False

        if rnd > 5:
            self.speed = self.getRndSpeed()
            isChanged = True
        return isChanged


    def initMove(self):
        self.speed = self.getRndSpeed()


    def getRndSpeed(self):
        spd1 = choice((-2, -1, 1, 2))
        spd2 = choice((-3, -2, -1, 1, 2, 3))
        return [spd1, spd2]        

    def isAlive(self):
        return self.__Alive

    def setRndPosition(self):
        x = randint(0, self.bound[0] - self.rect.width)
        y = randint(0, self.bound[1] - self.rect.height)
        self.rect.x = x
        self.rect.y = y
