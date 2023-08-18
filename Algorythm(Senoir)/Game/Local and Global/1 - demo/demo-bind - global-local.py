import tkinter as tk

root = tk.Tk()

root.geometry('600x600')
frame = tk.Frame()
frame.master.title("BIND EVENT DEMO GLOBAL-LOCAL")
canvas=tk.Canvas(frame)



points = []
def drawCircle(event):
    points.append(event.x)
    points.append(event.y)
    print("print from draw circle function",points)
 
def drawShape(event):
    points = []
    print("print from draw shape function",points)
    
root.bind("star","< Button-1>", drawCircle) #LEFT CLICK
root.bind("<Button-3>", drawShape) #RIGHT CLICK



canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()