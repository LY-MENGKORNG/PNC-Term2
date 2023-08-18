
from random import choice
from tkinter import *

# --------Root graphic--------
root=Tk()
root.geometry("1000x1000")
frame=Frame()
frame.master.title("Hello PNC")
canvas=Canvas(frame)

# <---Main program--->
colors=["red", "green", "blue", "yellow", "orange", "black","purple","gray"]
for row in range(0, 10):
    for col in range(0, 10):
        if row == 0 or col == 0 or row == 9 or col == 9:
            canvas.create_rectangle(55*col+50, 55*row+50, 55*col+100,55*row+100, fill=choice(colors))
        elif row%2 != 0 and col%2 != 0:
            canvas.create_rectangle(55*col+50, 55*row+50, 55*col+155,55*row+155, fill=choice(colors))
            
    

# ----------Display --------
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()