from GenObj import *

class Player(GenObj):
    """Basic Player calss"""

    def __init__(self, name, hp, img, rect, boundries):
#        self.__Speed = speed
#        self.__HP = hp
        self.name = name
        self.hp = hp
        self.img = img
        self.rect = rect
        self.bound = boundries