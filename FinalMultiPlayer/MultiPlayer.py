import tkinter as tk
from tkinter import font
from tkinter import messagebox


# create class for Tic-Tac-Toe game
class ticTacToe:

    # create class constructor
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Tic-Tac-Toe")

        # create font
        my_font = font.Font(family="Helvetica", size=12, weight="bold")

        # add label
        self.label = tk.Label(self.main_window, text="Please input the size of the gameboard:", font=my_font)
        self.label.grid(row=0, column=0, columnspan=2)

        # add entry field
        self.entry_field = tk.Entry(self.main_window, width=2)
        self.entry_field.grid(row=1, column=0)
        self.entry_field.focus_set()

        # add button
        self.play_button = tk.Button(self.main_window, text="Play", command=self.play_game, font=my_font)
        self.play_button.grid(row=1, column=1)

        # run the main loop
        tk.mainloop()

    # function to start the game
    def play_game(self):
        # get the size of the gameboard
        self.size = self.entry_field.get()
        if self.size.isdigit() and int(self.size) > 1:
            self.size = int(self.size)
            self.game_window = tk.Tk()
            self.game_window.title("Tic-Tac-Toe")
            self.game_window.geometry("300x300")
            self.game_window.resizable(0, 0)

            # create variable to store the state of the game
            self.game_state = [[0 for i in range(self.size)] for j in range(self.size)]
            self.player_turn = 1
            self.game_running = True

            # create a canvas
            self.game_canvas = tk.Canvas(self.game_window, width=300, height=300)
            self.game_canvas.pack()

            # draw the lines on canvas
            self.line_distance = 300 / self.size
            for i in range(1, self.size):
                self.game_canvas.create_line(0, i * self.line_distance, 300, i * self.line_distance)
                self.game_canvas.create_line(i * self.line_distance, 0, i * self.line_distance, 300)

            # create mouse click event
            self.game_canvas.bind("<Button-1>", self.mouse_click)
        else:
            messagebox.showerror("Error", "Please enter a valid size!")

    # function to draw X or O
    def draw_x_o(self, x, y):
        center_x = (x * self.line_distance) + (self.line_distance / 2)
        center_y = (y * self.line_distance) + (self.line_distance / 2)
        if self.player_turn == 1:
            self.game_canvas.create_oval(center_x - 15, center_y - 15, center_x + 15, center_y + 15, fill="black")
            self.game_state[x][y] = 1
        else:
            self.game_canvas.create_line(center_x - 15, center_y - 15, center_x + 15, center_y + 15, width=3,
                                         fill="red")
            self.game_canvas.create_line(center_x + 15, center_y - 15, center_x - 15, center_y + 15, width=3,
                                         fill="red")
            self.game_state[x][y] = 2

    # function to check win
    def check_win(self):
        # check for row
        for i in range(self.size):
            if self.game_state[i][0] != 0:
                for j in range(1, self.size):
                    if self.game_state[i][j] != self.game_state[i][j - 1]:
                        break
                    if j == self.size - 1:
                        return self.game_state[i][0]
        # check for column
        for i in range(self.size):
            if self.game_state[0][i] != 0:
                for j in range(1, self.size):
                    if self.game_state[j][i] != self.game_state[j - 1][i]:
                        break
                    if j == self.size - 1:
                        return self.game_state[0][i]
        # check for diagonal (from left top to right bottom)
        if self.game_state[0][0] != 0:
            for i in range(1, self.size):
                if self.game_state[i][i] != self.game_state[i - 1][i - 1]:
                    break
                if i == self.size - 1:
                    return self.game_state[0][0]
        # check for diagonal (from right top to left bottom)
        if self.game_state[0][self.size - 1] != 0:
            for i in range(1, self.size):
                if self.game_state[i][self.size - 1 - i] != self.game_state[i - 1][self.size - i]:
                    break
                if i == self.size - 1:
                    return self.game_state[0][self.size - 1]
        # check for draw
        for i in range(self.size):
            for j in range(self.size):
                if self.game_state[i][j] == 0:
                    return 0
        return 3

    # function to handle mouse click
    def mouse_click(self, event):
        if self.game_running == True:
            x = int(event.x / self.line_distance)
            y = int(event.y / self.line_distance)
            if self.game_state[x][y] == 0:
                self.draw_x_o(x, y)
                self.player_turn = (self.player_turn + 1) % 2
                result = self.check_win()
                if result == 1:
                    messagebox.showinfo("Result", "Player 1 Won")
                    self.game_running = False
                elif result == 2:
                    messagebox.showinfo("Result", "Player 2 Won")
                    self.game_running = False
                elif result == 3:
                    messagebox.showinfo("Result", "It's a draw")
                    self.game_running = False


# create object of ticTacToe class
t = ticTacToe()