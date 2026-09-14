import pygame
from entity import Entity
from conf import *
from graphics.resources import PlayerSprite

class Player(Entity):
    def __init__(self, pos):
        super().__init__(pos)
        self.keysPressed = []
        self.animation = PlayerSprite.PLAYER_IDLE
        self.width, self.height = PlayerSprite.width * SCALE, PlayerSprite.height * SCALE

        self.y = SCREEN_HEIGHT - self.height/2 - BORDER
        self.spawnBullet = False
        self.bulletTimer = 0
        self.spaceDown = False
        self.lives = 3

    def update(self):
        super().update()
        if self.bulletTimer > 0:
            self.bulletTimer -= 1
        elif self.bulletTimer < 0:
            self.bulletTimer = 0

        self.vx = 0        
        self.keyInputs()
        if self.x < BORDER + self.width/2:
            self.vx = 0
            self.x = self.width/2 + BORDER
        if self.x > RIGHT_BORDER - self.width/2 - BORDER:
            self.vx = 0
            self.x = RIGHT_BORDER - self.width/2 - BORDER


    def keyInputs(self):
        
        if self.keysPressed[pygame.K_a]:
            self.vx = -PLAYER_SPEED

        if self.keysPressed[pygame.K_d]:
            self.vx = PLAYER_SPEED

        self.spawnBullet = False
        if self.keysPressed[pygame.K_SPACE]:
            if not self.spaceDown and self.bulletTimer == 0:
                self.spawnBullet = True
                self.bulletTimer = PLAYER_BULLET_DELAY
                self.spaceDown = True
        elif self.bulletTimer == 0:
            self.spaceDown = False



