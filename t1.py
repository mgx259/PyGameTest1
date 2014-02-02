import sys

from lib_game1 import *
from random import randint





atackersList = []

a1 = {'name': 'kv1_1', 'speed': [2,2], 'hp': 10}

a2 = a1.copy()
a2['name'] = 'kv1_2'

a1['hp'] = 20

atackersList.append(a1)
atackersList.append(a2)
atackersList.append({'name': 'kv1_3', 'speed': [1,3], 'hp': 12})

# print atackersList


beamsList = []
beamsPool = []

i = 0

while i < 5:
    beamsList.append(newBeam(len(beamsList), 'rect'))
    i += 1



for bm in beamsList:
    print bm['name'] + ' - '+ str(randint(2,6))

#################

aa = Atacker('tigra', [-2, 2], 10, (12,34), (100,200))
ab = Atacker('IS',    [-2, 2], 10, (54,87), (100,200))

atackersList = []

atackersList.append(aa)
atackersList.append(ab)


for at in atackersList:
    if (at.name == 'tigra'):
        at.stop()
    print at.name +" - "+ str(at.speed)
