

class Tetrominoes():
    class T():
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

    class Lleft():
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

    class Lright():
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

    class sqr():
        sqr = [[1, 1],
               [1, 1]]

    class stick():
        stickup = [[1],
                   [1],
                   [1],
                   [1]]

        stickright = [[1, 1, 1, 1]]

    class S():
        Sup = [[0, 1, 1],
               [1, 1, 0]]

        Sright = [[1, 0],
                  [1, 1],
                  [0, 1]]

    class Z():
        Zup = [[1, 1, 0],
               [0, 1, 1]]

        Zright = [[0, 1],
                  [1, 1],
                  [1, 0]]



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
        for i in range(10):
            for j in range(6):
                if self.grid[i][j] != 0:
                    num += self.grid[i][j] - 3
        return num

    def checkRowCol(self):
        """
        returns list of rows and list of columns
        which have full lines
        """
        rows = []
        for i in range(10):
            row = True
            for j in range(6):
                if self.grid[i][j] == 0:
                    row = False
            if row:
                rows.append(i)
        cols = []
        for j in range(6):
            col = True
            for i in range(10):
                if self.grid[i][j] == 0:
                    col = False
            if col:
                cols.append(j)

        return rows, cols

    def clearRowCol(self, rowsCols):
        rows, cols = rowsCols
        for i in rows:
            for j in range(6):
                self.grid[i][j] = 0
        for j in cols:
            for i in range(10):
                self.grid[i][j] = 0

    def resetGrid(self):
        self.grid = []
        for i in range(10):
            line = []
            for j in range(6):
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
                    self.grid[i][j] = colour * tetromino[i - y][j - x]

    def checkTetromino(self, tetromino, xy):
        x, y = xy

        if x + len(tetromino[0]) >= 6:
            print("x too big")
            return False
        if y + len(tetromino) >= 10:
            print("y too big")
            return False 

        for i in range(y, y + len(tetromino)):
            for j in range(x, x + len(tetromino[0])):
                if self.grid[i][j] != 0:
                    print("somthing placed there")
                    return False
        return True


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
