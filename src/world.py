import pygame
import random
from entites.player import Player
from entites.enemy import Enemy
from entites.bullet import Bullet
from conf import *
from graphics.resources import *

class World():
    def __init__(self, screen):
        self.screen = screen
        self.player = Player((SCREEN_WIDTH/2, 0))
        self.enemies = []
        self.bullets = []
        self.enemyBullets = []
        self.reset()
        self.bulletTimer = ENEMY_BULLET_DELAY

    def update(self):
        
        self.player.update()
        if self.player.spawnBullet:
            self.bullets.append(Bullet((self.player.x, self.player.y)))

        for b in self.bullets:
            b.update()
            if b.y < 0:
                self.bullets.remove(b)
            for e in self.enemies:
                if b.detectCollision(e):
                    if e in self.enemies:
                        self.enemies.remove(e)
                    if b in self.bullets:
                        self.bullets.remove(b)
                    continue

        if self.enemies == []:
            self.reset()

        for b in self.enemyBullets:
            b.update()
            if b.y > SCREEN_HEIGHT:
                self.enemyBullets.remove(b)
            if b.detectCollision(self.player):
                self.player.lives -= 1
                if b in self.enemyBullets:
                    self.enemyBullets.remove(b)

        enemiesDown = False
        minY = SCREEN_HEIGHT
        minX = SCREEN_WIDTH
        maxX = 0
        for e in self.enemies:
            e.update()
            if e.moveCounter <= 0:
                e.animation.setFrame(random.randint(0, 2))
            if e.y > ENEMY_BORDER:
                self.player.lives = 0
            minY = min(minY, e.y)
            minX = min(minX, e.x)
            maxX = max(maxX, e.x)
            if e.down:
                enemiesDown = True
        if enemiesDown:
            for e in self.enemies:

                e.move()
                e.shiftDown()

        self.bulletTimer -= 1
        if self.bulletTimer <= 0:
            self.bulletTimer = ENEMY_BULLET_DELAY
        if random.randint(0, self.bulletTimer) < ENEMY_BULLET_CHANCE:
            b = Bullet((random.randint(int(minX/SCALE), int(maxX/SCALE))*SCALE, minY))
            b.playerBullet = False
            self.enemyBullets.append(b)
            self.bulletTimer = ENEMY_BULLET_DELAY


    def render(self):
        self.player.render(self.screen)
        for e in self.enemies:
            e.render(self.screen)
        for b in self.bullets + self.enemyBullets:
            b.render(self.screen)

        for heart in range(self.player.lives):
            x = SCREEN_WIDTH - ((HEART.spritesheet.imageWidth + BORDER) * (heart + 0.5) * SCALE)
            HEART.draw(self.screen, x, (HEART.spritesheet.imageHeight/2 + BORDER) * SCALE)

        pygame.draw.rect(self.screen, 'white', (RIGHT_BORDER, 0, SCALE, SCREEN_HEIGHT))

        GRID.draw(self.screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    def reset(self):
        self.enemies = []
        for i in range(ENEMIES_X):
            for j in range(ENEMIES_Y):
                e = Enemy((0,0), min(5, j+1))
                x = i * (EnemySprite.w1 * SCALE + BORDER) + EnemySprite.w1 * SCALE
                y = j * (e.height + BORDER) + e.height
                e.x = x
                e.y = y
                self.enemies.append(e)
