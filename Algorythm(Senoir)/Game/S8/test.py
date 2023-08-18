#  IMPORTS
from tkinter import *

from PIL import Image, ImageTk

#  CONSTANTS
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024

#---------Variables---------
EMPTY_CEL=0
WALL_CELL=2
PLAYER_CEL=1
REWARD_CEL=6
MONSTER_CEL=9
ENERMY_MOVE=True
# squareSize = #choose the appropriate size of the squares
root = Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
frame=Frame()
canvas = Canvas(frame)
canvas.configure(bg="black")

#---------Image---------
my_player=PhotoImage(file="image/dog.png")
reward=PhotoImage(file="image/coin.png")
monster=PhotoImage(file="image/monster.png")


#----------------------Functions-------------------------

#-------Find index Number one-----
def findIndex(array):
    for row in range(0, len(array)):
        for col in range(0, len(array[row])):
            if array[row][col] == 1:
                return row, col

#---------Move Right-------------
def moveRight(event):
    global grid, WALL_CELL
    index=findIndex(grid)
    if grid[index[0]][index[1]+1] != WALL_CELL:
        grid[index[0]][index[1]] = 0
        grid[index[0]][index[1]+1] = 1
    drawing()
    
#---------Move Left-------------
def moveLeft(event):
    global grid, WALL_CELL
    index=findIndex(grid)
    if grid[index[0]][index[1]-1] != WALL_CELL:
        grid[index[0]][index[1]] = 0
        grid[index[0]][index[1]-1] = 1
    drawing()
    
#---------Move Up-------------
def moveUp(event):
    global grid, WALL_CELL
    index=findIndex(grid)
    if grid[index[0]-1][index[1]] != WALL_CELL:
        grid[index[0]][index[1]] = 0
        grid[index[0]-1][index[1]] = 1
    drawing()
    
#---------Move Down-------------
def moveDown(event):
    global grid, WALL_CELL
    index=findIndex(grid)
    if grid[index[0]+1][index[1]] != WALL_CELL:
        grid[index[0]][index[1]] = 0
        grid[index[0]+1][index[1]] = 1
    drawing()

#------------------------Monster Position------------------
def monsterMove():
    global ENERMY_MOVE
    pos=canvas.coords(mon)
    # print(pos)
    if pos[1] > 660:
        ENERMY_MOVE=False
    elif pos[1] == 550:
        ENERMY_MOVE=True
    
    if ENERMY_MOVE:
        moveY=10
    else:
        moveY=-10
    canvas.move(mon,0, moveY)
    canvas.after(100,monsterMove)
    # return pos
    
#Reward
# def rewardCell():
#     global coin
#     position=canvas.coords(coin)
#     monsterPos=monsterMove()
#     if position[0]>=monsterPos[0] or position[0]<=monsterPos[0]:
#         canvas.delete("all")
#     print(position)
    


   

# Array
grid = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2],
        [2,2,2,2,2,0,0,0,0,2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,1,0,0,2,2,2,2,2,0,0,0,2],
        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2],
        [2,2,2,2,2,0,0,0,0,2,0,0,0,2,2,2,2,2],
        [2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]] 


#--------Desing Graphic---------
def drawing():
    global mon, coin
    canvas.delete("all")
    y=40
    for i in range(len(grid)):
        value = grid[i]
        x = 50
        for j in range(len(value)):
            if value[j] == EMPTY_CEL:
                canvas.create_rectangle(x, y, x+50, y+50, fill='white')
                # canvas.create_image(x,y, image=emty, anchor='nw')
            elif value[j] == WALL_CELL:
                    # canvas.create_image(x,y, image=stoneImage, anchor='nw')
                    canvas.create_rectangle(x,y,x+50,y+50,fill="red")
            elif value[j] == PLAYER_CEL:
                canvas.create_rectangle(x,y,x+50,y+50,fill="white")
                canvas.create_image(x+25,y+25,image=my_player)
            # elif value[j] == REWARD_CEL:
            #     canvas.create_rectangle(x,y,x+50,y+50,fill="white")
            x += 50
        y += 50
    coin=canvas.create_image(125,665,image=reward)
    mon=canvas.create_image(675,550,image=monster) 

drawing()
monsterMove()
# rewardCell() 



            
#---------Remotes--------------------
root.bind("<Right>", moveRight)
root.bind("<Left>", moveLeft)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)

    

# ---------Display--------------------
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
root.mainloop()