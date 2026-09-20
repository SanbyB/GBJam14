import pygame

class Controller():
    def __init__(self, tet):
        self.tet = tet
        self.initState()

    def initState(self):
        self.selected = 0
        self.state = "selecting"
        self.keysPressed = {"a":False, "w":False,
                            "s":False, "d":False,
                            "p":False, "l":False}
        self.spawnNew = False

    def update(self, events):
        self.keysPressed["a"] = False
        self.keysPressed["w"] = False
        self.keysPressed["s"] = False
        self.keysPressed["d"] = False
        self.keysPressed["p"] = False
        self.keysPressed["l"] = False

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.keysPressed["a"] = True
                if event.key == pygame.K_w:
                    self.keysPressed["w"] = True
                if event.key == pygame.K_s:
                    self.keysPressed["s"] = True
                if event.key == pygame.K_d:
                    self.keysPressed["d"] = True
                if event.key == pygame.K_p:
                    self.keysPressed["p"] = True
                if event.key == pygame.K_l:
                    self.keysPressed["l"] = True

        if self.state == "selecting":
            if self.tet.selected == None:
                self.selected = 0
            if self.keysPressed["a"] or self.keysPressed["s"]:
                self.tet.selected.setFrame(self.tet.selected.colour)
                if self.selected > 0:
                    self.selected -= 1
                else:
                    self.selected = len(self.tet.select) - 1
            if self.keysPressed["d"] or self.keysPressed["w"]:
                self.tet.selected.setFrame(self.tet.selected.colour)
                if self.selected < len(self.tet.select) - 1:
                    self.selected += 1
                else:
                    self.selected = 0

            self.tet.selected = self.tet.select[self.selected]

            if self.keysPressed["l"]:
                self.state = "moving"

        elif self.state == "moving":
            if self.keysPressed["a"]:
                self.tet.move("left")
            elif self.keysPressed["w"]:
                self.tet.move("up")
            elif self.keysPressed["s"]:
                self.tet.move("down")
            elif self.keysPressed["d"]:
                self.tet.move("right")
            elif self.keysPressed["p"]:
                self.tet.rotate()

            if self.keysPressed["l"]:
                self.selected = 0
                if not self.tet.place():
                    self.tet.selected.gridX = -1
                    self.tet.selected.gridY = -1
                else:
                    self.spawnNew = True
                self.state = "selecting"
