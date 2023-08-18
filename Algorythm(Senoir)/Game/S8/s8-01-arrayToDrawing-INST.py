#  IMPORTS
from tkinter import *

#  CONSTANTS
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

#  VARIABLES
grid = [0,0,1,0,0,0,0]

# squareSize = #choose the appropriate size of the squares
root = Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
frame=Frame()
frame.master.title("You and Me")
canvas = Canvas(frame)
 
#  -------Function-----------

#------Find index 1-------
def findIndex(array):
    for arr in range(len(array)):
        if array[arr]== 1:
            return arr
        
        
 #-----------Move Right--------
def moveRight(event):
    global grid
    index=findIndex(grid)
    if index < len(grid)-1:
        grid[index] = 0
        grid[index+1] = 1
    print(grid)
    arrayToDrawing()
    
    
 #-----------Move Left--------
def moveRight(event):
    global grid
    index=findIndex(grid)
    if index < len(grid)-1:
        grid[index] = 0
        grid[index+1] = 1
    print(grid)
    arrayToDrawing()







# draw a line with white and black squares using the global array
def arrayToDrawing():
    canvas.delete("all")
    # y=50
    global grid
    x=50
    for i in range(len(grid)):
        if grid[i] == 1:
            canvas.create_rectangle(x,50,x+50,100, outline="black", fill="black")
        else:
            canvas.create_rectangle(x,50,50+x,100,outline="black")
        x+=50
    # return None
arrayToDrawing()

root.bind("<Right>",moveRight)


canvas.pack(expand=True, fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()


