import pygame as pg
import random
import TetrominosCollection as TetCollection
pg.init()

#SCREEN INFO
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 740
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pg.image.load("./asset/tetris.png")
pg.display.set_icon(icon)
pg.display.set_caption("Tetris")

#COLOR DEFINES
WHITE = (255,255,255)
BLACK = (0,0,0)

COLORS = [(0, 255, 255),
(255, 255, 0),
(128, 0, 128),
(0, 255, 0),
(255, 0, 0),
(0, 0, 255),
(255, 127, 0)]

#GAME PROPERTIES
CELL_SIZE = 30
GRID_WIDTH = 360
GRID_HEIGHT = 660
CELLS_ON_ROW = GRID_WIDTH // CELL_SIZE
CELLS_ON_COL = GRID_HEIGHT // CELL_SIZE
LEFT_GAP = 70
UPPER_GAP = 40
drop_pos = 5
mlsec = 0
level = 1
nextTetFont = pg.font.Font("./asset/VCR_OSD_MONO_1.001.ttf", 46)
levelFont = pg.font.Font("./asset/VCR_OSD_MONO_1.001.ttf", 34)
textX = 520
textY = 40
evaImg = pg.image.load("./asset/lenin.jpg")
evaImg = pg.transform.scale(evaImg, (256, 76))
resetImg = pg.image.load("./asset/sinchronize-64.png")
exitImg = pg.image.load("./asset/exit-64.png")
exitImg = pg.transform.scale(exitImg, (54, 54))
#NEXT TETROMINO SECTION
NEXTTET_WIDTH = CELL_SIZE * 3
NEXTTET_HEIGHT = CELL_SIZE * 4
NEXTTET_LEFT_GAP = 530
NEXTTET_UPPER_GAP = 300


game_map = []
for i in range (0, CELLS_ON_ROW * CELLS_ON_COL):
    game_map.append(0)
clock = pg.time.Clock()
move_down = CELLS_ON_ROW

screen_looping = True
game_pause = False
game_point = 0

rotation = 0
rand_num = random.randint(0, 6)
rand_num_next = random.randint(0, 6)
tetromino = TetCollection.tetrominos[rand_num]
color = COLORS[rand_num]
color_next = COLORS[rand_num_next]

levelX = 660
levelY = NEXTTET_UPPER_GAP + 105

game_states = ["start_menu", "game_play", "end"]
state = game_states[0]

startHeadingFont = pg.font.Font("./asset/VCR_OSD_MONO_1.001.ttf", 120)
startMenuFont = pg.font.Font("./asset/VCR_OSD_MONO_1.001.ttf", 80)
scoreLoseFont = pg.font.Font("./asset/times new roman bold.ttf", 72)
buttonLoseFont = pg.font.Font("./asset/times new roman bold.ttf", 60)
