import tkinter as tk
import frame2

root = tk.Tk()

frame1 = tk.Frame()
frame2 = tk.Frame()

button1 = tk.Button(frame1, text='Call Frame2', command=frame2.call_frame2())
button1.pack()

frame1.pack()
frame2.pack()

root.mainloop()
