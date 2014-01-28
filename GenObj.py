class GenObj():
    """General space object class"""

    __Speed = [0,0]
    __HP = 0

    def __init__(self, name, hp, img, rect, boundries):
        self.__Speed = speed
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
        pass

    def hit(self, damage):
        self.hp -= damage
        if (self.hp < 1):
            self.stop()

    def checkBound(self):
        if self.rect.left < 0:
            self.speed[0] = self.speed[0] * -1
            self.img = self.img_r
        if self.rect.right > self.bound[0]:
            self.speed[0] = self.speed[0] * -1
            self.img = self.img_l
        if self.rect.top < 0 or self.rect.bottom > self.bound[1]:
            self.speed[1] = self.speed[1] * -1      

    def getHP(self):
        return self.hp

    def move(self, new_speed):
        self.speed = new_speed
        #print "Speed of "+ self.name + " changed to "+ str(new_speed)