# _______________Question: 1_____________________
# def sum(array_of_number):
#     result = 0
#     for arr in array_of_number:
#         result += arr
#     return result 
# array_value = eval(input())
# print(sum(array_value))
    
    
# _________________Question: 2_________________________
# def numberOfEight(array):
#     result = 0
#     for arr in array:
#         if arr==7:
#             result+=1
#         elif 7 not in array:
#             result =-1
#     return result
# number = eval(input())
# print(numberOfEight(number))
#    ____________other way____________
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
    
    
# _________________Question: 3_________________________
# Question:3
# def finddrady(array):
#     indexofRaday = 0
#     for arr in range(len(array)):
#         if array[arr].upper()=="RADY":
#             indexofRaday = arr
#     return indexofRaday
# array = ["me", "you", "RADY", "rady"]
# print(finddrady(array))


# _________________Question: 4_________________________
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

            