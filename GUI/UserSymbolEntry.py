import tkinter as tk
from tkinter import *
from GUI import gameBoardFrame


def inputUserSymbol(boardSize):
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Tic Tac Toe")
    root.geometry("500x300")

    tk.Label(root, text="Tic Tac Toe", font=('Ariel', 25)).pack()

    # create a label
    label = tk.Label(root, text="Size of the gameboard", font=('Ariel', 16))
    label.pack()

    # Define a function to get the output for selected option
    label02 = tk.Label(root, font=('Ariel', 16))

    def selection():
        selected = "You have selected " + str(radio.get())
        label02.config(text=selected)

    # create an entry
    radio = IntVar()
    r1 = Radiobutton(root, font=('Ariel', 16), text="X", variable=radio, value=1, command=selection)
    r1.pack(anchor=N, side=tk.LEFT)
    r2 = Radiobutton(root, font=('Ariel', 16), text="0", variable=radio, value=2, command=selection)
    r2.pack(anchor=N, side=tk.RIGHT)

    # create a button
    button = tk.Button(root, text="Submit", height=2, width=10, bd=3,
                       command=lambda: gameBoardFrame.gameBoard(boardSize, radio.get()))
    label02.pack()
    button.pack()
    root.mainloop()


# if __name__ == '__main__':
#     inputUserSymbol(4)
