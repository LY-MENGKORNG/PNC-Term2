

import tkinter as tk

# Create an empty window
root = tk.Tk() 
# Set TK window size to width 600 px and height 200 px
root.geometry("600x600")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame() 
# Set the title of the frame
frame.master.title("PNC UI GAME")

# HERE YOU CAN START TO DRAW
# canvas is like "svg tag" in HTML, it allows user to draw shapes
canvas = tk.Canvas()
x1=100
y1=100
x2=400
y2=400
colors=["red", "blue","green", "orange","green"]
for i in range(5):
    canvas.create_rectangle(x1, y1, x2, y2, outline="#1abc9c", fill=colors[i])
    x1+=30
    y1+=30
    x2-=30
    y2-=30

# canvas.create_text(200, 200, text="Just do it", font=("Purisa", 26))
# pack means "draw what you put inside"
canvas.pack(expand=True, fill='both')
# frame.pack(expand=True, fill='both')

# Display all
root.mainloop()