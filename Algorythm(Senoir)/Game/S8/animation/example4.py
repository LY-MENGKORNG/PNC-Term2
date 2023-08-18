from glob import glob
from random import choice, random, randrange
from tkinter import *

root=Tk()
root.geometry("600x600")
frame=Frame()
canvas=Canvas(frame)

#CONSTANTS
colors=["red", "green", "blue", "black", "purple", "pink", "teal", "orange"]
countCircle=0
# Main program
def random():
    x=randrange(0,500)
    y=randrange(0,500)
    size=randrange(0,500)
    return x, y, size

    #---------Stop when circles are 10---------
def drawCircle():
    global countCircle
    position=random()
    if countCircle<10:
        canvas.create_oval( position[0], position[1], position[0]+position[2], position[1]+position[2],fill=choice(colors))
        canvas.after(1000, drawCircle)
    countCircle+=1
drawCircle()
    

#DISPLAY
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()