
from random import choice, random, randrange
from re import T
from tkinter import *

from pyautogui import position

#-------CANSTANTS -------------------------
WINDOW_WIDTH=600
WINDOW_HEIGHT=600
moveRight=True
# ---------------------------------

root=Tk()
root.geometry(str(WINDOW_WIDTH)+ "x" + str(WINDOW_HEIGHT))
frame=Frame()
canvas=Canvas(frame)

# Main program
# def drawCircle():
#     position=canvas.coords(ball)
#     if WINDOW_WIDTH > position[2]:
#         canvas.move(ball, 10,10)
#         canvas.after(100, drawCircle) 
#     else:
#         drawAgain()
        
# def drawAgain():
#     pos=canvas.coords(ball)
#     if pos[0] >0:
#         canvas.move(ball, -10,-10)
#         canvas.after(100, drawAgain) 
#     else:
#         drawCircle()
#     print(position[0])
def drawCircle():
    global moveRight
    pos=canvas.coords(ball)
    if pos[0] >= WINDOW_WIDTH-50:
        moveRight=False
    elif pos[0] ==0:
        moveRight=True
        
    if moveRight:
        moveX= 10
    else:
        moveX=-10
    canvas.move(ball, moveX,0)
    canvas.after(100, drawCircle)
    

    
    





ball=canvas.create_oval(0, 0, 50,50, fill="purple" )


drawCircle()
#DISPLAY
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()