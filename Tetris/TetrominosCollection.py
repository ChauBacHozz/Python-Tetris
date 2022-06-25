CELLS_ON_ROW = 12
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
