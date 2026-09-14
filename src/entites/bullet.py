from entity import Entity
from graphics.resources import BulletSprite
from conf import BULLET_SPEED, ENEMY_BULLET_SPEED

class Bullet(Entity):
    def __init__(self, pos):
        super().__init__(pos)
        self.animation = BulletSprite.BULLET
        self.width, self.height = BulletSprite.w, BulletSprite.h
        self.playerBullet = True

    def move(self):
        if self.playerBullet:
            self.y -= BULLET_SPEED
        else:
            self.y += ENEMY_BULLET_SPEED