# screen configs
SCALE = 3

SCREEN_WIDTH = 160 * SCALE
SCREEN_HEIGHT = 144 * SCALE

BORDER = SCALE
RIGHT_BORDER = SCREEN_WIDTH * 0.7

# player configs
PLAYER_SPEED = 2 * SCALE
PLAYER_BULLET_DELAY = 30

# enemy configs
MOVE_COUNTER = 20
ENEMIES_X = 7
ENEMIES_Y = 6
ENEMY_SPEED = SCALE
# number counts down each update to increase the chance of enemy producing bullet
ENEMY_BULLET_DELAY = 2000
# if a random number generated between 0 and the above number is less than this number an enemy will produce a bullet
ENEMY_BULLET_CHANCE = 10
ENEMY_BORDER = SCREEN_HEIGHT * 0.8

# bullet configs
BULLET_SPEED = 3 * SCALE
ENEMY_BULLET_SPEED = SCALE
