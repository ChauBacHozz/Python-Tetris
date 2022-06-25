import GameProperties 
def checkLevel(point):
    if point > 100:
        GameProperties.level = 5
        current_speed = 0.05
        return 
    if point >= 80:
        GameProperties.level = 4
        current_speed = 0.1
        return
    if point >= 40:
        GameProperties.level = 3
        current_speed = 0.17
        return
    if point >= 20:
        GameProperties.level = 2
        current_speed = 0.2
        return
def checkTetLeft(tet):
    res = tet[0]
    for i in tet:
        if (i + GameProperties.CELLS_ON_ROW) % GameProperties.CELLS_ON_ROW < (res + GameProperties.CELLS_ON_ROW) % GameProperties.CELLS_ON_ROW:
            res = i
    return res
def checkTetRight(tet):
    res = tet[0]
    for i in tet:
        if (i + GameProperties.CELLS_ON_ROW) % GameProperties.CELLS_ON_ROW > (res + GameProperties.CELLS_ON_ROW) % GameProperties.CELLS_ON_ROW:
            res = i
    return res

def checkBottomCollision(pos):
    for i in GameProperties.tetromino[GameProperties.rotation]:
        if GameProperties.game_map[pos + i + GameProperties.CELLS_ON_ROW] != 0:
            return True
    return False 

def checkEdge(pos):
    if (pos + GameProperties.tetromino[GameProperties.rotation][3]) in range (252, 264) :
        return True
    if checkBottomCollision(pos):
        return True
    return False

def leftEdge(pos):
    for i in GameProperties.tetromino[GameProperties.rotation]:
        if (pos + i + GameProperties.CELLS_ON_ROW) % GameProperties.CELLS_ON_ROW == 0:
            return False
        if GameProperties.game_map[pos + i - 1] != 0:
            return False
    return True

def rightEdge(pos):
    for i in GameProperties.tetromino[GameProperties.rotation]:
        if (pos + i + GameProperties.CELLS_ON_ROW) % GameProperties.CELLS_ON_ROW == GameProperties.CELLS_ON_ROW - 1:
            return False
        if GameProperties.game_map[pos + i + 1] != 0:
            return False

    return True
def checkFullOneRow(pos):
    for i in range (pos, pos + 12):
        if GameProperties.game_map[i] == 0:
            return False
    return True

def checkFullAllRow(pos):

    first_row = (pos + GameProperties.tetromino[GameProperties.rotation][0]) // GameProperties.CELLS_ON_ROW
    second_row = (pos + GameProperties.tetromino[GameProperties.rotation][3]) // GameProperties.CELLS_ON_ROW
    col_take = []
    for i in range (first_row * GameProperties.CELLS_ON_ROW, second_row * GameProperties.CELLS_ON_ROW + GameProperties.CELLS_ON_ROW, GameProperties.CELLS_ON_ROW):
        if checkFullOneRow(i):
            col_take.append(i)
            for j in range (i, i + 12):
                GameProperties.game_map[j] = 0

    ct_length = len(col_take)
    if ct_length != 0:
        #GOT POINTS AFTER FULL ROW
        GameProperties.game_point = GameProperties.game_point + 10 * ct_length 
        checkLevel(GameProperties.game_point)
        head_pos = col_take[0]
        for i in reversed(range(0, head_pos)):
            if GameProperties.game_map[i] != 0:
                res = GameProperties.game_map[i]
                GameProperties.game_map[i] = 0
                GameProperties.game_map[i + ct_length * GameProperties.CELLS_ON_ROW] = res
def checkRot(pos):
    GameProperties.new_rotation = (GameProperties.rotation + 1) % 4
    first_cell = checkTetLeft(GameProperties.tetromino[GameProperties.new_rotation])
    last_cell = checkTetRight(GameProperties.tetromino[GameProperties.new_rotation])
    length = (last_cell + GameProperties.CELLS_ON_ROW) % GameProperties.CELLS_ON_ROW - (first_cell + GameProperties.CELLS_ON_ROW) % GameProperties.CELLS_ON_ROW
    if (pos + checkTetLeft(GameProperties.tetromino[GameProperties.rotation]) + GameProperties.CELLS_ON_ROW) % GameProperties.CELLS_ON_ROW < 5:
        for i in GameProperties.tetromino[GameProperties.new_rotation]:
            if (pos + i + GameProperties.CELLS_ON_ROW) % GameProperties.CELLS_ON_ROW == 11:
                return ((pos // GameProperties.CELLS_ON_ROW) * GameProperties.CELLS_ON_ROW  + 
                ((first_cell + pos) % GameProperties.CELLS_ON_ROW - (pos) % GameProperties.CELLS_ON_ROW))
    else:
        for i in GameProperties.tetromino[GameProperties.new_rotation]:
            if (pos + i + GameProperties.CELLS_ON_ROW) % GameProperties.CELLS_ON_ROW == 0:
                return (pos // GameProperties.CELLS_ON_ROW) * GameProperties.CELLS_ON_ROW + 11 - length
    return pos

def checkLose(pos):
    for i in range (0, 12):
        if GameProperties.game_map[i] != 0:
            return True
    return False
