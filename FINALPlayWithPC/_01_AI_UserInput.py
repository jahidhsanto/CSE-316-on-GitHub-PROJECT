import tkinter as tk
from tkinter import messagebox

from FINALPlayWithPC._02_UI import TicTacToeUI


class UserInput:
    def __init__(self):
        # Create the main window
        window = tk.Tk()
        window.title('Tic-Tac-Toe Game')
        window.geometry('400x400')

        # Create a Label frame
        frame = tk.LabelFrame(window, text='Input User Details')
        frame.pack(fill='both', ex='yes')

        # Create a Label
        label1 = tk.Label(frame, text='Enter size of game board (e.g. 3): ')
        label1.pack(padx=10, pady=10)

        # Create an Entry
        entry1 = tk.Entry(frame)
        entry1.pack(padx=10, pady=10)

        # Create a Label
        label2 = tk.Label(frame, text='Choose your symbol (X or O): ')
        label2.pack(padx=10, pady=10)

        # Create an Entry
        entry2 = tk.Entry(frame)
        entry2.pack(padx=10, pady=10)

        # Create a Label
        label3 = tk.Label(frame, text='Choose difficulty level (1-3): ')
        label3.pack(padx=10, pady=10)

        # Create an Entry
        entry3 = tk.Entry(frame)
        entry3.pack(padx=10, pady=10)

        # Create a function to start the game
        def start_game():
            size = entry1.get()
            symbol = entry2.get()
            difficulty = entry3.get()
            if size == '' or symbol == '' or difficulty == '':
                messagebox.showinfo('Input Error', 'Please fill all entries!')
                print(type(difficulty))
            else:
                # Start the Tic-Tac-Toe game
                # Code for starting the game here
                TicTacToeUI(int(size), symbol, difficulty)
                # board_size = 3
                # TicTacToeUI(board_size)

        # Create a button to start the game
        button = tk.Button(window, text='Start', command=start_game)
        button.pack(fill='both', ex='yes', padx=10, pady=10)

        window.mainloop()
