# IMPORTS21``
import tkinter as tk

#MOVE BALL
move_ball=True


# FUNCTIONS
def moveBall():
    global move_ball
    pos=canvas.coords(ball)
    if pos[2]>= 600:
        move_ball=False
    elif pos[0] == 0:
        move_ball=True
    
    if move_ball:
        posX, posY=10,10
    else:
        posX, posY=-10,-10
        
    canvas.move(ball, posX, posY)
    canvas.after(50, moveBall)
    

# MAIN 
root = tk.Tk() 
root.geometry("600x600")
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')

#BALL
ball = canvas.create_oval(0,0,50,50,fill="teal", outline="")
moveBall()

root.mainloop()