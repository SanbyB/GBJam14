import pygame
import os.path

pygame.mixer.init(frequency=22050, size=-16, channels=6, buffer=8192)

enemyShot = pygame.mixer.Sound(os.path.join("Audio", "enemyShot.ogg"))
playerShot = pygame.mixer.Sound(os.path.join("Audio", "playerShot.ogg"))
clearedRow = pygame.mixer.Sound(os.path.join("Audio", "clearedRow.ogg"))
clearedLine = pygame.mixer.Sound(os.path.join("Audio", "clearedLine.ogg"))
