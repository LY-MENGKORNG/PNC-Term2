from random import choice, randrange
from tkinter import *

root=Tk()
root.geometry("600x600")
frame=Frame()
canvas=Canvas(frame)

#CONSTANTS
colors=["red", "green", "blue", "black", "purple", "pink", "teal", "orange"]


# Main program
def drawCircle():
    x=randrange(0,300)
    y=randrange(0,300)
    size=randrange(0,300)
    canvas.create_oval(x, y, x+size, y+size,fill=choice(colors))

def click(event):
    canvas.after(200,drawCircle)


#REMOTES  
root.bind("<c>", click)
    
    


#DISPLAY
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()