# IMPORTS 
from random import randrange
import tkinter as tk 
 
 
# CONSTANT
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

# FUNCTIONS 
def moveBall(ball, moveX, moveY): 
    canvas.move(ball, moveX, moveY)
    ballX1 = canvas.coords(ball)[0] 
    ballX2 = canvas.coords(ball)[2] 
    ballY1= canvas.coords(ball)[1]
    ballY2= canvas.coords(ball)[3]
    
    if ballX1 <=0:
        moveX = -moveX
    elif ballX2 >= WINDOW_WIDTH:
        moveX=-moveX
    elif ballY1 <=0:
        moveY=-moveY
    elif ballY2 >= WINDOW_HEIGHT:
        moveY=-moveY
        
    canvas.after(5, lambda: moveBall(ball, moveX, moveY)) 
     
# MAIN WINDOW
root = tk.Tk()  
root.geometry( str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT)) 
canvas = tk.Canvas(root) 
canvas.pack(expand=True, fill='both') 
 
#CREATE BALL 
ball1 = canvas.create_oval(0,0,50,50,fill="blue", outline="") 
ball2 = canvas.create_oval(0,100,50,150,fill="red", outline="") 
ball3 = canvas.create_oval(0,150,50,200,fill="orange", outline="") 
ball4 = canvas.create_oval(0,200,50,250,fill="purple", outline="") 

#RUN FUNCTIONS
moveBall(ball1, randrange(0,20), randrange(0,20)) 
moveBall(ball2, randrange(0,20), randrange(0,20)) 
moveBall(ball3, randrange(0,20), randrange(0,20)) 
moveBall(ball4, randrange(0,20), randrange(0,20)) 
 
# DISPLAY WINDOW
root.mainloop()
































# from tkinter import  BOTH, Tk, Canvas, mainloop

# ### VARIABLES
# WIDTH = 800
# HEIGHT = 600
# VOLOCITY =  {
#     1: {
#         "xVolocity": 10,
#         "yVolocity": 10
#     },
#     2: {
#         "xVolocity": 20,
#         "yVolocity": 10
#     },
#     3: {
#         "xVolocity": 10,
#         "yVolocity": 20
#     },
#     4: {
#         "xVolocity": 20,
#         "yVolocity": 20
#     }
# }

# ballSIze = 40

# ### FUNCTION
# def moveBall(canvasBall, xVolocity, yVolocity):
#     ### CONDITIONS
#     if shape.coords(canvasBall)[0] > WIDTH-ballSIze:
#         xVolocity = -xVolocity
#     elif shape.coords(canvasBall)[0] < 0:
#         xVolocity = -1*xVolocity
#     elif shape.coords(canvasBall)[1] > HEIGHT-ballSIze:
#         yVolocity = -yVolocity
#     elif shape.coords(canvasBall)[1] < 0:
#         yVolocity = -1*yVolocity

#     ### START THE ANIMATION
#     shape.move(canvasBall, xVolocity, yVolocity)
#     shape.after(10, lambda:moveBall(canvasBall, xVolocity, yVolocity))

#     ### PRINT THE COORDINATION TO TERMINAL
#     print(shape.coords(canvasBall)[0], shape.coords(canvasBall)[2])


# ### MAIN WINDOW
# root = Tk()
# root.geometry(f"{WIDTH}x{HEIGHT}")
# root.resizable(0,0)

# ### CANVAS
# shape = Canvas(root, background="grey")
# ballOne = shape.create_oval(0, 0, ballSIze, ballSIze, fill="red")
# ballTwo = shape.create_oval(100, 100, 100+ballSIze, 100+ballSIze, fill="black")
# ballThree = shape.create_oval(150, 100, 150+ballSIze, 100+ballSIze, fill="cyan")
# ballFour = shape.create_oval(150, 90, 150+ballSIze, 90+ballSIze, fill="yellow")
# shape.pack(expand=True, fill=BOTH)

# listOfBall = [ballOne, ballTwo, ballThree, ballFour]

# ### CALLS FUNCTIONS

# for i in listOfBall:
#     moveBall(i, VOLOCITY[i]["xVolocity"], VOLOCITY[i]["yVolocity"])

# root.mainloop()