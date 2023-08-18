from glob import glob
from random import choice, random, randrange
from tkinter import *

root=Tk()
root.geometry("600x600")
frame=Frame()
canvas=Canvas(frame)

#CONSTANTS
colors=["red", "green", "blue", "black", "purple", "pink", "teal", "orange"]

# Main program
def random():
    x=randrange(0,300)
    y=randrange(0,300)
    size=randrange(0,300)
    return x, y, size

def space(event):
    position=random()
    canvas.create_rectangle(position[0], position[1], position[0]+position[2], position[1]+position[2],fill=choice(colors))
    canvas.after(2000,drawCircle)

def drawCircle():
    position=random()
    canvas.create_oval( position[0], position[1], position[0]+position[2], position[1]+position[2],fill=choice(colors))


#REMOTES  
root.bind("<space>", space)
    

#DISPLAY
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()