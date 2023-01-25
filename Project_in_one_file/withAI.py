from tkinter import *
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[0 for x in range(board_size)] for y in range(board_size)]

    def print_board(self):
        for row in range(0, self.board_size):
            for col in range(0, self.board_size):
                print(self.board[row][col], end="  ")
            print()

    def check_win(self):
        # check horizontal
        for row in range(self.board_size):
            if self.board[row][0] != 0 and all(
                    self.board[row][col] == self.board[row][0] for col in range(1, self.board_size)):
                return self.board[row][0]

        # check vertical
        for col in range(self.board_size):
            if self.board[0][col] != 0 and all(
                    self.board[row][col] == self.board[0][col] for row in range(1, self.board_size)):
                return self.board[0][col]

        # check diagonal
        # if self.board[0][0] != 0 and self.board[0][0] == self.board[1][1] == self.board[2][2]:
        #     return self.board[0][0]

        if self.board[0][0] != 0:
            sum_left = []
            for check in range(self.board_size):
                sum_left.append(self.board[check][check])
            list_set = set(sum_left)
            if len(list_set) == 1:
                return self.board[0][0]

        # if self.board[0][self.board_size - 1] != 0 and self.board[0][self.board_size - 1] == self.board[1][
        #     self.board_size - 2] == self.board[2][self.board_size - 3]:
        #     print(self.board_size - 1)
        #     print(self.board[0][self.board_size - 1])
        #     print(self.board[1][self.board_size - 2])
        #     print(self.board[2][self.board_size - 3])
        #     return self.board[0][self.board_size - 1]

        if self.board[0][self.board_size - 1] != 0:
            sum_right = []
            count = 0
            for check in reversed(range(self.board_size)):
                sum_right.append(self.board[count][check])
                count += 1
            list_set = set(sum_right)
            if len(list_set) == 1:
                return self.board[0][self.board_size - 1]

        return 0

    def set_board(self, row, col, player):
        self.board[row][col] = player

    def empty_positions(self):
        empty_pos = []
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row][col] == 0:
                    empty_pos.append([row, col])
        return empty_pos

    def human_move(self, row, col):
        if [row, col] in self.empty_positions():
            self.board[row][col] = 1
        else:
            messagebox.showerror("Error", "Position already used!")
            self.game.human_move(row, col)

    def computer_move(self, difficulty):
        empty_pos = self.empty_positions()
        if len(empty_pos) == 0:
            return

        if difficulty == "easy":
            move_pos = random.choice(empty_pos)
        elif difficulty == "medium":
            move_pos = self.strategic_move(empty_pos, 2)
            if move_pos is None:
                move_pos = random.choice(empty_pos)
        else:
            move_pos = self.strategic_move(empty_pos, 2)
            if move_pos is None:
                move_pos = self.strategic_move(empty_pos, 1)
                if move_pos is None:
                    move_pos = random.choice(empty_pos)

        self.board[move_pos[0]][move_pos[1]] = 2

    def strategic_move(self, empty_pos, player):
        for pos in empty_pos:
            row = pos[0]
            col = pos[1]
            self.board[row][col] = player
            if self.check_win() == player:
                self.board[row][col] = 0
                return pos
            else:
                self.board[row][col] = 0
        return None


class TicTacToeUI:
    def __init__(self, board_size):
        self.board_size = board_size
        self.root = Tk()
        self.root.title("Tic-Tac-Toe")
        self.buttons = []
        self.players = [" ", "X", "O"]
        self.game = TicTacToe(self.board_size)
        self.difficulty = "easy"
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


if __name__ == "__main__":
    board_size = 3
    TicTacToeUI(board_size)
