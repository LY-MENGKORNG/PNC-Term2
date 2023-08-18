from curses.textpad import rectangle
import tkinter as tk
root=tk.Tk()
root.geometry=("800x800")
frame=tk.Frame()
frame.master.title("Hello PNC")
canvas=tk.Canvas(frame)
# <---Main program--->
def myEventTrigger(event):
    canvas.create_rectangle(140, 60, 220,120 , fill="blue", tags="recTarget")
    canvas.tag_bind("recTarget","<Button-1>", myEventTrigger2)
    
def myEventTrigger2(event):
     canvas.create_rectangle(60, 140, 240,190 , fill="yellow")
    

oval=canvas.create_oval(60,60,120,120, fill="red", tags="squareTarget")
canvas.tag_bind("squareTarget","<Button-1>",myEventTrigger)






canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()