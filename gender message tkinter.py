from tkinter import *

top = Tk()

def selection1():
    selection = "You selected Male"
    label.config(text=selection)

def selection2():
    selection = "You selected Female"
    label.config(text=selection)

radio = IntVar()
r1 = Radiobutton(top, text="Male", variable=radio, value=1, command=selection1)
r1.pack(anchor=W)
r2 = Radiobutton(top, text="Female", variable=radio, value=2, command=selection2)
r2.pack(anchor=W)

label = Label(top)
label.pack()

top.mainloop()
