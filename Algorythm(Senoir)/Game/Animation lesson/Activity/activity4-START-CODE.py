# IMPORTS
import tkinter as tk

# FUNCTIONS
def moveBall():
    pos=canvas.coords(ball)
    posX=10
    posY=10
    print(pos)
    if pos[2] > 600:
        canvas.move(ball,-pos[2], -pos[2])  
    canvas.move(ball, posX,posY)
    canvas.after(100, moveBall)
    


# MAIN 
root = tk.Tk() 
root.geometry("600x600")
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')

ball = canvas.create_oval(0,0,50,50,fill="teal", outline="")

moveBall()

root.mainloop()