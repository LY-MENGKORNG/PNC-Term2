import tkinter as tk

# Create an empty window
root = tk.Tk() 
# Set TK window size to width 600 px and height 200 px
root.geometry("800x2000")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame() 
# Set the title of the frame
frame.master.title("Hello PNC")

# HERE YOU CAN START TO DRAW
# canvas is like "svg tag" in HTML, it allows user to draw shapes
canvas = tk.Canvas(frame)
# <-------Eye left------>
canvas.create_oval(50, 100, 300, 200, outline="#1abc9c", fill="pink")
# <-------Eye left------>
canvas.create_oval(50, 100, 300, 200, outline="#1abc9c", fill="#000000")
canvas.create_oval(170, 110, 240,190, outline="#1abc9c", fill="red")
# <-------Eye right------>
canvas.create_oval(500, 100, 750, 200, outline="#1abc9c", fill="#000000")
canvas.create_oval(620, 110, 690,190, outline="#1abc9c", fill="red")
# <-------Nose------>
canvas.create_oval(370, 310, 440,390, outline="#1abc9c", fill="#000000")
# <-------teeth------>
canvas.create_rectangle(170, 310, 240,390, outline="#1abc9c", fill="#000000")
# <-------Mouse------>
canvas.create_oval(200, 470, 600, 620, outline="#1abc9c", fill="#000000")
# canvas.create_text(200, 200, text="Just do it", font=("Purisa", 26))
# pack means "draw what you put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()

