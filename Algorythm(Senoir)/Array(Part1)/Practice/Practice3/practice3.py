
# ____________________Ex: 1_____________________
# def isEqual(list1,list2):
#     letter = ""
#     letter2=""
#     for i in list1:
#         letter+=str(i)
#     for j in list2:
#         letter2+=str(j)
#     if letter == letter2:
#         value = True
#     else:
#         value = False
#     return value
# list1 =[1,2,3]
# list2=[1,2,4]
# result =isEqual(list1,list2)
# if result == True:
#     print("Equal")
# else:
#     print("Not Equal")

# ____________Ex: 2__________
# def isEqual(list1,list2):
#     isValue = True
#     for arr in range(len(list1)):
#         countNumber = 0
#         nbofArray = list1[arr]
#         if len(list1) == len(list2) and isValue:
#             for index in range(len(list2)):
#                 if nbofArray == list2[index]:
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


# __________Ex: 3__________
# def numberOfCompare(array):
#     result = 0
#     value = True
#     for i in range(len(number)-1):
#         if number[i+1] > number[i]:
#             result +=1
#     return result
# number=eval(input())
# print(numberOfCompare(number))

# ________Ex: 4_________
# def sumFromTo(array):
#     result =0
#     if array[0]<array[1]:
#         value = True
#         nb = array[0]
#         nb2=array[1]
#     while nb <= nb2 and value:
#         result+=nb
#         nb+=1
#     return result
# number =eval(input())
# print(sumFromTo(number))

# ________________Ex: 5___________________
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