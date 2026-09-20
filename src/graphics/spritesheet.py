
import pygame
from math import floor
from conf import SCALE

class SpriteSheet:
    def __init__(self, image, xFrames, yFrames, flip=False):
        self.image = image
        self.xFrames = xFrames
        self.yFrames = yFrames
        self.imageWidth = self.image.get_width() / self.xFrames
        self.imageHeight = self.image.get_height() / self.yFrames
        self.flip = flip

    def draw(self, surface, xFrame, yFrame, x, y, scale=SCALE, rotate=0, refPoint="centre"):
        frame = pygame.Surface((self.imageWidth, self.imageHeight), pygame.SRCALPHA)
        frame.blit(self.image, (0, 0), (xFrame * self.imageWidth, yFrame * self.imageHeight, self.imageWidth, self.imageHeight))
        scaledImage = pygame.transform.scale(frame, (int(self.imageWidth) * scale, int(self.imageHeight) * scale))
        flippedImage = pygame.transform.flip(scaledImage, True, False) if self.flip else scaledImage
        rotatedImage = pygame.transform.rotate(flippedImage, -rotate)
        if refPoint == "centre":
            surface.blit(rotatedImage, (x - scale * self.imageWidth/2, y - scale * self.imageHeight/2))
        elif refPoint == "topLeft":
            surface.blit(rotatedImage, (x, y))
