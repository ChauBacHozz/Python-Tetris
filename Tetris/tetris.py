from ast import Global
from hashlib import new
from pdb import post_mortem
import pygame as pg
import random
pg.init()

#SCREEN INFO
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 740
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pg.image.load("tetris.png")
pg.display.set_icon(icon)
pg.display.set_caption("Tetris")

#COLOR DEFINES
WHITE = (255,255,255)
BLACK = (0,0,0)

COLORS = [(255,0,0),
(255,128,0),
(0,255,0),
(127, 0, 255),
(0,0,255),
(76,0,153),
(0,204,102)]

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

#NEXT TETROMINO SECTION
NEXTTET_WIDTH = CELL_SIZE * 3
NEXTTET_HEIGHT = CELL_SIZE * 4
NEXTTET_LEFT_GAP = 605
NEXTTET_UPPER_GAP = 400

# taken_cells = []
game_map = []
for i in range (0, CELLS_ON_ROW * CELLS_ON_COL):
    game_map.append(0)
clock = pg.time.Clock()
move_down = CELLS_ON_ROW

#DRAW SCORE SECTION
game_point = 0
font = pg.font.Font("freesansbold.ttf", 36)
textX = 525
textY = 100
def showScore(point):
    score = font.render("Score: " + "{:06d}".format(point), True, WHITE)
    screen.blit(score, (textX,textY))

#TETROMINO DEFINES
oTetromino = [
    [0, 1, CELLS_ON_ROW, 1 + CELLS_ON_ROW],
    [0, 1, CELLS_ON_ROW, 1 + CELLS_ON_ROW],
    [0, 1, CELLS_ON_ROW, 1 + CELLS_ON_ROW],
    [0, 1, CELLS_ON_ROW, 1 + CELLS_ON_ROW],
]
zTetromino = [
    [0, 1, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW],
    [2, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2],
    [0, 1, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW],
    [2, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2]
]
rv_zTetromino = [
    [1, 2, CELLS_ON_ROW, 1 + CELLS_ON_ROW],
    [0, CELLS_ON_ROW, 1 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2],
    [1, 2, CELLS_ON_ROW, 1 + CELLS_ON_ROW],
    [0, CELLS_ON_ROW, 1 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2]
] 
tTetromino = [
    [1, CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW],
    [1, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2],
    [CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2],
    [1, CELLS_ON_ROW, 1 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2]
]
iTetromino = [
    [1, CELLS_ON_ROW + 1, CELLS_ON_ROW*2 + 1, CELLS_ON_ROW*3 + 1],
    [CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, 3 + CELLS_ON_ROW],
    [1, CELLS_ON_ROW + 1, CELLS_ON_ROW*2 + 1, CELLS_ON_ROW*3 + 1],
    [CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, 3 + CELLS_ON_ROW]
]
lTetromino = [
    [0, 1, 1 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2],
    [2, CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW],
    [1, 1 + CELLS_ON_ROW, 1 + CELLS_ON_ROW*2, 2 + CELLS_ON_ROW*2],
    [CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, CELLS_ON_ROW*2]
]
rv_lTetromino = [
    [1, 2, CELLS_ON_ROW + 1, CELLS_ON_ROW*2 + 1],
    [CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW, 2 + CELLS_ON_ROW*2],
    [1, 1 + CELLS_ON_ROW, CELLS_ON_ROW*2, 1 + CELLS_ON_ROW*2],
    [0, CELLS_ON_ROW, 1 + CELLS_ON_ROW, 2 + CELLS_ON_ROW]
]
tetrominos = [
    oTetromino,
    zTetromino,
    rv_zTetromino,
    tTetromino,
    iTetromino,
    lTetromino,
    rv_lTetromino
]
rotation = 0
rand_num = random.randint(0, 6)
rand_num_next = random.randint(0, 6)
tetromino = tetrominos[rand_num]
color = COLORS[rand_num]
color_next = COLORS[rand_num_next]
#DRAW STUFFS ON SCREEN
def drawTetrisSurface():
    pg.draw.line(screen, WHITE, (500, 0), (500, SCREEN_HEIGHT), 2)
    pg.draw.rect(screen, WHITE, (LEFT_GAP, UPPER_GAP, GRID_WIDTH, GRID_HEIGHT))

