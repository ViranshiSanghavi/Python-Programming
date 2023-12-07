# Create a simple python program to create a welcome page by using tkinter
import tkinter as tk

# Create a tkinter window
window = tk.Tk()
window.title("Welcome Page")

# Create a label with a welcome message
welcome_label = tk.Label(window, text="Welcome to Our Program!", font=("Helvetica", 20))
welcome_label.pack(pady=20)

# Create a button to close the window
exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.pack()

# Start the tkinter main loop
window.mainloop()
