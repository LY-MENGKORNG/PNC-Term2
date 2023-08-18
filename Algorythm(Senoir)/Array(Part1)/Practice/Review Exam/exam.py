# ____________Ex: 1__________
# def toContains(word,letter):
#     value = False
#     for i in range(len(word)):
#         if  word[i].lower()==letter.lower():
#             value = True
#     return value
# word=str(input())
# letter = str(input())
# isFound = toContains(word,letter)
# if isFound == True:
#     result = "Valid"
# else:
#     result = "Not Valid"
# print(result)

# ________Ex: 2______________
# def toReverse(word):
#     new_word=""
#     for i in range(len(word)):
#         new_word+=word[-i-1]
#     return new_word
# word = str(input())
# print(toReverse(word))


# _______________Ex: 3______________
# def multiplyArray(array):
#     result = 1
#     for arr in array:
#         result *= arr
#     return result 
# number = eval(input())
# print(multiplyArray(number))

# ____________Ex: 4___________
# def countChar(array,letter):
#     result = 0
#     for arr in range(len(array)):
#         for index in range(len(array[arr])):
#             text = array[arr]
#             if text[index].upper()==letter.upper():
#                 result+=1
#     return result 
# array=eval(input())
# letter=str(input())
# print(countChar(array,letter))

# _________Ex: 5___________
# def Average(array):
#     total = 0
#     numberOfarray =0
#     while array[0]<=array[1]:
#         total += array[0]
#         array[0]+=1
#         numberOfarray+=1
#     result =total / numberOfarray
#     return result
# array=[8,15]    
# print(Average(array))
        
            

    
