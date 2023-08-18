import tkinter as tk
from random import randrange

root = tk.Tk()
root.geometry =("1000x1000")
canvas=tk.Canvas(root)
# <-----Main program---->
colors=["pink","red","green","yellow","orange"]
x1=50
y1=50
x2=100
y2=100
for i in range(10):
    colorIndex=randrange(0,len(colors)-1)
    canvas.create_rectangle(x1,y1,x2,y2, fill=colors[colorIndex])
    x1+=60
    x2+=60
    




canvas.pack(expand=True,fill="both")
root.mainloop()