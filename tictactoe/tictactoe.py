#!/usr/bin/env python3
# Import modules
try:
    from tkinter import *
except:
    from Tkinter import *

# Constants
SCREEN_W    = 683
SCREEN_H    = 470 
BUTTON_W    = 15
BUTTON_H    = 3
FONT        = ('Arial', 24, 'bold')
X           = True
O           = False

class Game:
    def __init__(self):
        # Internal variables
        self.game_over      = False
        self.win            = False
        self.row            = [0]*3
        self.column         = [0]*3
        self.main_diagonal  = 0
        self.anti_diagonal  = 0
        self.cell_count     = 0
        self.player         = X

        # Create main window
        self.root = Tk()
        self.root.geometry(str(SCREEN_W) + 'x' + str(SCREEN_H))
        self.root.resizable(False, False)
        self.root.title('Tictactoe')
        self.root.config(bg = '#0DA192')

        # Images
        self.image_none     = PhotoImage(file = 'none.png')
        self.image_x        = PhotoImage(file = 'x.png')
        self.image_o        = PhotoImage(file = 'o.png')
        self.image_new_game = PhotoImage(file = 'new_game.png')

        # Create frames
        self.game_frame      = Frame(self.root, bg = '#0DA192')      # Frame contains Tictactoe game
        self.white_space1    = Frame(self.root, bg = '#0DA192', width = 20)
        self.control_frame   = Frame(self.root, bg = '#0DA192')      # Frame contains new game button and announcement
        self.white_space2    = Frame(self.control_frame, bg = '#0DA192', height = 20)
        self.control_frame1  = Frame(self.control_frame, bg = 'white') 
        self.control_frame2  = Frame(self.control_frame, bg = '#0DA192')      # Frame contains new game button and announcement

        # Create Tictactoe game
        self.cell = [[None]*3 for _ in range(3)]              # 3x3 table for Tictactoe game
        for i in range(3):
            for j in range(3):
                self.cell[i][j] = Button(self.game_frame, command = lambda i=i, j=j : self.make_move(i, j))
                self.cell[i][j].config(image = self.image_none, relief = RAISED)

        # Create announcement
        self.announce_text = StringVar()
        self.announce_text.set('It\'s ' + ('X' if self.player == X else 'O') + ' turn')
        self.announce = Label(self.control_frame1, textvariable = self.announce_text)
        self.announce.config(font = FONT, bg = 'white')

        # Create new game button
        self.b_new_game = Button(self.control_frame2, command = self.new_game)
        self.b_new_game.config(image = self.image_new_game) 

        # Display widgets
        # Game frame
        self.game_frame.grid(row = 0, column = 0)
        for i in range(3):
            for j in range(3):
                self.cell[i][j].grid(row = i, column = j)

        self.white_space1.grid(row = 0, column = 1)

        # Control frame
        self.control_frame.grid(row = 0, column = 2)
        self.control_frame1.grid(row = 0)
        self.white_space2.grid(row = 1)
        self.control_frame2.grid(row = 2)
        self.announce.pack()
        self.b_new_game.pack()

    def check(self): # Check for win or game over condition
        self.win = any(abs(i) == 3 for i in self.row + self.column + [self.main_diagonal] + [self.anti_diagonal])
        self.game_over = self.cell_count >= 9 or self.win

        if self.game_over:
            if self.win:
                self.announce_text.set(('X' if self.player == O else 'O') + ' win!')
            else:
                self.announce_text.set('Game over')
            for i in range(3):
                for j in range(3):
                    self.cell[i][j]['command'] = 0

    def make_move(self, i, j): # Function call when players make their moves
        if not self.game_over:
            # Update cell
            self.cell[i][j].config(image = (self.image_x if self.player == X else self.image_o))
            self.cell[i][j]['command'] = 0

            # Update internal variables
            self.row[i]         +=  1 + self.player*-2
            self.column[j]      +=  1 + self.player*-2
            self.main_diagonal  += (1 + self.player*-2)*(i == j)
            self.anti_diagonal  += (1 + self.player*-2)*(i + j == 2)
            self.cell_count     +=  1
            self.player          =  not self.player # Switch player

            # Update announcement and check for win condition
            self.announce_text.set('It\'s ' + ('X' if self.player == X else 'O') + ' turn')
            self.check()

    def new_game(self): # Function call when user pressed new game
        self.game_over      = False
        self.win            = False
        self.row            = [0]*3
        self.column         = [0]*3
        self.main_diagonal  = 0
        self.anti_diagonal  = 0
        self.cell_count     = 0
        self.player         = X
        self.announce_text.set('It\'s ' + ('X' if self.player == X else 'O') + ' turn')
        for i in range(3):
            for j in range(3):
                self.cell[i][j].config(image = self.image_none)
                self.cell[i][j]['command'] = lambda i = i, j = j : self.make_move(i, j)

master = Game()
master.root.mainloop()
