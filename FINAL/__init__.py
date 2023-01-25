from tkinter import *
from FINALPlayWithPC._01_AI_UserInput import UserInput
from FinalMultiPlayer.MultiPlayer import ticTacToe

# creating frame and window
root = Tk()
root.title("Tic-Tac-Toe Game")
root.geometry("400x400")


# functions
def computer():
    UserInput()
    print("You have selected to Play With Computer")


def friend():
    ticTacToe()
    print("You have selected to Play With Friends")


def about():
    print("This game is developed in python by @aviral_singh")


def exit():
    root.destroy()


# creating label widget
label = Label(root, text="Welcome to Tic-Tac-Toe Game", font=("Arial Bold", 15))
label.pack()

# creating button widget
computer_btn = Button(root, text="Play with Computer", command=computer, width=20, height=2)
computer_btn.pack()

friend_btn = Button(root, text="Play with Friends", command=friend, width=20, height=2)
friend_btn.pack()

about_btn = Button(root, text="About", command=about, width=20, height=2)
# about_btn.pack()

exit_btn = Button(root, text="Exit", command=exit, width=20, height=2)
exit_btn.pack()

# running mainloop
root.mainloop()
