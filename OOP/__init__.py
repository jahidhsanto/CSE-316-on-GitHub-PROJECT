import tkinter as tk
import jahidFrame

root = tk.Tk()

frame1 = tk.Frame()

button1 = tk.Button(frame1, text='Call Frame2', command=jahidFrame())
button1.pack()

frame1.pack()

root.mainloop()
