# screen configs
SCALE = 3

SCREEN_WIDTH = 160 * SCALE
SCREEN_HEIGHT = 144 * SCALE

BORDER = SCALE
RIGHT_BORDER = SCREEN_WIDTH * 0.7

# grid configs
GRID_X, GRID_Y = RIGHT_BORDER + BORDER * 2, SCREEN_HEIGHT * 0.5
GRID_ROWS, GRID_COLS = 6, 8

TILE_SIZE = 8
TILE = TILE_SIZE * SCALE
TILE_Y = SCREEN_HEIGHT * 0.2

STICK_X, STICK_Y = 114 * SCALE, 19 * SCALE
T_X, T_Y = 123 * SCALE, 37 * SCALE
L_X, L_Y = 114 * SCALE, 49 * SCALE
R_X, R_Y = 142 * SCALE, 49 * SCALE
S_X, S_Y = 125 * SCALE, 21 * SCALE
Z_X, Z_Y = 132 * SCALE, 46 * SCALE
SQR_X, SQR_Y = 142 * SCALE, 28 * SCALE

# tetromino configs
SELECT_FLASH_SPEED = 10
NUM_TETROMINOS = 4

# player configs
PLAYER_SPEED = 0.25 * SCALE
PLAYER_BULLET_DELAY = 60
PLAYER_MOVE_LIMIT = 5

# enemy configs
MOVE_COUNTER = 25
ENEMIES_X = 7
ENEMIES_Y = 6
ENEMY_SPEED = SCALE
# number counts down each update to increase the chance of enemy producing bullet
ENEMY_BULLET_DELAY = 2500
# if a random number generated between 0 and the above number is less than this number an enemy will produce a bullet
ENEMY_BULLET_CHANCE = 2
ENEMY_BORDER = SCREEN_HEIGHT * 0.8

# bullet configs
BULLET_SPEED = 3 * SCALE
ENEMY_BULLET_SPEED = 0.2 * SCALE

# sound configs
BACKGROUND_VOLUME = 0.5