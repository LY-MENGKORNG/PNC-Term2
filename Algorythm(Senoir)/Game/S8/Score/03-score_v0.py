import tkinter as tk
from random import choice

root = tk.Tk()
root.geometry("550x200")
canvas = tk.Canvas(root)

score = 0
colors=["red", "green", "blue", "yellow", "orange", "black"]
def inc_score(event) :
    global score
    score += 1
    # new=score
    canvas.itemconfig(item, text=score)
    canvas.itemconfig(shape, fill=choice(colors))
    
    # canvas.itemconfig(item,text=score, fill='black')

item=canvas.create_text(25, 25, text=score, font=('consolas', 24, 'bold'), fill='black')
shape=canvas.create_rectangle(100, 100, 200, 200, tags="PNCTarget", fill='red')

canvas.tag_bind("PNCTarget","<Button-1>",inc_score)
root.bind('<Return>', inc_score)
root.bind('<Button-3>', inc_score)

# pack means "draw what I put inside"
canvas.pack(expand=True, fill='both')
root.mainloop()
