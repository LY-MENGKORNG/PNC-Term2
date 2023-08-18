# ____________________Ex: 1_________________
# def countNegNum(array):
#     Number_of_negative_value=0
#     for arr in array:
#         if arr < 0:
#             Number_of_negative_value+=1
#     return Number_of_negative_value
# number = eval(input())
# print("Number of negative value is: "+str(countNegNum(number)))


#___________EX: 2________________
# def getIndexMinNumber(array):
#     m = array[0]
#     for i in range(len(array)):
#         letter = array[i]
#         if letter < m:
#             m = letter
#             result = i
#     return result
# array = eval(input())
# print(getIndexMinNumber(array))

# _____________Ex: 3________________-
# def getIndexOfNumberFive(array):
#     for arr in range(len(array)):
#         letter = array[arr]
#         if letter == 5 and isFound:
#             result = arr
#     return result     
# isFound = True
# number = eval(input())
# print("The First index of number five is: "+str(getIndexOfNumberFive(number)))



# _______________Ex: 4______________
# def sumOdd_EvenNumber(array):
#     sumOfEven = 0
#     sumOfOdd = 0
#     for arr in array:
#         if arr %2 ==0:
#             sumOfEven +=arr
#         else:
#             sumOfOdd+=arr
#     return [sumOfEven,sumOfOdd]
# number = [1,2,3,4]
# result = sumOdd_EvenNumber(number)
# print(result[1],result[0])


# ___________________Ex: 5_________________
# def replaceNumber(array):
#     for arr in range(len(array)):
#         if array[arr]== 9:
#             array[arr]=168
#     return array
# number = eval(input())
# print(replaceNumber(number))


# _____________Ex: 6_______________________
# def replaceLetter(array):
#     for i in range(len(array)):
#         letter = ""
#         for index in range(len(array[i])):
#             item = array[i]
#             if item[index] == "a":
#                 letter += "$"
#             else:
#                 letter += item[index]
#         array[i]=letter
#     return array
# arrayName = eval(input())
# print(replaceLetter(arrayName))
                
            
                
                
            