from tkinter import *

top = Tk()
l1 = Label(top, text="Username")
l1.pack(side=LEFT)

e1 = Entry(top, bd=5)  # Corrected the Entry widget creation
e1.pack(side=RIGHT)

top.mainloop()
