import GameProperties as GameProps
import CheckEvent
import TetrominosCollection
import Draw
import Button
import random

playImg = GameProps.pg.image.load("./asset/play-64.png")
pauseImg = GameProps.pg.image.load("./asset/pause-64.png")
loseBgImg = GameProps.pg.image.load("./asset/loseBG.jpg")
loseBgImg = GameProps.pg.transform.scale(loseBgImg, (1020, 700))

timeBtn = Button.TimeButton(130, 150, (655, GameProps.NEXTTET_UPPER_GAP - 70), playImg, pauseImg, (255, 65, 0))          
exitBtn = Button.ExitButton("EXIT", 180, 60, (600, 560), (255,0,0), GameProps.levelFont)
resetBtn = Button.ResetButton("RESET", 180, 60, (520, 640), (255,0,0), GameProps.levelFont)
startBtn = Button.StartButton("START", 200, 100, (GameProps.SCREEN_WIDTH/2 - 100, 280), (0,0,0), GameProps.startMenuFont)                       
menuExitBtn = Button.ExitButton("EXIT", 200, 100, (GameProps.SCREEN_WIDTH/2 - 100, 380), (0,0,0), GameProps.startMenuFont)
loseResetBtn = Button.StartButton("Start a new game", 250, 60, (120, 570), (0,0,0), GameProps.buttonLoseFont)
loseExitBtn = Button.ExitButton("Exit, give up (and be a pussy)", 800, 60, (-10, 650), (0,0,0), GameProps.buttonLoseFont)



while GameProps.screen_looping:
    GameProps.pg.display.flip()
    GameProps.screen.fill(GameProps.BLACK)
    if GameProps.state == "start_menu":
        for event in GameProps.pg.event.get():
            startBtn.click(event)
            menuExitBtn.click(event)
            if event.type == GameProps.pg.QUIT:
                GameProps.screen_looping = False 
        Draw.showStartMenu()
        startBtn.draw()
        menuExitBtn.draw()
    if GameProps.state == "game_play":
        if GameProps.pg.key.get_pressed()[GameProps.pg.K_DOWN]:
                if GameProps.game_pause == False:
                    GameProps.fall_speed = 0.05
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
                            GameProps.move_down = 0
                    if event.key == GameProps.pg.K_RIGHT:
                        if CheckEvent.rightEdge(GameProps.drop_pos):
                            GameProps.drop_pos += 1
                            GameProps.move_down = 0
                    if event.key == GameProps.pg.K_SPACE:
                        if CheckEvent.checkEdge(GameProps.drop_pos) == False:
                            GameProps.drop_pos = CheckEvent.checkRot(GameProps.drop_pos)
                            GameProps.rotation = (GameProps.rotation + 1) % 4
            if event.type == GameProps.pg.KEYUP:
                if event.key == GameProps.pg.K_LEFT:
                    GameProps.move_down = GameProps.CELLS_ON_ROW
                if event.key == GameProps.pg.K_RIGHT:
                    GameProps.move_down = GameProps.CELLS_ON_ROW
                if event.key == GameProps.pg.K_DOWN:
                    GameProps.fall_speed = GameProps.current_speed
        Draw.drawTetrisSurface()
        Draw.drawTakenTetrominos()
        Draw.drawNextTetSection()
        Draw.drawTetromino(GameProps.drop_pos, GameProps.color)
        timeBtn.draw()
        exitBtn.draw()
        resetBtn.draw()
        if CheckEvent.checkLose(GameProps.drop_pos):
            GameProps.game_pause = True
            GameProps.state = GameProps.game_states[2]
        #Đếm thời gian, sau một thời gian đủ thì thực hiện rơi tetromino
        GameProps.fall_time += GameProps.clock.get_rawtime()
        GameProps.clock.tick()
        if GameProps.fall_time/1000 >= GameProps.fall_speed:
            GameProps.fall_time = 0
            if CheckEvent.checkEdge(GameProps.drop_pos) == False:
                GameProps.drop_pos += GameProps.move_down
            else: 
                #Lưu giá trị màu sắc của tetromino vào vị trí tương ứng trong game_map
                for i in GameProps.tetromino[GameProps.rotation]:
                    GameProps.game_map[GameProps.drop_pos + i] = GameProps.color
                CheckEvent.checkFullAllRow(GameProps.drop_pos)
                #Tạo ra tetromino mới, reset lại vị trí ban đầu, tạo màu mới 
                GameProps.rand_num = GameProps.rand_num_next
                GameProps.tetromino = TetrominosCollection.tetrominos[GameProps.rand_num]
                GameProps.color = GameProps.color_next
                GameProps.drop_pos = 5
                GameProps.rotation = 0
                GameProps.rand_num_next = random.randint(0, 6)
                GameProps.color_next = GameProps.COLORS[GameProps.rand_num_next]
        if GameProps.game_pause == True:
            #Dừng thời gian 
            GameProps.clock.tick(0)
        Draw.showScore(GameProps.game_point)
        Draw.drawLevel(GameProps.level)
        print(GameProps.level)
    if GameProps.state == "end":
        for event in GameProps.pg.event.get():
            loseExitBtn.click(event)
            loseResetBtn.click(event)
            if event.type == GameProps.pg.QUIT:
                GameProps.screen_looping = False 
        GameProps.screen.blit(loseBgImg, (-20,-50))
        loseScore = GameProps.scoreLoseFont.render(str(GameProps.game_point), True, (255,255,255))
        GameProps.screen.blit(loseScore, (340, 477))
        loseResetBtn.draw()
        loseExitBtn.draw()
