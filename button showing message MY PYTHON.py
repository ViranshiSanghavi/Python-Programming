from tkinter import *
import tkinter.messagebox as t

top = Tk()  # Use 'Tk' with a capital 'T'

def click():
    t.showinfo("Hello", "My Python Button!!")

B = Button(top, text="Click Me", command=click)
B.pack()

top.mainloop()
