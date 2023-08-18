def reverseString(word):
    newText = ""
    for i in range(len(word)):
        newText += word[len(word) - 1 - i]
    return newText

itemsList = eval(input("Enter list: "))

for item in itemsList:
    print("The reverse of " + item + " is " + reverseString(item))