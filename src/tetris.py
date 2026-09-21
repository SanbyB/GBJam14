from graphics.resources import Tetrominos
from graphics.animation import Animation
from conf import *

class Tetrominoes():
    def __init__(self, colour = 3):
        self.animation = None
        self.defaultY, self.defaultY = 0, 0
        self.x, self.y = 0, 0
        self.rotate = 0
        self.colour = colour
        self.states = {}
        self.gridX, self.gridY = -1, -1

    def init(self):
        self.animation.setFrame(self.colour)

    def getFrame(self):
        return self.animation.getFrame()

    def setFrame(self, frame):
        self.animation.setFrame(frame)



class singleTile(Tetrominoes):
    def __init__(self, colour):
        super().__init__(colour)
        self.animation = Animation(Tetrominos.singleTile.sprite, 0, 0)


class T(Tetrominoes):
    def __init__(self, colour):
        super().__init__(colour)
        Tup = [[0, 1, 0],
                [1, 1, 1]]
        
        Tright = [[1, 0],
                    [1, 1],
                    [1, 0]]
        
        Tdown = [[1, 1, 1],
                    [0, 1, 0]]

        Tleft = [[0, 1],
                    [1, 1],
                    [0, 1]]


        self.animation = Animation(Tetrominos.T.sprite, 0, 0)
        self.x, self.y = T_X, T_Y
        self.defaultX, self.defaultY = T_X, T_Y
        self.rotate = 90
        self.states = {0: Tup, 90: Tright, 180: Tdown, 270: Tleft}
        super().init()


class Lleft(Tetrominoes):
    def __init__(self, colour):
        super().__init__(colour)
        self.animation = Animation(Tetrominos.Lleft.sprite, 0, 0)
        self.x, self.y = L_X, L_Y
        self.defaultX, self.defaultY = L_X, L_Y

        Lup = [[1, 0],
            [1, 0],
            [1, 1]]
        
        Lright = [[1, 1, 1],
                [1, 0, 0]]
        
        Ldown = [[1, 1],
                [0, 1],
                [0, 1]]
        
        Lleft = [[0, 0, 1],
                [1, 1, 1]]

        self.states = {0: Lup, 90: Lright, 180: Ldown, 270: Lleft}
        super().init()



class Lright(Tetrominoes):
    def __init__(self, colour):
        super().__init__(colour)
        self.animation = Animation(Tetrominos.Lright.sprite, 0, 0)
        self.defaultX, self.defaultY = R_X, R_Y
        self.x, self.y = R_X, R_Y

        Lup = [[0, 1],
            [0, 1],
            [1, 1]]

        Lright = [[1, 0, 0],
                [1, 1, 1]]

        Ldown = [[1, 1],
                [1, 0],
                [1, 0]]

        Lleft = [[1, 1, 1],
                [0, 0, 1]]

        self.states = {0: Lup, 90: Lright, 180: Ldown, 270: Lleft}
        super().init()



class sqr(Tetrominoes):
    def __init__(self, colour):
        super().__init__(colour)
        self.animation = Animation(Tetrominos.Square.sprite, 0, 0)
        self.x, self.y = SQR_X, SQR_Y
        self.defaultX, self.defaultY = SQR_X, SQR_Y

        sqr = [[1, 1],
            [1, 1]]

        self.states = {0: sqr, 90: sqr, 180: sqr, 270: sqr}
        super().init()



class stick(Tetrominoes):
    def __init__(self, colour):
        super().__init__(colour)
        self.animation = Animation(Tetrominos.Stick.sprite, 0, 0)
        self.x, self.y = STICK_X, STICK_Y
        self.rotate = 90
        self.defaultX, self.defaultY = STICK_X, STICK_Y

        stickup = [[1],
                [1],
                [1],
                [1]]

        stickright = [[1, 1, 1, 1]]

        self.states = {0: stickright, 90: stickup, 180: stickright, 270: stickup}
        super().init()


class S(Tetrominoes):
    def __init__(self, colour):
        super().__init__(colour)
        self.animation = Animation(Tetrominos.S.sprite, 0, 0)
        self.x, self.y = S_X, S_Y
        self.rotate = 90
        self.defaultX, self.defaultY = S_X, S_Y

        Sup = [[0, 1, 1],
            [1, 1, 0]]

        Sright = [[1, 0],
                [1, 1],
                [0, 1]]

        self.states = {0: Sup, 90: Sright, 180: Sup, 270: Sright}
        super().init()


