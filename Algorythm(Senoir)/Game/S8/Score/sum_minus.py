from tkinter import *

root=Tk()
root.geometry("600x600")
frame=Frame()
canvas=Canvas(frame)

#------------Main program --------------------------
score=0
def add(event):
    global score
    score+=1
    canvas.itemconfig(item, text=score)
    
def minus(event):
    global score
    if score > 0:
        score-=1
    canvas.itemconfig(item,text=score)



item=canvas.create_text(300, 100,text=score, font=("arial", 30,"bold"))
canvas.create_text(200, 200, text="Add",font=("arial", 30, "bold"), tags="add")
canvas.create_text(400, 200,text="Minus", font=("arial", 30, "bold"), tags="minus")


#-------------Remotes-------------------------------
canvas.tag_bind("add", "<Button-1>", add)
canvas.tag_bind("minus", "<Button-1>", minus)


#------------Display --------------------------------
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()