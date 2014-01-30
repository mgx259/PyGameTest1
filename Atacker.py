from GenObj import *

class Atacker(GenObj):
    """Basic enemy class"""
    speed = [0, 0]

    def __init__(self, name, hp, img_l, img_r, rect, boundries):
      #  self.__Speed = speed
        self.__HP = hp

        self.name = name
        self.initMove()
        self.hp = hp
        self.img = img_l
        self.img_l = img_l
        self.img_r = img_r
        self.rect = rect
        self.bound = boundries


    def checkBound(self):
        if self.rect.left < 0:
            self.speed[0] = self.speed[0] * -1
            self.img = self.img_r
        if self.rect.right > self.bound[0]:
            self.speed[0] = self.speed[0] * -1
            self.img = self.img_l
        if self.rect.top < 0 or self.rect.bottom > self.bound[1]:
            self.speed[1] = self.speed[1] * -1   


    def ai_decision(self):
        """ Take some "smart" decision """

        decision = {}
        decision['direction_change'] = self.changeDirection()
        decision['fire'] = self.fire()

        return decision