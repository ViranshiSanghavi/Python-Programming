#Q. Write a program to create an arc(give the arc as red; bg color blue)
import tkinter as tk

# Create a tkinter window
window = tk.Tk()
window.title("Arc Example")

# Create a canvas widget
canvas = tk.Canvas(window, width=300, height=200, bg="blue")
canvas.pack()

# Define the coordinates and angles for the arc
x1, y1, x2, y2 = 50, 50, 250, 150
start_angle = 0
extent_angle = 90

# Create the arc with red color
canvas.create_arc(x1, y1, x2, y2, start=start_angle, extent=extent_angle, outline="red", fill="blue")

# Run the Tkinter main loop
window.mainloop()
