def hasMonsterOnCell (monsterPosition, cellX, cellY):
    # Write your code here !
    for value in monsterPosition:
        if value[0] == cellY and value[1] ==cellX:
            return True
    return False

# MAIN CODE 
values = eval(input())

# Write your code here !
result = ""
for row in range(5):
    for col in range(5):
        if hasMonsterOnCell(values,row,col):
            result+="*"
        else:
            result+="0"
    result +="\n"
print(result)