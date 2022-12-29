import tkinter as tk


# Function to open second window
def open_window2(num1, num2):
    root = tk.Tk()
    root.geometry('200x100')
    root.title('Second Window')

    # Calculate the sum and display it
    num3 = int(num1) + int(num2)
    lbl = tk.Label(root, text='Sum are ' + str(num3))
    lbl.pack()
    root.mainloop()


if __name__ == '__main__':
    open_window2(20, 30)
