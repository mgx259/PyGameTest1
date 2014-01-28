class Atacker():
    """Basic enemy class"""
    __Speed = []
    __HP = 0

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
      #  self.rect.move(self.speed)
      #  print "Checking speed "+ str(self.speed)
        if self.rect.left < 0:
            self.speed[0] = self.speed[0] * -1
            self.img = self.img_r
        if self.rect.right > self.bound[0]:
            self.speed[0] = self.speed[0] * -1
            self.img = self.img_l
           # print "Vertikalnij BUM"
        if self.rect.top < 0 or self.rect.bottom > self.bound[1]:
            self.speed[1] = self.speed[1] * -1      
#            print "Gorizontalnij BUM"


    def getHP(self):
        return self.hp