from pygame import font
W_WIDTH, W_HEIGHT = 400, 600
TITLE = 'Mehdi\'s Game'
VEL_ADD = 6
IMAGE_PLAYER = 'images/player2.png'
IMAGE_BACKGROUND = 'images/background22.jpg'
IMAGE_BULLET = 'images/bullet2.png'
IMAGE_ENEMY = 'images/enemy1.png'
ENEMY_COUNT = 7

font.init()
SMALLER_FONT = font.SysFont('Sans', 10)
SMALL_FONT = font.SysFont('Sans', 16)
LARGE_FONT = font.SysFont('Sans', 22)

RED = (201,18,18)
YELLOW = (214,211,0)
GREEN = (3,150,23)
WHITE = (255,255,255)
GRAY = (140,140,140)