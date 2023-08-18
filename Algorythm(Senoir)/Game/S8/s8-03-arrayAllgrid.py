#  IMPORTS
# from textwrap import fill
# import tkinter as tk
# from turtle import bgcolor
from tkinter import *

from PIL import Image, ImageTk

#  CONSTANTS
SCREEN_WIDTH = 920
SCREEN_HEIGHT = 900
wall=2
# squareSize = #choose the appropriate size of the squares
root = Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
frame=Frame()
canvas = Canvas(frame)
canvas.configure(bg="black")


#  VARIABLES
grid = [[0,2,2,2,2,2,2,2,0],
        [2,0,0,0,0,0,0,0,2],
        [2,0,1,0,5,0,0,0,2],
        [2,0,0,0,2,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,2],
        [0,2,2,2,2,2,2,2,0]]

 # Move Array

#Find number one index
def findIndex(arr):
    for row in range(len(arr)):
        index=arr[row]
        for col in range(len(index)):
            if index[col] == 1:
                return row, col

#  Move right      
def moveRight(event):
    global grid, wall
    index= findIndex(grid)
    indexRow=index[0]
    indexCol=index[1]
    if indexCol < len(grid[1]) - 2 :
        grid[indexRow][indexCol] = 0
        grid[indexRow][indexCol+1] = 1
    arrayToDrawing()
    print(grid)
    
# Move left
def moveLeft(event):
    global grid
    index = findIndex(grid)
    indexRow=index[0]
    indexCol=index[1]
    if indexCol > 1:
        grid[indexRow][indexCol] = 0
        grid[indexRow][indexCol-1] = 1
    arrayToDrawing()
    print(grid)
    
    
# Move up
def moveUp(event):
    global grid
    index = findIndex(grid)
    indexRow=index[0]
    indexCol=index[1]
    if indexRow > 1:
        grid[indexRow][indexCol] = 0
        grid[indexRow-1][indexCol] = 1
    arrayToDrawing()
    print(grid)
    
    
# Move down
def moveDown(event):
    global grid
    index = findIndex(grid)
    indexRow=index[0]
    indexCol=index[1]
    if indexRow < len(grid)-2:
        grid[indexRow][indexCol] = 0
        grid[indexRow+1][indexCol] = 1
    arrayToDrawing()
    print(grid)


#Drawing
my_img=PhotoImage(file="image/dog.png")
my_wall=PhotoImage(file="image/Kit-Cat.png")
def arrayToDrawing():
    canvas.delete("all")
    global grid
    for j in range(len(grid)):
        index=grid[j]
        for i in range(len(index)):
            if index[i] == 1: 
                canvas.create_rectangle(100*i+10,100*j+10,100*i+110,110+100*j, outline="white", fill=None)
                canvas.create_image(i*100+60,100*j+60, image=my_img)
            if index[i] == 5:
                canvas.create_rectangle(100*i+10,100*j+10,100*i+110,110+100*j, outline="white", fill=None)
                canvas.create_image(i*100+60,100*j+60, image=my_img)
            if index[i] == 2:
                canvas.create_rectangle(100*i+10,100*j+10,100*i+110,110+100*j, outline="white", fill=None)
                canvas.create_image(i*100+60,50, image=my_wall)
                canvas.create_image(i*100+60,650, image=my_wall)
                canvas.create_image(60,100*j+50, image=my_wall)
                canvas.create_image(860,100*j+50, image=my_wall)
            else:
                canvas.create_rectangle(100*i+10,100*j+10,100*i+110,110+100*j, outline="white", fill=None)
    return None
arrayToDrawing()
    
# Remotes
root.bind("<Right>",moveRight)
root.bind("<Left>",moveLeft)
root.bind("<Up>",moveUp)
root.bind("<Down>",moveDown)

canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()