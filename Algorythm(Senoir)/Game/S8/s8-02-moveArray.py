#  IMPORTS
import tkinter as tk

#  CONSTANTS
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
# squareSize = #choose the appropriate size of the squares
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
canvas = tk.Canvas(root)

#  VARIABLES
grid = [0,0,1,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0]
# Move Array
def findIndex(arr):
    for i in range(len(arr)):
        if arr[i] == 1:
            return i
        
# Move right      
def moveRight(event):
    global grid
    index= findIndex(grid)
    if index < len(grid) - 1:
        grid[index] = 0
        grid[index+1] = 1
    arrayToDrawing()
    print(grid)
    
# Move left
def moveLeft(event):
    global grid
    index = findIndex(grid)
    if index > 0:
        grid[index] = 0
        grid[index-1] = 1
    arrayToDrawing()
    print(grid)

#Drawing
def arrayToDrawing():
    canvas.delete("all")
    global grid
    for i in range(len(grid)):
        if grid[i] == 1: 
            canvas.create_rectangle(100*i,100*i,100*i+100,200*i+200, outline="black", fill="black")
        else:
            canvas.create_rectangle(100*i,100*i,100*i+100,200*i+200, outline="black")
    return None
arrayToDrawing()
    
root.bind("<Right>",moveRight)
root.bind("<Left>",moveLeft)

canvas.pack(expand=True, fill="both")
root.mainloop()