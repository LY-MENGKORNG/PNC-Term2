# IMPORTS 
import tkinter as tk 
 
# CONSTANT
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600


#VARIABLES
POSITIVE=True
NEGATIVE=False

#MOVE BALL
moveBlueball=True
moveRedball=True

# FUNCTIONS 
def moveBall(ball, direction, time): 
    ballX1 = canvas.coords(ball)[0] 
    ballX2 = canvas.coords(ball)[2] 

    if ballX2 >= WINDOW_WIDTH and direction==POSITIVE: 
        direction=NEGATIVE
    elif ballX1 <= 0 and direction==NEGATIVE: 
        direction=POSITIVE
        
    if direction== POSITIVE:
        moveX=10
    else:
        moveX=-10
         
    canvas.move(ball, moveX, 0) 
    canvas.after(time, lambda: moveBall(ball, direction, time)) 
     
# MAIN  
root = tk.Tk()  
root.geometry( str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT)) 
canvas = tk.Canvas(root) 
canvas.pack(expand=True, fill='both') 
 
#BALL 
ball1 = canvas.create_oval(0,0,50,50,fill="blue", outline="") 
ball2 = canvas.create_oval(0,100,50,150,fill="red", outline="") 

moveBall(ball1, moveBlueball, 20) 
moveBall(ball2, moveRedball, 50) 
 
root.mainloop()