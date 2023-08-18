from doctest import Example
import tkinter as tk
from random import randrange
root=tk.Tk()
root.geometry=("1000x1000")
frame=tk.Frame()
frame.master.title("Lottery")
canvas=tk.Canvas(frame)

# <---Main program---->
def winner(event):
    canvas.create_text(150,150,text="You're win!", font=("arial, 30"))
    

winNumber=randrange(0,8)
for i in range(9):
    canvas.create_oval(i*55,50,50+(i*55),100, fill="blue")
    if winNumber==i:
        canvas.create_oval(i*55,50,50+(i*55),100, fill="blue", tags="win")
        canvas.tag_bind("win", "<Button-1>", winner)
        
        
    






canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()