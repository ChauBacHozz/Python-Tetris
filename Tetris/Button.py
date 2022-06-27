import GameProperties

class ResetButton:
    def __init__(self, text, width, height, pos, color, font):
        # global font
        self.top_rect = GameProperties.pg.Rect(pos, (width,height))
        self.top_color = color
        self.text = font.render(text, True, (255,255,255))
        self.text_rect = self.text.get_rect(center = self.top_rect.center)
    def draw(self):
        GameProperties.pg.draw.rect(GameProperties.screen, self.top_color, self.top_rect, border_radius=4)
        GameProperties.screen.blit(self.text, self.text_rect)  
    def click(self, event):
        # global drop_pos, game_pause, game_point
        x, y = GameProperties.pg.mouse.get_pos()
        if event.type == GameProperties.pg.MOUSEBUTTONDOWN:
            if GameProperties.pg.mouse.get_pressed()[0]:
                if self.top_rect.collidepoint(x, y):
                    GameProperties.game_pause = False
                    for i in range(0, GameProperties.CELLS_ON_ROW * GameProperties.CELLS_ON_COL):
                        GameProperties.game_map[i] = 0
                        GameProperties.drop_pos = 5
                        GameProperties.game_point = 0
class ExitButton:
    def __init__(self, text, width, height, pos, color, font):
        # global font
        self.top_rect = GameProperties.pg.Rect(pos, (width,height))
        self.top_color = color
        self.text = font.render(text, True, (255,255,255))
        self.text_rect = self.text.get_rect(center = self.top_rect.center)
    def draw(self):
        GameProperties.pg.draw.rect(GameProperties.screen, self.top_color, self.top_rect, border_radius=4)
        GameProperties.screen.blit(self.text, self.text_rect)  
    def click(self, event):
        # global GameProperties.screen_looping
        x, y = GameProperties.pg.mouse.get_pos()
        if event.type == GameProperties.pg.MOUSEBUTTONDOWN:
            if GameProperties.pg.mouse.get_pressed()[0]:
                if self.top_rect.collidepoint(x, y):
                    GameProperties.screen_looping = False
                           
class TimeButton:
    def __init__(self,  width, height, pos, img1, img2, color):
        # global font
        self.top_rect = GameProperties.pg.Rect(pos, (width,height))
        self.top_color = color
        self.play_img = img1
        self.pause_img = img2
        self.icon = img2
        self.text_rect = self.play_img.get_rect(center = self.top_rect.center)
    def draw(self):
        GameProperties.pg.draw.rect(GameProperties.screen, self.top_color, self.top_rect, border_radius=4)
        GameProperties.screen.blit(self.icon, self.text_rect)  
    def click(self, event):
        x, y = GameProperties.pg.mouse.get_pos()
        if event.type == GameProperties.pg.MOUSEBUTTONDOWN:
            if GameProperties.pg.mouse.get_pressed()[0]:
                if self.top_rect.collidepoint(x, y):
                    GameProperties.game_pause = abs(GameProperties.game_pause - 1)
                    if GameProperties.game_pause == True:
                        self.icon = self.play_img
                        GameProperties.screen.blit(self.icon, self.text_rect)  
                    else:
                        self.icon = self.pause_img
                        GameProperties.screen.blit(self.icon, self.text_rect)     

class StartButton:
    def __init__(self, text, width, height, pos, color, font):
        # global font
        self.top_rect = GameProperties.pg.Rect(pos, (width,height))
        self.top_color = color
        self.text = font.render(text, True, (255,255,255))
        self.text_rect = self.text.get_rect(center = self.top_rect.center)
    def draw(self):
        GameProperties.pg.draw.rect(GameProperties.screen, self.top_color, self.top_rect, border_radius=4)
        GameProperties.screen.blit(self.text, self.text_rect)  
    def click(self, event):
        x, y = GameProperties.pg.mouse.get_pos()
        if event.type == GameProperties.pg.MOUSEBUTTONDOWN:
            if GameProperties.pg.mouse.get_pressed()[0]:
                if self.top_rect.collidepoint(x, y):
                    GameProperties.state = GameProperties.game_states[1]
                    GameProperties.game_pause = False
                    for i in range(0, GameProperties.CELLS_ON_ROW * GameProperties.CELLS_ON_COL):
                        GameProperties.game_map[i] = 0
                        GameProperties.drop_pos = 5
                        GameProperties.game_point = 0

class ScoreButton:
    def __init__(self, text, width, height, pos, color, font):
        # global font
        self.top_rect = GameProperties.pg.Rect(pos, (width,height))
        self.top_color = color
        self.text = font.render(text, True, (255,255,255))
        self.text_rect = self.text.get_rect(center = self.top_rect.center)
    def draw(self):
        GameProperties.pg.draw.rect(GameProperties.screen, self.top_color, self.top_rect, border_radius=4)
        GameProperties.screen.blit(self.text, self.text_rect)  
    def click(self, event):
        x, y = GameProperties.pg.mouse.get_pos()
        if event.type == GameProperties.pg.MOUSEBUTTONDOWN:
            if GameProperties.pg.mouse.get_pressed()[0]:
                if self.top_rect.collidepoint(x, y):
                    print("show score")


