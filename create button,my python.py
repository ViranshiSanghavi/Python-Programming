from tkinter import *
import tkinter
from tkinter import messagebox as t
top=tkinter.Tk()
def click():
    t.showinfo("Hello","My Python Button !!")
    z=Button(top,text="OK")
B=Button(top,text="Click me",command=click)
B.pack()
top.mainloop()
