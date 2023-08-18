
from hashlib import new
from random import shuffle,choice
from tkinter import *

#CONSTANT
WINDOW_WIDTH=600
WINDOW_HEIGHT=600

#VARIABLES
COLORS=["red", "green", "blue", "purple", "orange"]
newColors=[]

#FUNCTIONS
def createShape():
    shuffle(COLORS)
    for i in range(len(COLORS)):
        mixColors=canvas.create_rectangle(i*55+150, 100,i*55+200, 150, fill=COLORS[i])
        newColors.append(COLORS[i])
    print(newColors)
    canvas.after(5000, deleteAll)
        
def deleteAll():
    canvas.delete("mixColors")
    
def addNumber():
    canvas.configure(number, text="1")
    

    

#MAIN WINDOW
root=Tk()
root.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
frame=Frame()
canvas=Canvas(frame)
root.config(bg="grey")
    
#CREATE CANVAS
for i in range(len(COLORS)):
    shape=canvas.create_rectangle(i*55+150, 200,i*55+200, 250, fill=COLORS[i], tags=COLORS[i])
    number=canvas.create_text(100,200, text="0", font="arial, 20")
    canvas.tag_bind(COLORS[i], "<Button-1>", addNumber)


#BUTTON
myButton=Button(root, text="Click to start", command=createShape)
myButton.place(x=240, y=300,height=50)


#DISPLAY WINDOW
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()