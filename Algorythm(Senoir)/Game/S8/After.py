from random import randrange
from secrets import choice
from tkinter import *

root=Tk()
root.geometry("800x800")
frame=Frame()
canvas=Canvas(frame)

#--------Constants------------------------
colors=["red", "green", "blue", "yellow", "orange", "black", "orange"]
def circle():
    x=randrange(0, 600)
    y=randrange(0,600)
    size=randrange(0,600)
    canvas.create_oval(x,y,x+size, y+size,fill=choice(colors))
    root.after(500, circle)
circle()


#-----------------Display----------------
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()