import pygame
import random
from entites.player import Player
from entites.enemy import Enemy
from entites.bullet import Bullet
from tetris import *
from controller import Controller
from conf import *
from graphics.resources import *
from audioResources import *

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)

class World():
    def __init__(self, screen):
        self.screen = screen
        self.player = Player((SCREEN_WIDTH/2, 0))
        self.enemies = []
        self.bullets = []
        self.enemyBullets = []
        self.bulletTimer = ENEMY_BULLET_DELAY

        self.grid = Grid()
        self.tet = Tetris(self.grid)
        self.control = Controller(self.tet)

        self.reset()

        self.shotEnemy = False
        self.shotPlayer = False
        self.lineCleared = False
        self.rowCleared = False

    def initPieces(self):
        for i in range(NUM_TETROMINOS):
            self.spawnPiece()

    def spawnPiece(self):
        piecesInTet = []
        for tet in self.tet.select:
            if isinstance(tet, T):
                piecesInTet.append(0)
            elif isinstance(tet, S):
                piecesInTet.append(1)
            elif isinstance(tet, Z):
                piecesInTet.append(2)
            elif isinstance(tet, Lright):
                piecesInTet.append(3)
            elif isinstance(tet, Lleft):
                piecesInTet.append(4)
            elif isinstance(tet, stick):
                piecesInTet.append(5)
            elif isinstance(tet, sqr):
                piecesInTet.append(6)

        piecesToChoose = list(set([0,1,2,3,4,5,6]) - set(piecesInTet))

        piece = None
        rand = random.randint(0, len(piecesToChoose) - 1)
        rand = piecesToChoose[rand]
        colour = random.randint(1, 5)
        if rand == 0:
            piece = T(colour)
        elif rand == 1:
            piece = S(colour)
        elif rand == 2:
            piece = Z(colour)
        elif rand == 3:
            piece = Lright(colour)
        elif rand == 4:
            piece = Lleft(colour)
        elif rand == 5:
            piece = stick(colour)
        elif rand == 6:
            piece = sqr(colour)

        self.tet.spawn(piece)

    def update(self, events):
        self.shotEnemy = False
        self.shotPlayer = False
        self.lineCleared = False
        self.rowCleared = False


        rowsCols = self.grid.checkRowCol()
        if len(rowsCols[0]) != 0 or len(rowsCols[1]) != 0:
            self.lineCleared = True
            self.score += 10 * (len(rowsCols[0]) + len(rowsCols[1]))
            self.player.doubleShoot = DOUBLE_SHOOT_TIME
        self.grid.clearRowCol(rowsCols)
        self.control.update(events)
        if self.control.spawnNew:
            self.spawnPiece()
            self.control.spawnNew = False
        self.tet.update()

        self.player.movePlayer(self.tet.lastColourPlaced)
        
        self.player.update()
        if self.player.spawnBullet:
            self.bullets.append(Bullet((self.player.x, self.player.y)))

        for b in self.bullets[:]:
            b.update()
            if b.y < 0:
                self.bullets.remove(b)
            for e in self.enemies:
                if b.detectCollision(e):
                    self.shotEnemy = True
                    self.score += 1
                    if e in self.enemies:
                        self.enemies.remove(e)
                    if b in self.bullets:
                        self.bullets.remove(b)
                    break

        if self.enemies == []:
            self.rowCleared = True
            if self.player.lives < 3:
                self.player.lives += 1
            self.score += 50
            self.clearEnemies()

        for b in self.enemyBullets[:]:
            b.update()
            if b.y > SCREEN_HEIGHT:
                self.enemyBullets.remove(b)
            if b.detectCollision(self.player):
                self.shotPlayer = True
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
        rand = random.randint(0, self.bulletTimer)
        if rand < ENEMY_BULLET_CHANCE:
            b = Bullet((random.randint(int(minX/SCALE), int(maxX/SCALE))*SCALE, minY))
            b.playerBullet = False
            self.enemyBullets.append(b)
            self.bulletTimer = ENEMY_BULLET_DELAY

        self.playSounds()

    def playSounds(self):
        if self.rowCleared:
            clearedRow.play()
        elif self.lineCleared:
            clearedLine.play()
        elif self.shotPlayer:
            playerShot.play()
        elif self.shotEnemy:
            enemyShot.play() 


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

        GRID.draw(self.screen, GRID_X, GRID_Y, refPoint="topLeft")
        self.grid.render(self.screen)
        self.tet.render(self.screen)

        text = font.render(str(self.score), True, ((255,255,255)), (0,0,0))
        textRect = text.get_rect()
        textRect.topleft = (SCORE_X, SCORE_Y)
        self.screen.blit(text, textRect)

    def clearEnemies(self):
        self.enemies = []
        for i in range(ENEMIES_X):
            for j in range(ENEMIES_Y):
                e = Enemy((0,0), min(5, j+1))
                x = i * (EnemySprite.w1 * SCALE + BORDER) + EnemySprite.w1 * SCALE
                y = j * (e.height + BORDER) + e.height
                e.x = x
                e.y = y
                self.enemies.append(e)
        

    def reset(self):
        self.grid.resetGrid()
        self.clearEnemies()
        self.tet.select = []
        self.control.initState()
        self.initPieces()
        self.score = 0
        self.player.vx = 0
        self.bullets = []
        self.tet.lastColourPlaced = 0