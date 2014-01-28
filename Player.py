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

        self.speed = [0,0]

    def move_mouse(self, new_coord):
        self.rect.center = new_coord

    def changeSpeed(self, new_speed):
        tmpx = self.speed[0]
        tmpy = self.speed[1]

        tmpx += new_speed[0]
        if (abs(tmpx) > 2):
            pass
        else:
            self.speed[0] = tmpx

        tmpy += new_speed[1]
        if (abs(tmpy) > 2):
            pass
        else:
            self.speed[1] = tmpy
