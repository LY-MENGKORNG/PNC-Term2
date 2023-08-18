
import tkinter as tk


def displayHelloWorld():
    canvas.move(item,0,10)
    canvas.after(500, displayHelloWorld)


# Create an empty window
root = tk.Tk() 
root.geometry("600x600")
frame = tk.Frame() 
canvas = tk.Canvas(frame)


item=canvas.create_text(300,300, text = "Hello world")
canvas.after(1000, lambda:displayHelloWorld())




canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()