import GameProperties as GameProps
import TetrominosCollection
def drawLevel(lev):
    global level
    levelText = GameProps.levelFont.render("LV:" + "{:03d}".format(lev), True, (248,255,13))
    GameProps.screen.blit(levelText, (GameProps.levelX,GameProps.levelY))
    GameProps.pg.draw.rect(GameProps.screen, GameProps.WHITE, (520, 460, 260, 80), 2)
    GameProps.screen.blit(GameProps.evaImg, (522, 462))
    GameProps.screen.blit(GameProps.resetImg, (720, 640))
    GameProps.screen.blit(GameProps.exitImg, (520, 560))

def drawTetrisSurface():
    GameProps.pg.draw.line(GameProps.screen, GameProps.WHITE, (500, 0), (500, GameProps.SCREEN_HEIGHT), 2)
    GameProps.pg.draw.rect(GameProps.screen, (249, 44, 228), (GameProps.LEFT_GAP-4, GameProps.UPPER_GAP-4, GameProps.GRID_WIDTH + 8, GameProps.GRID_HEIGHT + 8), 4)
    GameProps.pg.draw.rect(GameProps.screen, (40,33,33), (GameProps.LEFT_GAP, GameProps.UPPER_GAP, GameProps.GRID_WIDTH, GameProps.GRID_HEIGHT))

def drawCell(pos, color):
    GameProps.pg.draw.rect(GameProps.screen, color, 
    (GameProps.LEFT_GAP + ((pos + GameProps.CELLS_ON_ROW) % GameProps.CELLS_ON_ROW) * GameProps.CELL_SIZE
    ,GameProps.UPPER_GAP + (pos // GameProps.CELLS_ON_ROW) * GameProps.CELL_SIZE, GameProps.CELL_SIZE, GameProps.CELL_SIZE))

def drawTetromino(pos, color):
    for i in GameProps.tetromino[GameProps.rotation]:
        drawCell(pos + i, color)

def drawTakenTetrominos():
    for i in range (0, GameProps.CELLS_ON_COL * GameProps.CELLS_ON_ROW):
        if GameProps.game_map[i] != 0:
            drawCell(i, GameProps.game_map[i])

def showScore(point):
    GameProps.pg.draw.rect(GameProps.screen, (0,255,0), (GameProps.textX, GameProps.textY, 260, 160), 4)
    scoreText = GameProps.nextTetFont.render("SCORE----", True, (0,255,0))
    GameProps.screen.blit(scoreText, (GameProps.textX + 18,GameProps.textY + 16))
    scoreValue = GameProps.nextTetFont.render("----" + "{:05d}".format(point), True, (0,255,0))
    GameProps.screen.blit(scoreValue, (GameProps.textX,GameProps.textY + 100))

def drawNextTetSection():
    next = GameProps.nextTetFont.render("NEXT", True, (71,244,255))
    GameProps.screen.blit(next, (GameProps.NEXTTET_LEFT_GAP - 5, GameProps.NEXTTET_UPPER_GAP - 70))
    GameProps.pg.draw.rect(GameProps.screen, (71,244,255), (GameProps.NEXTTET_LEFT_GAP - 10, GameProps.NEXTTET_UPPER_GAP - 20, GameProps.NEXTTET_WIDTH + 20, GameProps.NEXTTET_HEIGHT + 40), 2)
    for i in TetrominosCollection.tetrominos[GameProps.rand_num_next][0]:
        GameProps.pg.draw.rect(GameProps.screen, GameProps.color_next, 
        (GameProps.NEXTTET_LEFT_GAP + ((i + GameProps.CELLS_ON_ROW) % GameProps.CELLS_ON_ROW) * GameProps.CELL_SIZE
        ,GameProps.NEXTTET_UPPER_GAP + (i // GameProps.CELLS_ON_ROW) * GameProps.CELL_SIZE, GameProps.CELL_SIZE, GameProps.CELL_SIZE))

def showStartMenu():
    headingText = GameProps.startHeadingFont.render("TETRIS", True, (255,255,255))
    GameProps.screen.blit(headingText, (GameProps.SCREEN_WIDTH/2 - headingText.get_rect().width/2, 80))


