from random import randrange
from tkinter import *

root=Tk()
root.geometry("600x600")
frame=Frame()
frame.master.title("ColorfulGrid")
canvas=Canvas(frame)


# ----Main program---------
colors= ['aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 
'lime', 'maroon', 'navy', 'olive', 'orange', 'purple', 'red', 
'silver', 'teal', 'white', 'yellow']
x1=100
x2=200
y1=100
y2=200









# ----------Display-------
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()