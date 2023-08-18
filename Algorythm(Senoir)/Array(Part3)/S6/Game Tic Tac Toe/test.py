#               For Row
# def checkrow(array2D,row):
#     boo=True
#     for row in range(len(array2D)):
#         if array2D[r][row] !="A":
#             boo=False
#     return boo
        
# listArray=[["A","A","B"],
#            ["A","B","A"],
#            ["A","A","A"]]
# result =""
# for r in range(len(listArray)):
#     isFound=checkrow(listArray,r)
#     if isFound:
#         result = "WIN"
# print(result)





#               For Column
# def checkColumn(array2D,col):
#     boo=True
#     for col in range(len(array2D)):
#         if array2D[col][c] !="A":
#             boo=False
#     return boo
        
# listArray=[["A","A","B"],
#            ["A","B","A"],
#            ["A","A","B"]]
# result="B WIN"
# for c in range(len(listArray)):
#     isFound=checkColumn(listArray,c)
#     if isFound:
#         result = "A WIN"     
# print(result)





#                                onlyAOnDiagonal
# def onlyAOnDiagonal(array2D):
#     nbOfA=0
#     isFound=False
#     for arr in range(len(array2D)):
#         if array2D[arr][arr] == "A":
#             nbOfA+=1
#     if nbOfA==3:
#         isFound=True
#     return isFound

# listArray=[["A","A","B"],
#            ["B","A","A"],
#            ["A","A","A"]]
# if onlyAOnDiagonal(listArray):
#     print("A WIN")
# else:
#     print("B WiN")
    





# <-----------------Full option---------------------->

#   @param grid   (an array 2D)
#   @param rowIndex  (integer)
#   @param sign  (string)
#   @return True if the ROW at the given rowIndex is composed ONLY of the given sign
def signOnRow(grid, rowIndex, sign):
    isFound=False
    nbOfSign=0
    for rowIndex in grid:
        for i in range(len(rowIndex)):
            if grid[rowIndex][i] == sign:
                nbOfSign+=1
        if nbOfSign==3:
            isFound=True
    return isFound   # TO CHANGE !!
    

#   @param grid   (an array 2D)
#   @param columnIndex  (integer)
#   @param sign  (string)
#   @return True if the ROW at the given columnIndex is composed ONLY of the given sign
def signOnColumn(grid, columnIndex, sign):
    # TODO !!


#   @param grid   (an array 2D)
#   @param sign  (string)
#   @return True if a DIAGONAL is composed ONLY of the given sign
def signOnDiagonal(grid, sign):
     # TODO !!   
  

#   @param grid   (an array 2D)
#   @param sign  (string)
#   @return True if the given sign has WON
def hasSignWon(grid, sign):
    # TODO ! 
    #  It true if : 
    #  - one of the 2 diagonal is composed of this sign
    #  - or if 1 of the 3 rows is composed of this sign
    #  - or if 1 of the 3 columns is composed of this

    
# MAIN PROGRAM (nothing to change here !)
grid= [['A', 'A', 'A'],
        ['B', 'A', 'B'],
        ['B', 'B', 'A']]
if hasSignWon(grid, "A"):
    print("A WON")

elif hasSignWon(grid, "B"):
    print("B WON")

else:
    print("NO WINNER")




    