def newBeam(nr, rect):
    newBeam = {'name': 'beam_'+str(nr), 
               'speed': [5,0], 
               'visible' : True,
               'rect' : rect
             }
    return newBeam