from tkinter import *
from tkinter import messagebox

from FINALPlayWithPC._03_game import TicTacToe


class TicTacToeUI:
    def __init__(self, board_size, symbol, difficulty):
        self.board_size = board_size
        self.root = Tk()
        self.root.title("Tic-Tac-Toe")
        self.buttons = []
        # self.players = [" ", "X", "O"]
        if symbol == "X" or symbol == "x":
            self.players = [" ", "X", "O"]
        elif symbol == "0" or symbol == "O" or symbol == "o":
            self.players = [" ", "0", "X"]
        self.game = TicTacToe(self.board_size)
        # self.difficulty = "hard"
        print(difficulty)
        if difficulty == "1":
            self.difficulty = "easy"
        elif difficulty == "2":
            self.difficulty = "medium"
        else:
            self.difficulty = difficulty
        self.create_buttons()
        self.root.mainloop()

    def create_buttons(self):
        for row in range(self.board_size):
            row_buttons = []
            for col in range(self.board_size):
                button = Button(self.root, text=" ", font='Times 20 bold', bg='white', fg='black', height=4, width=8,
                                command=lambda row=row, col=col: self.button_pressed(row, col))
                button.grid(row=row, column=col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def button_pressed(self, row, col):
        self.game.human_move(row, col)
        self.update_board()
        if self.game.check_win() == 1:
            self.show_result("You win!")
        elif self.game.check_win() == 2:
            self.show_result("You lose!")
        elif self.game.check_win() == 0 and len(self.game.empty_positions()) == 0:
            self.show_result("It's a draw!")
        else:
            self.game.computer_move(self.difficulty)
            self.update_board()
            if self.game.check_win() == 1:
                self.show_result("You win!")
            elif self.game.check_win() == 2:
                self.show_result("You lose!")
            elif self.game.check_win() == 0 and len(self.game.empty_positions()) == 0:
                self.show_result("It's a draw!")

    def update_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.buttons[row][col]["text"] = self.players[self.game.board[row][col]]

    def show_result(self, message):
        result = messagebox.showinfo("Result", message)
        if result == "ok":
            self.root.destroy()
