from tkinter import *

root=Tk()
root.geometry("600x600")
frame=Frame()
canvas=Canvas(frame)

#------------Main program --------------------------
score=0
#------------Sum---------
def add(event):
    global score
    if score < 100:
        score+=2
    else:
        greater_Than_100()
    canvas.itemconfig(item,text=score)
    
    
#------------Multiply---------
def multiply(event):
    global score
    if score < 100:
        score*=2
    else:
        greater_Than_100()
    canvas.itemconfig(item, text=score)
    
#------------Divide---------
def divide(event):
    global score
    if score < 100:
        score/=2
    else:
        greater_Than_100()
    canvas.itemconfig(item, text=score)
        
        
#------------Greater than 100 reset ------
def greater_Than_100():
    global score
    score=0
    canvas.itemconfig(item,text=score)
    
#------------Reset all score ------
def reset(event):
    global score
    if score>100:
        score=0
    else:
        score=0
    canvas.itemconfig(item,text=score)


#-----------------------------GRAPHIC------------------------
item=canvas.create_text(300, 150,text=score, font=("arial", 30,"bold"),fill="orange")
                        #------------Multipy---------
# canvas.create_rectangle(180, 180, 220, 220, outline="black")
canvas.create_text(200, 200, text="x2",font=("arial", 30, "bold"),borderWidth=2, tags="multiply")
                        #------------Divide---------
canvas.create_rectangle(380, 180, 420, 220, outline="black")
canvas.create_text(400, 200,text="/2", font=("arial", 30, "bold"), tags="divide")
                        #------------Sum---------
canvas.create_rectangle(250, 230, 350, 280, outline="black")
canvas.create_text(300, 250, text="+2",font=("arial", 30, "bold"), tags="add")
                        #------------Reset---------
canvas.create_rectangle(250, 180, 350, 220, outline="black")
canvas.create_text(300, 200,text="Reset", font=("arial", 30, "bold"), tags="reset")


#-------------Remotes-------------------------------
canvas.tag_bind("add", "<Button-1>", add)
canvas.tag_bind("multiply", "<Button-1>", multiply)
canvas.tag_bind("divide", "<Button-1>", divide)
canvas.tag_bind("reset", "<Button-1>", reset)


#------------Display --------------------------------
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()