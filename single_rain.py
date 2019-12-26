'''
Created on Mar 6, 2019

@author: Wyatt Muller
'''
import pyglet, random, project_runner
from single_character import Single_Character

class Rain():

    def __init__(self):
        self.overlap = False
        self.overlapped = False
        self.startX = 0
        self.start = 0
        self.head = 0
        self.drops = []
        self.leads = []
        self.time = 0
        self.stopped = False
        self.fading = False
        self.fadingIdx = 0
        self.default_color = (60, 150, 60)
        self.default_lead_color = (200, 255, 200)
        
        self.drops.append(Single_Character())
        self.rand_position()
        self.look_overlap()
        self.golden()
        if (not self.overlap):
            self.drops[0].x = self.startX
            self.drops[0].y = self.start
            self.leads.append(0)
            self.drops[0].color = self.default_lead_color
            self.time = (random.random()) + (project_runner.back.scale_y * 3)
            pyglet.clock.schedule_once(self.stop_update, self.time)
            
    def golden(self):
        chance = random.randint(1, 50)
        if chance == 1:
            self.default_color = (255, 223, 0)
            self.default_lead_color = (250, 250, 215)
        
    def rand_position(self):
        spacesX = random.randint(0, int(project_runner.window.width / self.drops[0].width) - 1)
        self.startX = spacesX * self.drops[0].width
        spacesY = random.randint(int(project_runner.window.height / (2 * self.drops[0].height)), int(project_runner.window.height / self.drops[0].height) - 1)
        self.head = spacesY * self.drops[0].height
        self.start = spacesY * self.drops[0].height
        
    def look_overlap(self):
        for obj in project_runner.rain_streaks:
            if ((obj.startX == self.startX) and (self.start <= obj.start and self.start >= (obj.head - self.drops[0].height))):
                self.overlap = True
                obj.overlapped = True
                
    def update(self):
        if self.overlapped:
            self.overlapped = False
            self.leads.append(0)
        if (self.head <= 0):
            self.stopped = True
        else:
            digitBelow = False
            for rain in project_runner.rain_streaks:
                if ((not rain.fading) and rain.startX == self.startX and rain.start == self.head - self.drops[-1].height):
                    digitBelow = True
                    rain.overlapped = True
                    self.stopped = True
            if not digitBelow:
                self.drops.append(Single_Character())
                self.head = self.head - self.drops[-1].height
                self.drops[-1].position = (self.startX, self.head)
        
    def stop_update(self, dt):
        self.stopped = True
        
    def start_fade(self, dt):
        for drop in self.drops:
            if (drop.opac - 20 <= 0):
                self.fadingIdx -= 1
                self.drops.remove(drop)
        if self.fadingIdx < len(self.drops):
            self.drops[self.fadingIdx].fade(0)
            self.fadingIdx += 1
        elif len(self.drops) == 0:
            if not project_runner.rain_streaks.count(self) == 0:
                project_runner.rain_streaks.remove(self)
        pyglet.clock.schedule_once(self.start_fade, 1/10)
        
    def update_leads(self):
        i = 0
        while i < len(self.leads):
            if (self.leads[i] == (len(self.drops) - 1)):
                self.drops[self.leads[i]].color = self.default_color
                del self.leads[i]
            else:
                self.drops[self.leads[i]].color = self.default_color
                self.leads[i] = self.leads[i] + 1
                self.drops[self.leads[i]].color = self.default_lead_color
            i = i + 1
                
                