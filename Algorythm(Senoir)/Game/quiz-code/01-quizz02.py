import tkinter as tk

# Create an empty window
root = tk.Tk() 
# Set TK window size to width 600 px and height 200 px
root.geometry("600x200")
# Create a frame in the window (frame is a container, like "div" in HTML)
frame = tk.Frame() 
# Set the title of the frame
frame.master.title("Hello PNC")

canvas = tk.Canvas(frame)

canvas.create_oval(50, 50, 100, 100, fill="#FF0000")
canvas.create_oval(100, 100, 200, 200, fill="#00FF00")
canvas.create_oval(200, 200, 400, 400, fill="#0000FF")

# pack means "draw what i put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop()