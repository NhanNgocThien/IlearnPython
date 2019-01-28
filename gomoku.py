# Date created: 28/01/2019
# Human vs human gomoku game

# Import modules
try:
    from tkinter import *
except:
    from Tkinter import *

# Constants
SCREEN_W    = 800
SCREEN_H    = 580
BUTTON_W    = 15
BUTTON_H    = 3
CELL_W      = 9
CELL_H      = 5
FONT        = ('Helvetica', 24)
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
        self.root.title('Gomoku')



        # Create frames
        self.game_frame     = Frame(self.root)      # Frame contains Gomoku game
        self.control_frame  = Frame(self.root)      # Frame contains new game button and announcement



        # Create Gomoku game
        self.cell       = [[None]*3 for _ in range(3)]              # 3x3 table for Gomoku game
        self.cell_text  = [[None]*3 for _ in range(3)]              # Displayed text for each cell ('X' or 'O')
        for i in range(3):
            for j in range(3):
                self.cell_text[i][j] = StringVar()
                self.cell_text[i][j].set('')
                self.cell[i][j] = Button(self.game_frame, command = lambda i=i, j=j : self.make_move(i, j))
                self.cell[i][j].config(font = FONT, textvariable = self.cell_text[i][j], width = CELL_W, height = CELL_H)



        # Create announcement
        self.announce_text = StringVar()
        self.announce_text.set('It\'s ' + ('X' if self.player == X else 'O') + ' turn')
        self.announce = Label(self.control_frame, textvariable = self.announce_text)
        self.announce.config(font = FONT)



        # Create new game button
        self.b_new_game = Button(self.control_frame, command = self.new_game)
        self.b_new_game.config(text = 'NEW GAME', width = BUTTON_W, height = BUTTON_H)



        # Display widgets
        self.game_frame.grid(row = 0, column = 0)
        for i in range(3):
            for j in range(3):
                self.cell[i][j].grid(row = i, column = j)

        self.control_frame.grid(row = 0, column = 1)
        self.announce.grid(row = 0)
        self.b_new_game.grid(row = 1)




    def check(self):
        self.win = any(abs(i) == 3 for i in self.row + self.column + [self.main_diagonal] + [self.anti_diagonal])
        self.game_over = self.cell_count >= 9 or self.win

        if self.game_over:
            if self.win:
                self.announce_text.set(('X' if self.player == O else 'O') + ' win!')
            else:
                self.announce_text.set('Game over')
            for i in range(3):
                for j in range(3):
                    self.cell[i][j].config(state = 'disabled')



    def make_move(self, i, j):                          # Function call when players make their moves
        if not self.game_over:
            # Update cell
            self.cell_text[i][j].set('X' if self.player == X else 'O')
            self.cell[i][j].config(state = 'disabled')  # Once a move is made in a cell, that cell is disabled

            # Update internal variables
            self.row[i]         +=  1 + self.player*-2
            self.column[j]      +=  1 + self.player*-2
            self.main_diagonal  += (1 + self.player*-2)*(i == j)
            self.anti_diagonal  += (1 + self.player*-2)*(i + j == 2)
            self.cell_count     +=  1
            self.player          =  not self.player     # Switch player

            # Update announcement and check for win condition
            self.announce_text.set('It\'s ' + ('X' if self.player == X else 'O') + ' turn')
            self.check()



    def new_game(self):                                 # Function call when user pressed new game
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
                self.cell_text[i][j].set('')
                self.cell[i][j].config(state = 'normal')

master = Game()
master.root.mainloop()
