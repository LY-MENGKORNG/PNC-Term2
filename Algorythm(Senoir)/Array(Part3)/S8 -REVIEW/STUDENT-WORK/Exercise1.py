# case 1 :
sourceArray=eval(input())
result=[]
for row in range(len(sourceArray[0])):
    sum=0
    for col in range(len(sourceArray)):
        sum+=sourceArray[col][row]
    result.append(sum)
    
print(result)
