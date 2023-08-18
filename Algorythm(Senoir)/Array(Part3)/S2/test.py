# Ex:1
# def starPosition(array):
#     for i in range(len(array)):
#         if array[i]=="*":
#             index=i
#     return index

# list = ["0", "*", "0", "0", "0"]
# result = starPosition(list)
# list[result]="0"
# list[result+1]="*"
# print(list)


# Ex:2
# def starPosition(array):
#     for i in range(len(array)):
#         if array[i]=="*":
#             index=i
#     return index

# list = eval(input())
# letter = str(input())
# result = starPosition(list)
# value  = True
# if result == 0 or result == 4:
#     value = False
# if letter == "r" and value:
#     list[result] = "0"
#     list[result+1] ="*"
# if letter == "l" and value:
#     list[result] = "0"
#     list[result-1] ="*"
# print(list)


# Ex: 3
# def findStarindex(array2D):
#     for ro in range(len(array2D)):
#         cols = array2D[ro]
#         for col in range(len(cols)):
#             if  cols[col] == "*":
#                 column = col
#                 row = ro
#     return row, column
        
# listOfarray2D = [["0","0", "0", "0", "0"],
#                 ["0","0", "0", "0", "0"],
#                 ["0","0", "0", "0", "0"],
#                 ["0","0", "0", "0", "0"],
#                 ["0","0", "0", "*", "0"]]
# letter = str(input())
# result=findStarindex(listOfarray2D)
# value = True
# if result[0] == 0 and letter.upper() == "U" or result[0] == 4 and letter.upper() == "D" or result[1] == 0 and letter.upper() == "L" or result[1] == 4 and letter.upper() == "R":
#     value = False
# if letter.upper() == "L" and value:
#     listOfarray2D[result[0]][result[1]-1] = "*"
#     listOfarray2D[result[0]][result[1]] = "0"
# elif letter.upper() == "R" and value:
#     listOfarray2D[result[0]][result[1]+1]  = "*"
#     listOfarray2D[result[0]][result[1]] = "0"
# elif letter.upper() == "U" and value:
#     listOfarray2D[result[0]-1][result[1]] = "*"
#     listOfarray2D[result[0]][result[1]] = "0"
# elif letter.upper() == "D" and value:
#     listOfarray2D[result[0]+1][result[1]] = "*"
#     listOfarray2D[result[0]][result[1]] = "0"
# print(listOfarray2D)
        

    



