
from random import choice
from tkinter import *

b=Tk()
b.title("Button")
b.geometry("600x600")
b.configure(bg="black")
# color=Canvas(b,width=500,height=500)

# <----Main program--->
l=Label(b,height=3,text="Hello World",bg="black",fg="white")
l.pack()             #pack : use to display s.th

c=Canvas(b,width=300,height=300)
c.configure(bg="black")
c.pack()


def addColors():
    c.create_oval(50,50,250,250, fill=choice(colors))
    # my_text=Label(b, text="Who allow you to click it !!")
    # my_text.pack()
    # print("I love you")
    
colors=["red", "green", "blue", "yellow","pink"]
c.create_oval(50,50,250,250, fill=choice(colors))
button=Button(b, height=1, text="Click to change colors", command=addColors)
# button=Button(b, text="Click to change colors", width=40,height=500, bg="pink", command=addColors)
button.pack()

# color.bind("<Button-1>", addColors)
b.mainloop()