
from curses import color_content
import tkinter as tk
from random import randrange
root = tk.Tk()
root.geometry("600x600")
frame=tk.Frame()
frame.master.title("PNC UI GAME")


# canvas is like "svg tag" in HTML, it allows user to draw shapes
canvas = tk.Canvas(frame)
x1=20
y1=50
x2=70
y2=90
colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'purple','teal']
for x in range(9):
    for y in range(9):
        colorIndex = randrange(0, len(colors)-1)
        canvas.create_oval(x1,y1,x2,y2, outline="#1abc9c", fill=colors[colorIndex])
        canvas.create_text(x1+25,y1+20, text="Me", font=("Purisa", 10), fill="white")
        x1+=60
        x2+=60
    x1=20
    x2=70
    y1+=50
    y2+=50
        
# canvas.create_text(200, 200, text="Just do it", font=("Purisa", 26))
# pack means "draw what you put inside"
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop() 