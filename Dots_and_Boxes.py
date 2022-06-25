from itertools import count
import numpy as np
import pygame
import sys



pygame.init()

class Window():
    def __init__(self, change) -> None:
        self.screen_width = 1100
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Dots and boxes")
        self.backround = (184, 255, 249)
        self.screen.fill(self.backround)
        self.grid = (133, 244, 250)
        self.grid_backround = (250,250,250)
        self.empty_space = 100
        self.border_space = 50
        self.lines_width = 10
        self.lines_height = 90
        self.rects_horiz = []
        self.rects_vertical = []
        self.rects_changed = []


        self.board_status = np.zeros((7,7))
        self.already_marked_boxes = []
        #changed 
        self.change = change
        self.end = change

        #Counter
        self.player1_counter = 0
        self.player2_counter = 0

        self.board()
        self.als()
        self.play()

    def information(self):
        self.GIF_width = 250
        self.GIF_height = 300

        self.GameInformationFace = pygame.Surface((self.GIF_width, self.GIF_height))
        self.GameInformationFace.fill((133, 244, 250))

        #Names
        self.Name_font = pygame.font.SysFont(None, 30)
        self.player1_Label = self.Name_font.render("Player 1", True, "Red")
        self.player2_Label = self.Name_font.render("Player 2", True, (0, 85, 85))

        #Winner
        if self.player1_counter > self.player2_counter:
            self.winner = "Player 1"
        elif self.player2_counter > self.player1_counter:
            self.winner = "Player 2"
        else:
            self.winner = "Draw"
        self.winner_font = pygame.font.SysFont(None, 30)
        self.winner_label  =self.winner_font.render("Winner: ", True, "Black")
        
        if self.winner == "Player 1":
            self.winner_Name = self.winner_font.render(self.winner, True,"Red")
        elif self.winner == "Player 2":
            self.winner_Name = self.winner_font.render(self.winner, True, (0, 85, 85))
        else:
            self.winner_Name = self.winner_font.render(self.winner, True, "Black")

        self.GameInformationFace.blit(self.winner_label, (10,200))
        self.GameInformationFace.blit(self.winner_Name, (100,200))
        
        #instruction
        self.instruction =[
        "Instruction:",
        "The goal is to capture as  many  boxes",
        "as  possible. A  box is captured  when",
        "the fourth wall (side edge) is placed.",
        "You  can  place  one  wall  each turn.",
        "When you have captured a box, you have",
        "to make another  move right away - and",
        "you might get  another box right away.",
        ""
]   
        self.instruction_font = pygame.font.SysFont("Arial",15)
        for self.i in self.instruction:
            self.instruction_label = self.instruction_font.render(self.i, True, "Black")
            self.GameInformationFace.blit(self.instruction_label, (5,535+((self.instruction.index(self.i))*20)))

        #Blits
        self.GameInformationFace.blit(self.player1_Label, (10,10))
        self.GameInformationFace.blit(self.player2_Label, (160,10))

        #counter
        self.Counter_font = pygame.font.SysFont(None, 40)

        self.player1_counter_Label = self.Counter_font.render(str(self.player1_counter), True, "Red")
        self.player2_counter_Label = self.Counter_font.render(str(self.player2_counter), True, (0, 85, 85))

        self.GameInformationFace.blit(self.player1_counter_Label, (40,50))
        self.GameInformationFace.blit(self.player2_counter_Label, (195,50))


    def als(self):
        self.a = 250
        self.b = 410

        self.n = pygame.Surface((self.a, self.b))
        self.n.fill((133, 244, 250))

        self.winner_font = pygame.font.SysFont(None, 30)
        self.buttonLabel = self.winner_font.render("Restart", True, "Black")
        self.n.blit(self.buttonLabel, (95,10))

        self.mouse = pygame.mouse.get_pos()
        self.buttonRect = pygame.Rect(90,5,80,30)
        pygame.draw.rect(self.n, "Black", self.buttonRect,2)

        self.instruction =[
        "Instruction:",
        "The goal is to capture as  many  boxes",
        "as  possible. A  box is captured  when",
        "the fourth wall (side edge) is placed.",
        "You  can  place  one  wall  each turn.",
        "When you have captured a box, you have",
        "to make another  move right away - and",
        "you might get  another box right away.",
        ""
]   
        self.instruction_font = pygame.font.SysFont("Arial",15)
        for self.i in self.instruction:
            self.instruction_label = self.instruction_font.render(self.i, True, "Black")
            self.n.blit(self.instruction_label, (5,200+((self.instruction.index(self.i))*20)))
        

    def restart(self, pos):
        if pos[0] > 890 and pos[0] < 970 and pos[1] > 344 and pos[1] < 375:
            Window(not self.end)
            

    def board(self):
        self.gameFace_width = 800
        self.gameFace_height = 800

        self.gameFace = pygame.Surface((self.gameFace_width,self.gameFace_height))
        self.gameFace.fill(self.backround)
        pygame.draw.rect(self.gameFace, self.grid_backround,(40,40,710,710), border_radius=10)

        for self.row in range(8):
            self.line = []
            for self.column in range(7):
                self.rect = pygame.Rect(self.row * self.empty_space +self.border_space-10,
                                self.column * self.empty_space+self.border_space,
                                self.lines_width,
                                self.lines_height)
                pygame.draw.rect(self.gameFace,(133, 244, 250), self.rect)                
                self.line.append(self.rect)
            self.rects_horiz.append(self.line)

        for self.row2 in range(7):
            self.line2 = []
            for self.column2 in range(8):
                self.rect2 = pygame.Rect(self.row2 * self.empty_space +self.border_space,
                                self.column2 * self.empty_space+self.border_space-10,
                                self.lines_height,
                                self.lines_width)
                pygame.draw.rect(self.gameFace,(133, 244, 250), self.rect2)
                self.line2.append(self.rect2)
            self.rects_vertical.append(self.line2)


    def addBoxes(self):
        boxes = np.argwhere(self.board_status == 4)
        for box in boxes:
            if list(box) not in self.already_marked_boxes and list(box) != []:
                self.already_marked_boxes.append(list(box))
                if not self.change:
                    pygame.draw.rect(self.gameFace,(255, 99, 99),[(90+10)*box[1]+55,
                                                        (90+10)*box[0]+55,
                                                        80,80])
                    self.player1_counter += 1
                    self.change = True

                else:
                    pygame.draw.rect(self.gameFace,(6, 154, 142),[(90+10)*box[1]+55,
                                                        (90+10)*box[0]+55,
                                                        80,80])
                    self.player2_counter += 1
                    self.change = False
    def update(self, type, pos):
        r = pos[0] // 100 
        c = pos[1] // 100
        
        val = 1
        if c < 7 and r < 7:
            self.board_status[c][r] += val

        if type == "row":
            if c >= 1:
                self.board_status[c-1][r] += val

        elif type == 'column':
            if r >= 1:
                self.board_status[c][r-1] += val


    def handle(self, pos):
        self.postion = pos
        
        for self.vertical_row in self.rects_vertical:
            for self.vertical_column in self.vertical_row:
                if self.vertical_column.collidepoint(self.postion) and self.vertical_column not in self.rects_changed:
                    if self.change:
                        pygame.draw.rect(self.gameFace, "Red", self.vertical_column)
                        self.change = False
                    else:
                        pygame.draw.rect(self.gameFace, (0, 85, 85), self.vertical_column)
                        self.change = True
                    self.rects_changed.append(self.vertical_column)
                    self.update("row",self.vertical_column)
                    self.addBoxes()
        for self.horiz_row in self.rects_horiz:
            for self.horiz_column in self.horiz_row: 
                if self.horiz_column.collidepoint(self.postion) and self.horiz_column not in self.rects_changed:
                    
                    if self.change:
                        pygame.draw.rect(self.gameFace, "Red", self.horiz_column)
                        self.change = False
                    else:
                        pygame.draw.rect(self.gameFace, (0, 85, 85), self.horiz_column)
                        self.change = True
                    self.rects_changed.append(self.horiz_column)
                    self.update("column", self.horiz_column)
                    self.addBoxes()

        

    def play(self):
        self.clock = pygame.time.Clock()
        self.changePlayer = True


        self.grid = []
        for self.row_grid in range(10):
            self.grid.append([])
            for self.column_grid in range(10):
                self.grid[self.row_grid].append(0)
        self.a = True
        while self.a:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    sys.exit()

                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    self.restart(self.pos)
                    self.handle(self.pos)

            self.information()
            self.screen.blit(self.gameFace,(0,0))
            self.screen.blit(self.GameInformationFace, (800,40))
            self.screen.blit(self.n,(800,340))
            self.clock.tick(60)
            pygame.display.update()
     






if __name__ == "__main__":
    Window(True)