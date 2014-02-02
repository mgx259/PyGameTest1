#from GenObj import *

class Weapon():
    """Basic Weapon calss"""

    def __init__(self, name, damage, speed, x, y, img, rect, snd):
        self.name = name
        self.damage = damage
        self.speed = (speed, 0)

        self.img = img
        self.rect = rect

       # self.pos = (x, y)
        self.rect.x = x
        self.rect.y = y

        self.snd = snd
        self.visible = True
        # self.target_xy

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def setPos(self, x, y):
        self.pos = (x, y)

