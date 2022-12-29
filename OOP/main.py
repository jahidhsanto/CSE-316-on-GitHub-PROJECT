import tkinter as tk

from OOP import main2


def open_window():
    root = tk.Tk()
    root.geometry('200x100')
    root.title('Main Window')

    # Create two text boxes
    num1 = tk.Entry(root)
    num1.pack()
    num2 = tk.Entry(root)
    num2.pack()

    # Create a submit button
    btn = tk.Button(root, text='Submit', command=lambda: main2.open_window2(num1.get(), num2.get()))
    btn.pack()

    root.mainloop()


# Function to open second window
def open_window2(num1, num2):
    root = tk.Tk()
    root.geometry('200x100')
    root.title('Second Window')

    # Calculate the sum and display it
    num3 = int(num1) + int(num2)
    lbl = tk.Label(root, text='Sum is ' + str(num3))
    lbl.pack()
    root.mainloop()


if __name__ == '__main__':
    open_window()
