
# IMPORTS
from random import randrange, choice
import tkinter as tk

#CONSTANTS
WINDOW_HEIGHT=600
WINDOW_WIDTH=600

#VARIABLES
COLORS=["red", "green", "blue", "yellow", "purple", "orange", "teal", "pink"]

# FUNCTIONS
def moveBall(ball, moveX, moveY):
    canvas.move(ball, moveX,moveY)
    
    posX1=canvas.coords(ball)[0]
    posX2= canvas.coords(ball)[2]
    posY2=canvas.coords(ball)[3]
    
    if posX2>=WINDOW_WIDTH:
        moveX = -moveX
        moveY= -moveY
    elif posX1<=0:
        moveX = -moveX
        moveY= -moveY
    elif posY2 >= WINDOW_HEIGHT:
        moveX= -moveX
        moveY= -moveY
    canvas.itemconfig(ball, fill=choice(COLORS))     
    canvas.after(50, moveBall(ball, moveX, moveY))
   


# MAIN WINDOW
root = tk.Tk() 
root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')


#BALL
ball1 = canvas.create_oval(0,0,50,50,fill="red", outline="")
ball2 = canvas.create_oval(0,550,50,600,fill="black", outline="") 
ball3 = canvas.create_oval(550,0,600,50,fill="purple", outline="") 
ball4 = canvas.create_oval(550,550,600,600,fill="blue", outline="") 
moveBall(ball1,10, 10 )
moveBall(ball2,10, -10 )
moveBall(ball3,-10, 10 )
moveBall(ball4,-10, -10 )

root.mainloop()



