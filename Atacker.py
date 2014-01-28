from GenObj import *

class Atacker(GenObj):
    """Basic enemy class"""


    # boundries (w,h)
    def __init__(self, name, speed, hp, img_l, img_r, rect, boundries):
        self.__Speed = speed
        self.__HP = hp

        self.name = name
        self.speed = speed
        self.hp = hp
        self.img = img_l
        self.img_l = img_l
        self.img_r = img_r
        self.rect = rect
        self.bound = boundries
