# Ex:1
# def hasMonsterOnCell (monsterPosition, cellX, cellY):
#     isFound=False
#     for i in range(len(monsterPosition)):
#         if monsterPosition[i][0] == cellX and monsterPosition[i][1]==cellY:
#             isFound=True
#     return isFound

# position=eval(input())
# for row in range(5):
#     for col in range(5):
#         result=hasMonsterOnCell(position,col,row)
#         if result:
#             print("*",end="")
#         else:
#             print("0",end="")
#     print("")


# Ex: 2


def isInfected(grid, r, c ) :
    return grid[r][c] == 1


def getNextInfectedCells(grid) :
    result = []
    for row in range(rowNb):
        for col in range(columnNb):
            infected= isInfected(grid,row,col)
            if infected:
    return result

grid=[[0, 0, 0, 0, 0],
      [0, 1, 0, 1, 0],
      [1, 0, 0, 0, 0],
      [0, 1, 0, 1, 0],
      [0, 0, 0, 0, 0]]




def willBeInfected(grid, r, c) :

    # 1- Check if any VETICAL CONTAMINATION   (top cell and buttom cells are  infected)
    verticalCont = False
    horizontalCont = False
    rowNb = len(grid)-2
    columnNb = len(grid[0])-2
    # 3- cell infected if vertical or horizontal contamination
    return verticalCont,horizontalCont



            
    
    
            
    