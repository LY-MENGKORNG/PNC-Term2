# IMPORTS 
from random import randrange
import tkinter as tk

 
# CONSTANT
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

#VARIABLES
paddleY1=735
ballX2=50
ballY2=50
move_right = 50
move_left=-50
scores=0


# ----------------------------------------------------------------
                    # FUNCTIONS 
# ----------------------------------------------------------------


# BALL_MOVE
def moveBall(ball, moveX, moveY): 
    canvas.move(ball, moveX, moveY)
    pos_ballX1 = canvas.coords(ball)[0] 
    pos_ballX2 = canvas.coords(ball)[2] 
    pos_ballY1= canvas.coords(ball)[1]
    pos_ballY2= canvas.coords(ball)[3]
    if pos_ballX1 <=0:
        moveX = -moveX
    elif pos_ballX2 >= WINDOW_WIDTH:
        moveX=-moveX 
    elif pos_ballY1 <=0:
        moveY=-moveY
    elif pos_ballY2 >= paddleY1:
        moveY=-moveY
        canvas.itemconfig(score, text=str(addScore()))
         
    canvas.after(20, lambda: moveBall(ball, moveX, moveY)) 


# MOVE_PADDLE_RIGHT
def movePaddle_Right(event):
    global paddle
    padX2=canvas.coords(paddle)[2]
    if padX2 <WINDOW_WIDTH:
        canvas.move(paddle, move_right,0)
        
        
# MOVE_PADDLE_LEFT
def movePaddle_Left(event):
    global paddle
    padX1=canvas.coords(paddle)[0]
    if padX1 > 0:
        canvas.move(paddle, move_left,0)
   
#SCORES
def addScore():
    global scores
    scores+=1
    return scores
    
# ----------------------------------------------------------------
                        # MAIN WINDOW
# ----------------------------------------------------------------
root = tk.Tk()  
root.geometry( str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT)) 
canvas = tk.Canvas(root) 
canvas.pack(expand=True, fill='both') 
canvas.config(bg="black")
l=tk.Label(root, text="score:", font="arial, 30")
l.place(relx=0.4, rely=0.05,anchor="ne")
 
# ----------------------------------------------------------------
                        # CREATE BALL AND PADDLE
# ----------------------------------------------------------------
ball1 = canvas.create_oval(0,0,ballX2,ballY2,fill="yellow", outline="") 
paddle=canvas.create_rectangle(0, paddleY1, 100,750, fill="white")

# ----------------------------------------------------------------
                        #  SCORE
# ----------------------------------------------------------------
score=canvas.create_text(350,59,text="0" ,font="arial, 30", fill="white")

# ----------------------------------------------------------------
                        # REMOTES
# ----------------------------------------------------------------
root.bind("<Right>",movePaddle_Right)
root.bind("<Left>",movePaddle_Left)


# ----------------------------------------------------------------
                    #RUN FUNCTIONS
# ----------------------------------------------------------------
moveBall(ball1, randrange(0,20), randrange(0,20)) 

 
# ----------------------------------------------------------------
                        # DISPLAY WINDOW
# ----------------------------------------------------------------
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



















# from random import randrange
# from tkinter import *

# #CONSTANT
# WINDOW_WIDTH=800
# WINDOW_HEIGHT=800
# BALL_SIZE= 50

# #VARIABLES
# x=randrange(0, 700)
# y=randrange(0, 700)
# paddleY1=735
# DOWN="down"
# UP="up"

# #BALL FORWARD
# forward="up"
# #FUNCTIONS
# def fallDown(ball,moveX, moveY):
#     # global DOWN, UP
#     canvas.move(ball,moveX,moveY)
#     posX1=canvas.coords(ball)[0]
#     posX2=canvas.coords(ball)[2]
#     posY1=canvas.coords(ball)[1]
#     posY2=canvas.coords(ball)[3]
#     moveX=randrange(0,100)
#     moveY=randrange(0,100)
#     if forward==UP:
#         if posY2 >= paddleY1:
#             moveY=-moveY
#         elif posY1 <= 0:
#             moveY=-1*moveY
#     # elif posX2 >= WINDOW_WIDTH:
#     #     moveX=-1*moveX
#     # if posX1 <=0:
#     #     moveX=-moveX
#     # elif posX2 >=WINDOW_WIDTH:
#     #     moveX=-moveX
        
#     canvas.after(100, lambda: fallDown(ball,moveX, moveY))

    
# #MAIN WINDOW
# root=Tk()
# root.geometry(str(WINDOW_WIDTH)+ "x" + str(WINDOW_HEIGHT))
# frame=Frame()
# canvas=Canvas(frame)

# #BALLS
# ball=canvas.create_oval(x, 0, x+50, 50, fill="red")
# canvas.create_rectangle(0, paddleY1, 800,750, fill="black")

# fallDown(ball,x,y)




# #DISPLAY
# canvas.pack(expand=True, fill="both")
# frame.pack(expand=True, fill="both")
# root.mainloop()
