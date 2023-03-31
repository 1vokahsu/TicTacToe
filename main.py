import tkinter as tk
from tkinter import Canvas
import random
import time


class TicTacToe(Canvas):

    # create window
    def __init__(self, window):
        super().__init__(window, width=300, height=300)
        self.draw_lines()
        self.state = [None] * 9
        self.bind('<Button-1>', self.click)

    def click(self, event):  # processing the user's progress
        column = event.x // 100
        row = event.y // 100
        index = (row * 3) + column
        if self.state[index] == None:
            self.state[index] = 'x'
            self.add_x(column, row)
            winner = self.get_winner()
            if winner != None:
                time.sleep(0.5)
                self.delete('all')
                self.create_text(150, 150, text=winner, font=('Courier', 30))
                time.sleep(1)
                self.delete('all')
                self.state = [None] * 9
                self.draw_lines()
            else:
                move = self.bot_move()
                column = move % 3
                row = move // 3
                self.add_o(column, row)
                self.state[move] = "o"
                winner = self.get_winner()
                if winner != None:
                    time.sleep(0.5)
                    self.delete('all')
                    self.create_text(150, 150, text=winner, font=('Courier', 30))
                    time.sleep(1)
                    self.delete('all')
                    self.state = [None] * 9
                    self.draw_lines()

    def draw_lines(self):  # drawing the markup
        self.create_line(100, 0, 100, 300, fill='black')
        self.create_line(200, 0, 200, 300, fill='black')
        self.create_line(0, 100, 300, 100, fill='black')
        self.create_line(0, 200, 300, 200, fill='black')

    def add_x(self, column, row):  # Drawing 'X'
        self.create_line(10 + (100 * column), 10 + (100 * row),
                         85 + (100 * column), 85 + (100 * row), width=5, fill='blue')
        self.create_line(10 + (100 * column), 85 + (100 * row),
                         85 + (100 * column), 10 + (100 * row), width=5, fill='blue')

    def add_o(self, column, row):  # Drawing 'O'
        self.create_oval(10 + (100 * column), 10 + (100 * row),
                         85 + (100 * column), 85 + (100 * row), width=5, outline='red')

    def bot_move(self):  # Creating bot

        possibleMoves = [x for x, letter in enumerate(self.state) if letter == None and x != 'o']
        move = None
        for let in ['o', 'x']:
            for i in possibleMoves:
                boardCopy = self.state[:]
                boardCopy[i] = let
                if self.isWinner(boardCopy, let):
                    move = i
                    return move

        cornersOpen = []
        for i in possibleMoves:
            if i in [0, 2, 6, 8]:
                cornersOpen.append(i)
        ln = len(cornersOpen)
        if ln > 0:
            r = random.randrange(0, ln)
            move = cornersOpen[r]
            return move

        if 4 in possibleMoves:
            move = 4
            return move

        edgesOpen = []
        for i in possibleMoves:
            if i in [1, 3, 5, 7]:
                edgesOpen.append(i)
        ln = len(edgesOpen)
        if ln > 0:
            r = random.randrange(0, ln)
            move = edgesOpen[r]
            return move

    def isWinner(self, bo, le):
        return ((bo[6] == le and bo[7] == le and bo[8] == le) or
                (bo[3] == le and bo[4] == le and bo[5] == le) or
                (bo[0] == le and bo[1] == le and bo[4] == le) or
                (bo[6] == le and bo[3] == le and bo[0] == le) or
                (bo[7] == le and bo[4] == le and bo[1] == le) or
                (bo[8] == le and bo[5] == le and bo[2] == le) or
                (bo[6] == le and bo[4] == le and bo[2] == le) or
                (bo[8] == le and bo[4] == le and bo[0] == le))

    def get_winner(self):  # determine the winner
        board = self.state
        if self.isWinner(board, 'x'):
            return 'x_win'
        elif self.isWinner(board, 'o'):
            return 'o_win'

        # Checking for fullness
        elif None not in self.state:
            return 'draw'

        return None

window = tk.Tk()
game = TicTacToe(window)
game.pack()
window.mainloop()   