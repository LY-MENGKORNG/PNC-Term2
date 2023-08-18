import tkinter as tk
root=tk.Tk()
root.geometry("1500x1500")
frame=tk.Frame()
frame.master.title("Captain America")
canvas=tk.Canvas(frame)

# <----Face---->
canvas.create_oval(50, 100, 550,700, fill="yellow")
# <----Hair---->
canvas.create_oval(30, 190, 150,310, fill="black")
canvas.create_oval(90, 80, 290,280, fill="black")
canvas.create_oval(220, 60, 420,260, fill="black")
canvas.create_oval(350, 80, 550,280, fill="black")
canvas.create_oval(460, 200, 580,320, fill="black")
# <----Eye left---->
canvas.create_oval(90, 330, 250,400, fill="white")
canvas.create_oval(130, 330, 210,400, fill="blue")
canvas.create_oval(165, 360, 175,370, fill="black")
# <----Eye right---->
canvas.create_oval(360, 330, 520,400, fill="white")
canvas.create_oval(400, 330, 480,400, fill="blue")
canvas.create_oval(435, 360, 445,370, fill="black")
# <----Nose---->
canvas.create_oval(300, 470, 360,530, fill="black")
canvas.create_oval(250, 470, 310,530, fill="black")
canvas.create_oval(270, 400, 340,530, fill="brown")
# <----Mouth---->
canvas.create_oval(345, 560, 405,620, outline="red", fill="red")
canvas.create_oval(195, 560, 250,620, outline="red", fill="red")
canvas.create_oval(200, 580, 400,630,outline="red", fill="red")
# <----Shield Capatain---->
x1=520
y1=520
x2=820
y2=820
colors=["red", "white", "red", "blue"]
for i in range(4):
    canvas.create_oval(x1, y1, x2, y2, outline="#1abc9c", fill=colors[i])
    x1+=30
    y1+=30
    x2-=30
    y2-=30
starPoints = [630,660,660,660,
              670,630,680,660,
              710,660,685,680,
              695,710,670,690,
              645,710,655,680]

canvas.create_polygon(starPoints, fill='white', outline='blue')
canvas.create_text(300,750, text="Captain Sal", font=("Purisa", 70), fill="black")















canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

# Display all
root.mainloop() 