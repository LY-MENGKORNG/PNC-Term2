def findA(name):
    Counta=0
    for i in name:
        if i == "a":
            Counta+=1
    return Counta


nameList=eval(input())
newNameList=[]
for arr in nameList:
    if findA(arr) == 2:
        newNameList.append(arr)
print(newNameList)