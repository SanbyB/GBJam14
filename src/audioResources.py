import pygame
import os.path
from conf import resource_path

pygame.mixer.init(44100, -16, 2, 4096)

enemyShot = pygame.mixer.Sound(resource_path("Audio", "enemyShot.mp3"))
playerShot = pygame.mixer.Sound(resource_path("Audio", "playerShot.mp3"))
clearedRow = pygame.mixer.Sound(resource_path("Audio", "clearedRow.mp3"))
clearedLine = pygame.mixer.Sound(resource_path("Audio", "clearedLine.mp3"))
