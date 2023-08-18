
import tkinter as tk
from random import randrange

root=tk.Tk()
root.geometry("800x800")
canvas=tk.Canvas(root)
# <---Main program--->
nb=randrange(0,9)
for i in range(9):
    color="red"
    if i == nb:
        color="blue"
    canvas.create_oval(i*50,50,50+(i*50),100, fill=color)     
        

canvas.pack(expand=True, fill='both')
root.mainloop()