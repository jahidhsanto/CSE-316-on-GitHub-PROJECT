import tkinter as tk
from GUI import UserSymbolEntry


def inputBoardSize():
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Tic Tac Toe")

    tk.Label(root, text="Tic Tac Toe", font=('Ariel', 25)).pack()

    # create a label
    label = tk.Label(root, text="Size of the gameboard", font=('Ariel', 16))
    label.pack()

    # create an entry
    entry = tk.Entry(root, font=('Ariel', 16))
    entry.pack(padx=50, pady=10, ipadx=10, ipady=10)

    # create a button
    button = tk.Button(root, text="Submit", height=2, width=10, bd=3,
                       command=lambda: UserSymbolEntry.inputUserSymbol(int(entry.get())))
    button.pack()

    root.mainloop()

# if __name__ == '__main__':
#     inputBoardSize()
