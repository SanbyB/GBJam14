import pygame
import os.path
from graphics.animation import Animation
from graphics.spritesheet import SpriteSheet
from conf import resource_path



GAMEOVER = SpriteSheet(pygame.image.load(resource_path("Graphics", "gameover.png")), 2, 1)
GAMEOVER = Animation(GAMEOVER, 0, 0.1)

GAMEOVER_CONT = SpriteSheet(pygame.image.load(resource_path("Graphics", "gameoverCont.png")), 2, 1)
GAMEOVER_CONT = Animation(GAMEOVER_CONT, 0, 0.05)

PRESS_START = SpriteSheet(pygame.image.load(resource_path("Graphics", "pressStart.png")), 3, 1)
PRESS_START = Animation(PRESS_START, 0, 0.05)

PAUSE = SpriteSheet(pygame.image.load(resource_path("Graphics", "pause.png")), 1, 1)
PAUSE = Animation(PAUSE, 0, 0)

START = SpriteSheet(pygame.image.load(resource_path("Graphics", "startScreen.png")), 2, 1)
START = Animation(START, 0, 0.1)

HEART = SpriteSheet(pygame.image.load(resource_path("Graphics", "heart.png")), 1, 1)
HEART = Animation(HEART, 0, 0)

GRID = SpriteSheet(pygame.image.load(resource_path("Graphics", "grid.png")), 1, 1)
GRID = Animation(GRID, 0, 0)


class BulletSprite():
    sprite = SpriteSheet(pygame.image.load(resource_path("Graphics", "bullet.png")), 1, 1)
    BULLET = Animation(sprite, 0, 0)
    w, h = sprite.imageWidth, sprite.imageHeight

class PlayerSprite():
    sprite = SpriteSheet(pygame.image.load(resource_path("Graphics", "spaceship.png")), 4, 2)
    PLAYER_IDLE = Animation(sprite, 0, 0.1)
    PLAYER_SHOOT = Animation(sprite, 1, 0.1)
    width = sprite.imageWidth
    height = sprite.imageHeight

class EnemySprite():
    sprite1 = SpriteSheet(pygame.image.load(resource_path("Graphics", "enemy1.png")), 3, 1)
    ENEMY1 = Animation(sprite1, 0, 0)
    w1, h1 = sprite1.imageWidth, sprite1.imageHeight

    sprite2 = SpriteSheet(pygame.image.load(resource_path("Graphics", "enemy2.png")), 3, 1)
    ENEMY2 = Animation(sprite2, 0, 0)
    w2, h2 = sprite2.imageWidth, sprite2.imageHeight

    sprite3 = SpriteSheet(pygame.image.load(resource_path("Graphics", "enemy3.png")), 3, 1)
    ENEMY3 = Animation(sprite3, 0, 0)
    w3, h3 = sprite3.imageWidth, sprite3.imageHeight

    sprite4 = SpriteSheet(pygame.image.load(resource_path("Graphics", "enemy4.png")), 3, 1)
    ENEMY4 = Animation(sprite4, 0, 0)
    w4, h4 = sprite4.imageWidth, sprite4.imageHeight

    sprite5 = SpriteSheet(pygame.image.load(resource_path("Graphics", "enemy5.png")), 3, 1)
    ENEMY5 = Animation(sprite5, 0, 0)
    w5, h5 = sprite5.imageWidth, sprite5.imageHeight

class Tetrominos():
    class singleTile():
        sprite = SpriteSheet(pygame.image.load(resource_path("Graphics", "singlePiece.png")), 6, 1)
        w, h = sprite.imageWidth, sprite.imageHeight

    class T():
        sprite = SpriteSheet(pygame.image.load(resource_path("Graphics", "tPiece.png")), 6, 1)
        w, h = sprite.imageWidth, sprite.imageHeight

    class Lleft():
        sprite = SpriteSheet(pygame.image.load(resource_path("Graphics", "lPiece.png")), 6, 1)
        w, h = sprite.imageWidth, sprite.imageHeight

    class Lright():
        sprite = SpriteSheet(pygame.image.load(resource_path("Graphics", "lPiece.png")), 6, 1)
        sprite.flip = True
        w, h = sprite.imageWidth, sprite.imageHeight

    class S():
        sprite = SpriteSheet(pygame.image.load(resource_path("Graphics", "sPiece.png")), 6, 1)
        w, h = sprite.imageWidth, sprite.imageHeight

    class Z():
        sprite = SpriteSheet(pygame.image.load(resource_path("Graphics", "sPiece.png")), 6, 1)
        sprite.flip = True
        w, h = sprite.imageWidth, sprite.imageHeight

    class Stick():
        sprite = SpriteSheet(pygame.image.load(resource_path("Graphics", "stickPiece.png")), 6, 1)
        w, h = sprite.imageWidth, sprite.imageHeight

    class Square():
        sprite = SpriteSheet(pygame.image.load(resource_path("Graphics", "sqrPiece.png")), 6, 1)
        w, h = sprite.imageWidth, sprite.imageHeight


    


        