def drawCell(pos, color):
    pg.draw.rect(screen, color, 
    (LEFT_GAP + ((pos + CELLS_ON_ROW) % CELLS_ON_ROW) * CELL_SIZE
    ,UPPER_GAP + (pos // CELLS_ON_ROW) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def drawTetromino(pos, color):
    for i in tetromino[rotation]:
        drawCell(pos + i, color)

def drawTakenTetrominos():
    for i in range (0, CELLS_ON_COL * CELLS_ON_ROW):
        if game_map[i] != 0:
            drawCell(i, game_map[i])

def drawNextTetSection():
    next = font.render("NEXT", True, WHITE)
    screen.blit(next, (NEXTTET_LEFT_GAP , NEXTTET_UPPER_GAP - 70))
    pg.draw.rect(screen, WHITE, (NEXTTET_LEFT_GAP - 10, NEXTTET_UPPER_GAP - 20, NEXTTET_WIDTH + 20, NEXTTET_HEIGHT + 40), 2)
    for i in tetrominos[rand_num_next][0]:
        pg.draw.rect(screen, color_next, 
        (NEXTTET_LEFT_GAP + ((i + CELLS_ON_ROW) % CELLS_ON_ROW) * CELL_SIZE
        ,NEXTTET_UPPER_GAP + (i // CELLS_ON_ROW) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

#CHECKING GAME EVENT
def checkTetLeft(tet):
    res = tet[0]
    for i in tet:
        if (i + CELLS_ON_ROW) % CELLS_ON_ROW < (res + CELLS_ON_ROW) % CELLS_ON_ROW:
            res = i
    return res
def checkTetRight(tet):
    res = tet[0]
    for i in tet:
        if (i + CELLS_ON_ROW) % CELLS_ON_ROW > (res + CELLS_ON_ROW) % CELLS_ON_ROW:
            res = i
    return res

def checkBottomCollision(pos):
    for i in tetromino[rotation]:
        if game_map[pos + i + CELLS_ON_ROW] != 0:
            return True
    return False 

def checkEdge(pos):
    if (pos + tetromino[rotation][3]) in range (252, 264) :
        return True
    if checkBottomCollision(pos):
        return True
    return False

def leftEdge(pos):
    for i in tetromino[rotation]:
        if (pos + i + CELLS_ON_ROW) % CELLS_ON_ROW == 0:
            return False
        if game_map[pos + i - 1] != 0:
            return False
    return True

def rightEdge(pos):
    for i in tetromino[rotation]:
        if (pos + i + CELLS_ON_ROW) % CELLS_ON_ROW == CELLS_ON_ROW - 1:
            return False
        if game_map[pos + i + 1] != 0:
            return False

    return True
def checkFullOneRow(pos):
    for i in range (pos, pos + 12):
        if game_map[i] == 0:
            return False
    return True

def checkFullAllRow(pos):
    global game_point
    first_row = (pos + tetromino[rotation][0]) // CELLS_ON_ROW
    second_row = (pos + tetromino[rotation][3]) // CELLS_ON_ROW
    col_take = []
    for i in range (first_row * CELLS_ON_ROW, second_row * CELLS_ON_ROW + CELLS_ON_ROW, CELLS_ON_ROW):
        if checkFullOneRow(i):
            col_take.append(i)
            for j in range (i, i + 12):
                game_map[j] = 0

    ct_length = len(col_take)
    if ct_length != 0:
        #GOT POINTS AFTER FULL ROW
        game_point = game_point + 10 * ct_length 
        head_pos = col_take[0]
        for i in reversed(range(0, head_pos)):
            if game_map[i] != 0:
                res = game_map[i]
                game_map[i] = 0
                game_map[i + ct_length * CELLS_ON_ROW] = res
def checkRot(pos):
    # new_rotation = (rotation + 1) % 4
    # first_cell = checkTetLeft(tetromino[new_rotation])
    # last_cell = checkTetRight(tetromino[new_rotation])
    # count = 0
    # res = 0
    # for i in tetromino[new_rotation]:
    #     # print(pos + i)
    #     if (pos + i) % CELLS_ON_ROW == 0 or (pos + i) % CELLS_ON_ROW == 11:
    #         print("check")
    #         # if (pos + first_cell) % CELLS_ON_ROW > 5:
    #         #     # pos -= 5
    #         #     res = CELLS_ON_ROW - ((pos - 5 + last_cell) % CELLS_ON_ROW)
    #         #     print(res)
                
    #         # else:
    #         #     # pos += 5
    #         #     res = ((pos + 5 + first_cell) % CELLS_ON_ROW) * (-1)
    #         #     # print(res)
    #         break
    # return res

    for i in tetromino[(rotation + 1) % 4]:
        if (pos + i + CELLS_ON_ROW) % CELLS_ON_ROW == 0:
            return False
    for i in tetromino[(rotation + 1) % 4]:
        if (pos + i + CELLS_ON_ROW) % CELLS_ON_ROW == 11:
            return False
        return True
def checkLose(pos):
    for i in range (0, 12):
        if game_map[i] != 0:
            return True
    return False


#GAME LOOP
screen_looping = True
game_pause = False
fall_speed = 0.27
fall_time = 0
while screen_looping:
    pg.display.flip()
    #check game events from keyboard and outter stuffs
    if pg.key.get_pressed()[pg.K_DOWN]:
        fall_speed = 0.05
    for event in pg.event.get():
        if event.type == pg.QUIT:
            screen_looping = False 
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                if leftEdge(drop_pos):
                    drop_pos -= 1
                    move_down = 0
            if event.key == pg.K_RIGHT:
                if rightEdge(drop_pos):
                    drop_pos += 1
                    move_down = 0
            if event.key == pg.K_SPACE:
                if checkEdge(drop_pos) == False:
                    if checkRot(drop_pos):
                        rotation = (rotation + 1) % 4
            if event.key == pg.K_UP:
                game_pause = abs(game_pause - 1)
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                move_down = CELLS_ON_ROW
            if event.key == pg.K_RIGHT:
                move_down = CELLS_ON_ROW
            if event.key == pg.K_DOWN:
                fall_speed = 0.27
    screen.fill(BLACK)
    drawTetrisSurface()
    drawTakenTetrominos()
    drawNextTetSection()
    # if game_pause == False:
    drawTetromino(drop_pos, color)

    if checkLose(drop_pos):
        game_pause = True
        
    fall_time += clock.get_rawtime()
    clock.tick()
    if fall_time/1000 >= fall_speed:
        fall_time = 0
        if checkEdge(drop_pos) == False:
            drop_pos += move_down
        else: 
            for i in tetromino[rotation]:
                game_map[drop_pos + i] = color
            checkFullAllRow(drop_pos)
            rand_num = rand_num_next
            tetromino = tetrominos[rand_num]
            color = color_next
            drop_pos = 5
            rotation = 0
            rand_num_next = random.randint(0, 6)
            color_next = COLORS[rand_num_next]
    if game_pause == True:
        clock.tick(0)
    showScore(game_point)
