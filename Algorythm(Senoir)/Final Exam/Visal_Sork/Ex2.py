def reverseString(text):
    word=""
    for i in range(len(text)):
        word+=text[-i-1]
    return word
        
        
array=eval(input())
newArray=[]
for arr in range(len(array)):
    newArray.insert(-arr,reverseString(array[arr]))
print(newArray)
    