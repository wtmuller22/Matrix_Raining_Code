'''
Created on Mar 5, 2019

@author: Wyatt Muller
'''

import pyglet, random, gc
from pyglet import image

class Single_Character(pyglet.sprite.Sprite):

    digitArray = [image.load('Numbers/zero.png'), 
                  image.load('Numbers/One.png'), 
                  image.load('Numbers/Two.png'), 
                  image.load('Numbers/Three.png'),
                  image.load('Numbers/Four.png'),
                  image.load('Numbers/Five.png'),
                  image.load('Numbers/Six.png'),
                  image.load('Numbers/Seven.png'),
                  image.load('Numbers/Eight.png'),
                  image.load('Numbers/Nine.png')]
    

    def __init__(self):
        super().__init__(img=self.digitArray[0])
        self.opac = 255
        self.randImage()
        self.color = (0, 128, 0)
        self.scale = (1/3)
        self.opacity = self.opac 
        self.time = random.randint(0, 3)
        if not self.time == 0:
            pyglet.clock.schedule_interval(self.update, 1 / self.time)
        
    def randImage(self):
        num = random.randint(0, 9)
        self.image = self.digitArray[num]
    
    def update(self, dt):
        self.randImage()
        
    def fade(self, dt):
        if self.opac - 20 <= 0:
            pyglet.clock.unschedule(self.update)
        else:
            self.opac = self.opac - 20
            pyglet.clock.schedule_once(self.fade, 1/45)
        