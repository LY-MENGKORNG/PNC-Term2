personsInRoom = eval(input())      # it's an array 2D !
newPersonRow = int(input())        # row of the new person to add
newPersonColumn = int(input())     # column of the new person to add

def findPeople(array2D):
    peoplePosition = []
    for row in range(len(array2D)):
        for col in range(len(array2D[row])):
            if array2D[row][col] == 1 :
                peoplePosition.append([row,col])
    return peoplePosition

peopleInRoom = findPeople(personsInRoom);
if len(peopleInRoom) >=3:
    print("CANNOT ADD")
else:
    isCanAdd = True
    for value in peopleInRoom:
        if value[0] == newPersonRow and value[1] == newPersonColumn:
            isCanAdd = False
    if isCanAdd:
        print("CAN ADD")
    else:
        print("CANNOT ADD")