class Z(Tetrominoes):
    def __init__(self, colour):
        super().__init__(colour)
        self.animation = Animation(Tetrominos.Z.sprite, 0, 0)
        self.x, self.y = Z_X, Z_Y
        self.rotate = 90
        self.defaultX, self.defaultY = Z_X, Z_Y

        Zup = [[1, 1, 0],
            [0, 1, 1]]

        Zright = [[0, 1],
                [1, 1],
                [1, 0]]

        self.states = {0: Zup, 90: Zright, 180: Zup, 270: Zright}
        super().init()



class Tetris():
    def __init__(self, grid):
        self.select = []
        self.selected = None
        self.grid = grid
        self.cooldown = 0
        self.lastColourPlaced = 0 # adjusted so blue = -2, pink = 2


    def spawn(self, tetromino):
        self.select.append(tetromino)

    def update(self):
        self.cooldown -= 1
        if self.selected != None:
            if self.cooldown <= 0:
                if self.selected.getFrame() == 0:
                    self.selected.setFrame(self.selected.colour)
                else:
                    self.selected.setFrame(0)
        if self.cooldown <= 0:
            self.cooldown = SELECT_FLASH_SPEED


    def render(self, screen):
        for tet in self.select:
            self.setPosFromGrid()
            tet.animation.draw(screen, tet.x, tet.y, rot=tet.rotate, refPoint="topLeft")

    def place(self):
        if self.selected == None:
            return False

        if self.selected.gridX == -1 or self.selected.gridY == -1:
            return False

        x, y = self.selected.gridX, self.selected.gridY
        if self.grid.addTetromino(self.selected.states[self.selected.rotate], (x, y), self.selected.colour):
            if self.selected in self.select:
                self.select.remove(self.selected)
                self.lastColourPlaced = self.selected.colour - 3
            return True
        return False

    def move(self, direction):
        if self.selected == None:
            return
        if self.selected.gridX == -1 or self.selected.gridY == -1:
            self.selected.gridX = 0
            self.selected.gridY = 0
        elif direction == "down":
            if self.grid.checkTetrominoInGrid(self.selected.states[self.selected.rotate], 
                                              (self.selected.gridX, self.selected.gridY + 1)):
                self.selected.gridY += 1
            else:
                self.selected.gridX = -1
                self.selected.gridY = -1
        elif direction == "up":
            if self.grid.checkTetrominoInGrid(self.selected.states[self.selected.rotate], 
                                                (self.selected.gridX, self.selected.gridY - 1)):
                self.selected.gridY -= 1
            else:
                self.selected.gridX = -1
                self.selected.gridY = -1
        elif direction == "right":
            if self.grid.checkTetrominoInGrid(self.selected.states[self.selected.rotate], 
                                                (self.selected.gridX + 1, self.selected.gridY)):
                self.selected.gridX += 1
            else:
                self.selected.gridX = -1
                self.selected.gridY = -1
        elif direction == "left":
            if self.grid.checkTetrominoInGrid(self.selected.states[self.selected.rotate], 
                                                (self.selected.gridX - 1, self.selected.gridY)):
                self.selected.gridX -= 1
            else:
                self.selected.gridX = -1
                self.selected.gridY = -1

    def rotate(self):
        if self.selected == None:
            return
        self.selected.rotate += 90
        if self.selected.rotate >= 360:
            self.selected.rotate = 0      


    def setPosFromGrid(self):
        if self.selected == None:
            return None
        if self.selected.gridX == -1 or self.selected.gridY == -1:
            self.selected.x = self.selected.defaultX
            self.selected.y = self.selected.defaultY
        else:
            self.selected.x = GRID_X + (self.selected.gridX * (Tetrominos.singleTile.w - 1) + 1) * SCALE
            self.selected.y = GRID_Y + (self.selected.gridY * (Tetrominos.singleTile.h - 1) + 1) * SCALE


