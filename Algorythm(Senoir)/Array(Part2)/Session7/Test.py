# _______________Ex:3_____________
# array = eval(input())
# allInRange= True
# for number in array:
#     if number < 5 or number >10:
#         allInRange = False
# print(allInRange)

# ____________Ex:2________________
# def createRow(number):
#     result = ""
#     for i in range(number):
#         result += str(number)
#     return result
# array=eval(input())
# result=""
# for maxNumber in array:
#     newRow = createRow(maxNumber)
#     result += newRow +"\n"
# print(result)

# __________Ex: 3______________
# list1 = eval(input())
# list2 = eval(input())
# list3 = eval(input())
# sumList1 = 0
# sumList2 = 0
# sumList3 = 0
# for i in list1:
#     sumList1+=i
# for j in list2:
#     sumList2+=j
# for k in list3:
#     sumList3+=k
# if sumList1 > sumList2 and sumList1 > sumList3:
#     print(list1)
# elif sumList2 > sumList1 and sumList2 > sumList3:
#     print(list2)
# elif sumList3 > sumList1 and sumList3 > sumList2:
#     print(list3)
# elif sumList1 == sumList2 or sumList1 == sumList3 or sumList2 == sumList3:
#     print([])

# __________Comment the block____________
# ___________Ex:2______________
# array = [1,2,4,-1,-6,-4]
# list = []
# for i in range(len(array)):
#     if array[i] < 0:
#         list.append(array[i])
# print(list)
# ______Insert_________
# list= [2,3,4,5,"me"]
# list.insert(3, "you")
# print(list)
# _______--Remove using index___________        _______Remove using specificed name___________
# list= [2,3,4,5,"me"]                          list=[1,2,3]
# list.pop(3)                                   list.remove(2)
# print(list)                                   print(list)


# ___________Ex:4____________
# for i in range(3):
#     fruitName  = str(input())
#     fruitPrice = int(input())
#     newFruitDict = {"name": fruitName, "price": fruitPrice}
# fruits=newFruitDict
# print(fruits)


# _________Ex: 5________________
# fruits = {"name": "apple","price":10},{"name":"orange","price":20},{"name": "pineapple","price":50}
# money = int(input())
# canBuy=[]
# for fruit in fruits:
#     if fruit["price"] < money:
#         canBuy.append(fruit["name"])
# print(canBuy)


# ៌៌៌៌៌៌៌៌______________Ex: 6______________
# array = eval(input())
# newArray = []
# for i in range(len(array)):
#     newArray.append(array[-i-1])
# print(newArray)



        
    
