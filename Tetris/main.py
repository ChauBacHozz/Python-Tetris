import GameProperties as GameProps
import CheckEvent
import TetrominosCollection
import Draw
import Button
import random


#BUTTON DEFINES
playImg = GameProps.pg.image.load("./asset/play-64.png")
pauseImg = GameProps.pg.image.load("./asset/pause-64.png")
                   
timeBtn = Button.TimeButton(130, 150, (655, GameProps.NEXTTET_UPPER_GAP - 70), playImg, pauseImg, (255, 65, 0))          
exitBtn = Button.ExitButton("EXIT", 180, 60, (600, 560), (255,0,0), GameProps.levelFont)
resetBtn = Button.ResetButton("RESET", 180, 60, (520, 640), (255,0,0), GameProps.levelFont)                       

#DRAW SCORE SECTION

#TETROMINO DEFINES
#DRAW STUFFS ON GameProps.screen
#GAME LOOP
move_down = GameProps.CELLS_ON_ROW
current_speed = 0.27
fall_speed = current_speed
fall_time = 0
while GameProps.screen_looping:
    GameProps.pg.display.flip()
    #check game events from keyboard and outter stuffs
    if GameProps.pg.key.get_pressed()[GameProps.pg.K_DOWN]:
            if GameProps.game_pause == False:
                fall_speed = 0.05
    for event in GameProps.pg.event.get():
        timeBtn.click(event)
        exitBtn.click(event)
        resetBtn.click(event)
        if event.type == GameProps.pg.QUIT:
            GameProps.screen_looping = False 
        if event.type == GameProps.pg.KEYDOWN:
            if GameProps.game_pause == False:
                if event.key == GameProps.pg.K_LEFT:
                    if CheckEvent.leftEdge(GameProps.drop_pos):
                        GameProps.drop_pos -= 1
                        move_down = 0
                if event.key == GameProps.pg.K_RIGHT:
                    if CheckEvent.rightEdge(GameProps.drop_pos):
                        GameProps.drop_pos += 1
                        move_down = 0
                if event.key == GameProps.pg.K_SPACE:
                    if CheckEvent.checkEdge(GameProps.drop_pos) == False:
                        GameProps.drop_pos = CheckEvent.checkRot(GameProps.drop_pos)
                        GameProps.rotation = (GameProps.rotation + 1) % 4
        if event.type == GameProps.pg.KEYUP:
            if event.key == GameProps.pg.K_LEFT:
                move_down = GameProps.CELLS_ON_ROW
            if event.key == GameProps.pg.K_RIGHT:
                move_down = GameProps.CELLS_ON_ROW
            if event.key == GameProps.pg.K_DOWN:
                fall_speed = current_speed
    GameProps.screen.fill(GameProps.BLACK)
    Draw.drawTetrisSurface()
    Draw.drawTakenTetrominos()
    Draw.drawNextTetSection()

    Draw.drawTetromino(GameProps.drop_pos, GameProps.color)
    timeBtn.draw()
    exitBtn.draw()
    resetBtn.draw()
    if CheckEvent.checkLose(GameProps.drop_pos):
        GameProps.game_pause = True
        
    fall_time += GameProps.clock.get_rawtime()
    GameProps.clock.tick()
    if fall_time/1000 >= fall_speed:
        fall_time = 0
        if CheckEvent.checkEdge(GameProps.drop_pos) == False:

            GameProps.drop_pos += move_down
        else: 
            for i in GameProps.tetromino[GameProps.rotation]:
                GameProps.game_map[GameProps.drop_pos + i] = GameProps.color
            CheckEvent.checkFullAllRow(GameProps.drop_pos)
            GameProps.rand_num = GameProps.rand_num_next
            GameProps.tetromino = TetrominosCollection.tetrominos[GameProps.rand_num]
            GameProps.color = GameProps.color_next
            GameProps.drop_pos = 5
            GameProps.rotation = 0
            GameProps.rand_num_next = random.randint(0, 6)
            GameProps.color_next = GameProps.COLORS[GameProps.rand_num_next]
    if GameProps.game_pause == True:
        GameProps.clock.tick(0)
    Draw.showScore(GameProps.game_point)
    Draw.drawLevel(GameProps.level)