class Grid():
    def __init__(self):
        self.resetGrid()

    def sum(self):
        """
        used to calculate how pink/blue
        the grid is, which is used to determine
        the direction of movement of the player.
        blue has a value of 1 and pink has a value
        of 5
        """
        num = 0
        for i in range(GRID_COLS):
            for j in range(GRID_ROWS):
                if self.grid[i][j] != 0:
                    num += self.grid[i][j] - 3
        return num

    def checkRowCol(self):
        """
        returns list of rows and list of columns
        which have full lines
        """
        rows = []
        for i in range(GRID_COLS):
            row = True
            for j in range(GRID_ROWS):
                if self.grid[i][j] == 0:
                    row = False
            if row:
                rows.append(i)
        cols = []
        for j in range(GRID_ROWS):
            col = True
            for i in range(GRID_COLS):
                if self.grid[i][j] == 0:
                    col = False
            if col:
                cols.append(j)

        return rows, cols

    def clearRowCol(self, rowsCols):
        rows, cols = rowsCols
        for i in rows:
            for j in range(GRID_ROWS):
                self.grid[i][j] = 0
        for j in cols:
            for i in range(GRID_COLS):
                self.grid[i][j] = 0

    def resetGrid(self):
        self.grid = []
        for i in range(GRID_COLS):
            line = []
            for j in range(GRID_ROWS):
                line.append(0)
            self.grid.append(line)

    def addTetromino(self, tetromino, xy, colour):
        """
        checks space for tetromino at grid coord xy
        if there is space then the tetromino is placed
        there with colour being how blue/pink the tetromino
        is, blue = 1, pink = 5
        """
        if self.checkTetromino(tetromino, xy):
            x, y = xy
            for i in range(y, y + len(tetromino)):
                for j in range(x, x + len(tetromino[0])):
                    if tetromino[i - y][j - x] != 0:
                        self.grid[i][j] = colour
            return True
        else:
            return False


    def checkTetromino(self, tetromino, xy):
        if not self.checkTetrominoInGrid(tetromino, xy):
            return False
        return self.checkTetrominoOverlap(tetromino, xy)


    def checkTetrominoInGrid(self, tetromino, xy):
        x, y = xy
        if x + len(tetromino[0]) > GRID_ROWS:
            return False
        if y + len(tetromino) > GRID_COLS:
            return False
        return True


    def checkTetrominoOverlap(self, tetromino, xy):
        x, y = xy

        for i in range(y, y + len(tetromino)):
            for j in range(x, x + len(tetromino[0])):
                if tetromino[i - y][j - x] != 0 and self.grid[i][j] != 0:
                    return False
        return True

    def render(self, screen):
        for i in range(GRID_COLS):
            for j in range(GRID_ROWS):
                if self.grid[i][j] != 0:
                    x = GRID_X + (j * (Tetrominos.singleTile.w - 1) + 1) * SCALE
                    y = GRID_Y + (i * (Tetrominos.singleTile.h - 1) + 1) * SCALE
                    tile = singleTile(self.grid[i][j])
                    tile.animation.setFrame(self.grid[i][j])
                    tile.animation.draw(screen, x, y, refPoint="topLeft")

if __name__ == "__main__":

    grid = Grid()

    # grid.grid = [[1, 2, 3, 4, 5, 5],
    #              [0, 1, 1, 4, 5, 5],
    #              [1, 2, 3, 4, 5, 5],
    #              [0, 0, 1, 4, 5, 5],
    #              [1, 2, 3, 4, 0, 5],
    #              [0, 1, 1, 4, 5, 5],
    #              [1, 2, 3, 4, 5, 5],
    #              [0, 1, 1, 4, 5, 5],
    #              [1, 2, 3, 4, 5, 5],
    #              [0, 1, 1, 4, 5, 5]]

    grid.addTetromino(Tetrominoes.T.Tup, (0, 0), 4)
    grid.addTetromino(Tetrominoes.S.Sright, (3, 6), 1)
    grid.addTetromino(Tetrominoes.stick.stickright, (0, 0), 4)
    grid.addTetromino(Tetrominoes.sqr.sqr, (5, 7), 2)

    print(grid.checkRowCol())
    print(grid.sum())
    grid.clearRowCol(grid.checkRowCol())
    print(grid.grid)
    print(grid.sum())
