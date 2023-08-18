# session1
# Ex:1
# def sum(array_of_number):
#     result = 0
#     for arr in array_of_number:
#         result += arr
#     return result 
# array_value = eval(input())
# print(sum(array_value))

# Ex:2
# def numberOfEight(array):
#     countEight= 0
#     for arr in array:
#         if arr == 7:
#             countEight+=1
#         toReturn=countEight
#     if countEight==0:
#         toReturn = -1
#     return toReturn
# array=eval(input())
# print(numberOfEight(array))

# Ex:3
# def finddrady(array):
#     indexofRaday = 0
#     for arr in range(len(array)):
#         if array[arr].upper()=="RADY":
#             indexofRaday = arr
#     return indexofRaday
# array = eval(input())
# print(finddrady(array))

# Ex:4
# def numberOfevenNumber(array):
#     countEven = 0
#     for arr in array:
#         if arr % 2==0:
#             countEven+=1
#     return countEven
# def numberOfoddNumber(array):
#     countOdd = 0
#     for arr in array:
#         if arr%2==1:
#             countOdd+=1
#     return countOdd
# number = eval(input())
# evenNumber = str(numberOfevenNumber(number))
# oddNumber =  str(numberOfoddNumber(number))
# print("EVEN:" +evenNumber+"\n"+"ODD:"+oddNumber)



# session2
# Ex:1
# def countNegNum(array):
#     Number_of_negative_value=0
#     for arr in array:
#         if arr < 0:
#             Number_of_negative_value+=1
#     return Number_of_negative_value
# number = eval(input())
# print("Number of negative value is: "+str(countNegNum(number)))

# Ex:2            NOT YET
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

# EX:3
# def getIndexOfNumberFive(array):
#     for arr in range(len(array)):
#         letter = array[arr]
#         if letter == 5 and isFound:
#             result = arr
#     return result     
# isFound = True
# number = eval(input())
# print("The First index of number five is: "+str(getIndexOfNumberFive(number)))

# Ex:4
# def sumOdd_EvenNumber(array):
#     sumOfEven = 0
#     sumOfOdd = 0
#     for arr in array:
#         if arr %2 ==0:
#             sumOfEven += arr
#         else:
#             sumOfOdd += arr
#     return [sumOfEven,sumOfOdd]
# number = eval(input())
# result = sumOdd_EvenNumber(number)
# print(result[1],result[0])

# Ex:5
# def replaceNumber(array):
#     for arr in range(len(array)):
#         if array[arr]== 9:
#             array[arr]=168
#     return array
# number = eval(input())
# print(replaceNumber(number))

# Ex:6
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



# session3
# Ex:1
# def isEqual(list1,list2):
#     letter = ""
#     letter2 = ""
#     for i in list1:
#         letter+=str(i)
#     for j in list2:
#         letter2+=str(j)
#     if letter == letter2:
#         value = True
#     else:
#         value = False
#     return value
# list1 = eval(input())
# list2= eval(input())
# result =isEqual(list1,list2)
# if result == True:
#     print("Equal")
# else:
#     print("Not Equal")

# Ex:2
# def isEqual(list1,list2):
#     isValue = True
#     for arr in range(len(list1)):
#         countNumber = 0
#         nbofArray1 = list1[arr]
#         if len(list1) == len(list2) and isValue:
#             for index in range(len(list2)):
#                 if nbofArray1 == list2[index]:
#                     countNumber += 1
#         if countNumber == 0:
#             isValue = False
#     return isValue
# list1=eval(input())
# list2=eval(input())
# result = isEqual(list1,list2)
# if result == True:
#     print("EQUAL")
# else:
#     print("NOT EQUAL")

# Ex:3
# def numberOfCompare(array):
#     result = 0
#     value = True
#     for i in range(len(number)-1):
#         if number[i+1] > number[i]:
#             result +=1
#     return result
# number=eval(input())
# print(numberOfCompare(number))

# Ex:4
# def sumFromTo(array):
#     result =0
#     if array[0] < array[1]:
#         value = True
#         nb = array[0]
#         nb2=array[1]
#     while nb <= nb2 and value:
#         result+=nb
#         nb+=1
#     return result
# number =eval(input())
# print(sumFromTo(number))

# Ex:5
# def sumBetweenNumber(array):
#     result =0
#     value = False
#     for i in range(len(array)):
#         text = array[i]
#         if text==2 and not value:
#             value=True
#         elif value and text!=2:
#             result += text
#         elif text==2:
#             value = False
#     return result
# array=eval(input())
# print(sumBetweenNumber(array))