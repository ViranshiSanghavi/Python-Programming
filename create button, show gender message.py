from tkinter import*
top=Tk()
def selection1():
    selection="You selected the Male"
    label.config(text=selection)
def selection2():
    selection="You selected the Female"
    label.config(text=selection)
radio=IntVar()
r1=Radiobutton(top,text="Male",variable=radio,command=selection1)
r1.pack(anchor=W)
r2=Radiobutton(top,text="Female",variable=radio,command=selection2)
r2.pack(anchor=W)
label=Label(top)
label.pack()
top.mainloop()
