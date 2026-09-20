
from math import floor
from conf import SCALE

class Animation:
    def __init__(self, spritesheet, rowIndex, speed):
        self.spritesheet = spritesheet
        self.yFrame = rowIndex
        self.frame = 0
        self.speed = speed
        return


    def update(self):
        self.frame += self.speed
        return

    def draw(self, surface, x, y, scale=SCALE, rot=0, refPoint="centre"):
        xFrame = floor(self.frame) % self.spritesheet.xFrames
        self.spritesheet.draw(
            surface,
            xFrame,
            self.yFrame,
            x, y,
            scale,
            rot,
            refPoint
        )
        return

    def reset(self):
        self.frame = 0

    def setFrame(self, frame):
        self.frame = frame

    def getFrame(self):
        return self.frame




