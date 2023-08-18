from random import choice
from tkinter import *

master=Tk()
c=Canvas(master, width=500, height=100)
c.pack()

# <---Main program--->
def ovals(event):
    global x1, y1, x2, y2
    c.create_oval(x1,y1,x2,y2, fill=choice(colors))
    x1+=10
    y1+=10
    x2+=30
    y2+=30
    # c.create_oval(30,30,50,50)
colors=["red", "green", "blue", "yellow"]
x1=30
y1=30
x2=50
y2=50
    
c.bind("<Button-1>", ovals)
c.mainloop()