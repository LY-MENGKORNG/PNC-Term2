import tkinter as tk
import random

# Create an empty window
root = tk.Tk()
root.geometry("600x600")

frame = tk.Frame()
canvas = tk.Canvas(frame)
def myEventTrigger(event):
    print("User has clicked at position : ", event.x, event.y)

canvas.create_oval(50, 50, 300, 300, fill="red", tags="PNCTarget")
canvas.tag_bind("PNCTarget","<Button-1>",myEventTrigger)



canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()
