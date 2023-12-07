import tkinter as tk

def open_file():
    print("File -> Open clicked")

def save_file():
    print("File -> Save clicked")

def exit_app():
    root.quit()

root = tk.Tk()
root.title("Menu Button Example")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

root.mainloop()
