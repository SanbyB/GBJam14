from graphics.resources import EnemySprite
from graphics.animation import Animation
from entity import Entity
from conf import *

animation = {1:EnemySprite.sprite1,\
             2:EnemySprite.sprite2,\
             3:EnemySprite.sprite3,\
             4:EnemySprite.sprite4,\
             5:EnemySprite.sprite5}

width = {1:EnemySprite.w1,\
         2:EnemySprite.w2,\
         3:EnemySprite.w3,\
         4:EnemySprite.w4,\
         5:EnemySprite.w5}

height = {1:EnemySprite.h1,\
          2:EnemySprite.h2,\
          3:EnemySprite.h3,\
          4:EnemySprite.h4,\
          5:EnemySprite.h5}

class Enemy(Entity):
    def __init__(self, pos, type):
        super().__init__(pos)
        self.animation = Animation(animation[type], 0, 0)
        self.width, self.height = width[type] * SCALE, height[type] * SCALE
        self.goingRight = True
        self.down = False
        self.moveCounter = MOVE_COUNTER

    def shiftDown(self):
        self.goingRight = not self.goingRight
        self.y += self.height + BORDER
        self.down = False


    def move(self):
        if self.moveCounter <= 0:
            self.moveCounter = MOVE_COUNTER
        else:
            self.moveCounter -= 1
            return
        if self.goingRight:
            self.x += ENEMY_SPEED
            if self.x + self.width/2 + ENEMY_SPEED > RIGHT_BORDER:
                self.down = True

        else:
            self.x -= ENEMY_SPEED
            if self.x - self.width/2 - ENEMY_SPEED < BORDER:
                self.down = True        


    
