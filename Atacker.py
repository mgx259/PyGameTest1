from GenObj import *

class Atacker(GenObj):
    """Basic enemy class"""
   # speed = [0, 0]
  #  __Alive = True

    def __init__(self, name, hp, img, rect, boundries):

        GenObj.__init__(self, name, hp, img, rect, boundries)
        self.__HP = hp
        # self.__Alive = True
        self.setAlive()

        self.name = name
        self.initMove()
        self.hp = hp
        self.img = img
        self.rect = rect.copy()
        self.bound = boundries

        self.rect.x = self.bound[0] - self.rect.width - 1
        self.setRndPosition(False, True)


    def ai_decision(self):
        """ Take some "smart" decision """
        decision = {}
        decision['direction_change'] = False
        decision['fire'] = False

      #  print "AI decision"
        if self.isAlive():
         #   print "HE HE HE: {}".format(self.isAlive())
            decision['direction_change'] = self.changeDirection()
            # if not (decision['direction_change']):
            decision['fire'] = self.fire()

        return decision