from conf import SCALE

class Entity():
    def __init__(self, pos):
        self.x, self.y = pos
        self.vx, self.vy = 0, 0
        
        self.animation = None
        self.width, self.height = (0, 0)
        self.scale = SCALE

    def update(self):
        self.move()
        if self.animation is not None:
            self.animation.update()

    def render(self, screen):            
            # Render the entity on the screen
            self.animation.draw(
                surface=screen,
                x=self.x,
                y=self.y,
                scale=self.scale
            )


    def detectCollision(self, other):
        if self.x + self.width/2 > other.x - other.width/2 and \
        self.x - self.width/2 < other.x + other.width/2 and \
        self.y + self.height/2 > other.y - other.height/2 and \
        self.y - self.height/2 < other.y + other.height/2:
            return True
        return False

    def move(self):
        self.x += self.vx
        self.y += self.vy
