import sys
import pygame
from pygame.locals import *
from conf import *
from world import World
from graphics.resources import GAMEOVER, GAMEOVER_CONT, START, PRESS_START, PAUSE

pygame.display.set_caption('Tetrinvaders')

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.world = World(self.screen)
        self.keysPressed = pygame.key.get_pressed()
        self.started = False
        self.paused = False


    def update(self):
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
                    PAUSE.draw(
                        surface=self.screen,
                        x=SCREEN_WIDTH/2,
                        y=SCREEN_HEIGHT/2,
                        scale=SCALE
                    )
                    for event in pygame.event.get():
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
                    self.world.player.keysPressed = self.keysPressed
                    self.world.update()
        else:
            self.start()


    def gameOver(self):
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
        PRESS_START.update()
        if self.keysPressed[pygame.K_RETURN]:
            self.started = True


RUNNING = True
game = Game()
clock = pygame.time.Clock()

while RUNNING:
    dt = clock.tick(60)
    # Clear the screen
    game.update()
    for event in pygame.event.get():
        if event.type == QUIT: # type: ignore
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
