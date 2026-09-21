import sys
import pygame
import os.path
from pygame.locals import *
from conf import *
from world import World
from graphics.resources import *

pygame.init()

pygame.display.set_caption('Tetrinvaders')
pygame.display.set_icon(pygame.image.load(resource_path("Graphics", "spaceshipIcon.png")))

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.world = World(self.screen)
        self.keysPressed = pygame.key.get_pressed()
        self.started = False
        self.paused = False
        self.musicPaused = False

    def setMusicPaused(self, paused):
        if paused != self.musicPaused:
            if paused:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
            self.musicPaused = paused

    def update(self, events):
        pygame.draw.rect(self.screen, (0, 0, 0, 255), Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)) # type: ignore
        self.world.render()

        self.keysPressed = pygame.key.get_pressed()

        if self.keysPressed[K_LCTRL] and self.keysPressed[K_w]:
            pygame.quit()
            sys.exit()
        
        if self.started:
            if self.world.player.lives <= 0:
                self.gameOver()
            else:
                if self.keysPressed[K_ESCAPE]:
                    self.paused = True

                if self.paused:
                    self.setMusicPaused(True)
                    PAUSE.draw(
                        surface=self.screen,
                        x=SCREEN_WIDTH/2,
                        y=SCREEN_HEIGHT/2,
                        scale=SCALE
                    )
                    for event in events:
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_ESCAPE:
                                paused = True
                                while paused:
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYUP:
                                            if event.key == pygame.K_ESCAPE:
                                                paused = False
                                                self.paused = False
                                        elif event.type == QUIT:
                                            pygame.quit()
                                            sys.exit()

                else:
                    self.setMusicPaused(False) 
                    # self.world.player.keysPressed = self.keysPressed
                    self.world.update(events)
        else:
            self.setMusicPaused(True)
            self.start()


    def gameOver(self):
        self.setMusicPaused(True)
        GAMEOVER.draw(
            surface=self.screen,
            x=SCREEN_WIDTH/2,
            y=SCREEN_HEIGHT/2,
            scale=SCALE
        )
        GAMEOVER.update()
        GAMEOVER_CONT.draw(
            surface=self.screen,
            x=SCREEN_WIDTH/2,
            y=SCREEN_HEIGHT/2,
            scale=SCALE
        )
        GAMEOVER_CONT.update()
        if self.keysPressed[pygame.K_RETURN]:
                self.restart()

    def restart(self):
        restart = True
        while restart:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        self.keysPressed = pygame.key.get_pressed()
                        self.world.reset()
                        self.world.player.lives = 3
                        self.started = False
                        restart = False
                        self.start()

    def start(self):
        START.draw(
            surface=self.screen,
            x=SCREEN_WIDTH/2,
            y=SCREEN_HEIGHT/2,
            scale=SCALE
        )
        PRESS_START.draw(
            surface=self.screen,
            x=SCREEN_WIDTH/2,
            y=SCREEN_HEIGHT/2,
            scale=SCALE
        )
        START.update()
        PRESS_START.update()

        if self.keysPressed[pygame.K_RETURN]:
            self.started = True


RUNNING = True
game = Game()
clock = pygame.time.Clock()

# pygame.mixer.init()

pygame.mixer.music.load(resource_path("Audio", "bgMusic.wav")) 
pygame.mixer.music.set_volume(BACKGROUND_VOLUME)     
pygame.mixer.music.play(-1,0.0)

# pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=8192)


while RUNNING:
    dt = clock.tick(60)
    events = pygame.event.get()
    for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    game.update(events)
    
    
    pygame.display.update()
