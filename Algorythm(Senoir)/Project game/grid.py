
# from socket import CAN_BCM
from email.mime import image
from tkinter import *
from PIL import ImageTk, Image


#---------------------CONSTANTS----------------
WINDOW_WIDTH=1220
WINDOW_HEIGHT=690

#---------------------VARIABLES----------------
empty_cell=0
wall_cell=1
player_cell=2
isValue=False
virus1_cell=3
#----------------------MAIN WINDOW-------------
root=Tk()
root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
frame=Frame()
canvas=Canvas(frame)


#----------------------IMAGES-----------------
bg=PhotoImage(file="IMAGE/background.png")
background=PhotoImage(file="IMAGE/f.png")
player_img=PhotoImage(file="IMAGE/player.gif")
wall_img=PhotoImage(file="IMAGE/wall.gif")
virus1_img=PhotoImage(file="IMAGE/cat.png")


#----------------------GRID WINDOW--------------
grid=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
      [1, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
      ]

virus=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
      ]


#----------------------FUNCTIONS MOVE PLAYER------------------

# GET INDEX OF PLAYER CELL
def getIndex(index):
    for row in range(len(index)):
        for col in range(len(index[row])):
            if index[row][col] == player_cell:
                return row, col

# MOVE PLAYER
def movePlayer(dx, dy):
    global grid, isValue, wall_cell, player_cell, empty_cell
    playerIndex=getIndex(grid)
    playerPositionX =  playerIndex[0]
    playerPositionY =  playerIndex[1]
    if isValue:
        if dx == 1 and dy == 0 and  grid[playerPositionX][playerPositionY+1] != wall_cell:
            grid[playerPositionX][playerPositionY] = empty_cell
            grid[playerPositionX][playerPositionY+1] = player_cell
            # arrayDrawing()
        elif dx == -1 and dy == 0 and  grid[playerPositionX][playerPositionY-1] != wall_cell:
            grid[playerPositionX][playerPositionY] = empty_cell
            grid[playerPositionX][playerPositionY-1] = player_cell
            # arrayDrawing()
        elif dx == 0 and dy == 1 and  grid[playerPositionX+1][playerPositionY] != wall_cell:
            grid[playerPositionX][playerPositionY] = empty_cell
            grid[playerPositionX+1][playerPositionY] = player_cell
            # arrayDrawing()
        elif dx == 0 and dy == -1 and  grid[playerPositionX-1][playerPositionY] != wall_cell:
            grid[playerPositionX][playerPositionY] = empty_cell
            grid[playerPositionX-1][playerPositionY] = player_cell
            # arrayDrawing()
    draw()
        
    
# MOVE RIGHT
def moveRight(event):
    movePlayer(1,0)
    
# MOVE LEFT
def moveLeft(event):
    movePlayer(-1,0)
    
# MOVE UP
def moveUp(event):
    movePlayer(0,-1)

# MOVE DOWN
def moveDown(event):
    movePlayer(0,1)
        
 #----------------------------------------------------------------   
 
# ---------------------DRAW GRAPHICS------------------------
def arrayDrawing():
    canvas.delete("all")
    global grid, virus, isValue
    score=canvas.create_text(500, 50, text="0", font="arial, 20")
    canvas.create_image(1, 0, image=background, anchor="nw")
    y=80
    if isValue:
        for row in range(len(grid)):
            x=60
            for col in range(len(grid[row])):
                if grid[row][col] == wall_cell: 
                    canvas.create_image(x,y, image=wall_img, anchor="nw")
                elif grid[row][col] == empty_cell:
                    canvas.create_rectangle(x, y,x+50, y+50,outline="", fill="")
                elif grid[row][col] == player_cell:
                    canvas.create_image(x+1,y, image=player_img, anchor="nw")
                if virus[row][col] == virus1_cell:
                    canvas.create_image(x+1,y, image=player_img, anchor="nw")
                x+=50
            y+=50 
    canvas.create_rectangle(30, 20, 150, 60, fill="red")
    canvas.create_text(90,40, text="Back",font="arial, 25",tags="back_home")
    canvas.tag_bind("back_home","<Button-1>",back_home)
    

def draw():
    arrayDrawing()
    # canvas.after(50, virus1_move)
    
    # monMove()
    
  
    

# ----------------------HOME & BACK $ INSTRUCTION-----------------------

def start(event):
    global isValue
    isValue = True
    draw()

def back_home(event):
    global isValue
    isValue=False
    home()
    
def home():
    canvas.create_image(1,0, image=background, anchor="nw")
    canvas.create_rectangle(30, 20, 150, 60, fill="red" )
    canvas.create_text(90,40, text="Start",font="arial, 25",tags="start")
    canvas.tag_bind("start","<Button-1>",start)



                

#--------------------------------------------------------


#---------------------MONSTER MOVE ----------------------

#GET INDEX OF MONSTER
# def virusPosition(virusPosition):
#     global virus
#     for row in range(len(virus)):
#         for col in range(len(virus[row])):
#             if virus[row][col] == virusPosition:
#                 return row, col
    
    
#MONSTER MOVE
# def virus1_move():
#     global virus
#     virusIndex=virusPosition(virus1_cell)
#     virusPositionX=virusIndex[0]
#     virusPositionY=virusIndex[1]
#     if virus[virusPositionX][virusPositionY+1] != wall_cell:
#         virus[virusPositionX][virusPositionY] = empty_cell
#         virus[virusPositionX][virusPositionY+1]= virus1_cell
        
    









home()

#---------------------KEY EVENT ----------------------
root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)




#DISPLAY WINDOW
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()
