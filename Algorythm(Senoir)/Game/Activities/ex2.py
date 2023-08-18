import tkinter as tk
from random import randrange

root = tk.Tk()
root.geometry("1000x1000")
canvas=tk.Canvas(root)

# <---Main progran--->
for y in range(5):
    for x in range(5):
        if x == y:
            color="red"
        else:
            color="blue"
        canvas.create_oval(x*65,y*65,60+(x*65),60+(y*65), fill=color)



canvas.pack(expand=True,fill='both')
root.mainloop()