#%% Minimum number 
# def computeMin(number1, number2):
#     if number1 < number2:
#         return number1
#     else:
#         return number2
# result = computeMin(6,5)
# print(result)
# %% ​​Name
# def myName(name):
#     print("My school's name is:" + name)
#     print("I like my school so much")
#     print("I want to go home")
# myName(" PNC")

# %% Exchange money
# number = int(input())
# def ExchangeDollarToKhmer(number):
#     return number* 4000
# print(ExchangeDollarToKhmer(number))
# print(ExchangeDollarToKhmer(int(input())))

# %% rectangle of "X"
# number = int(input())
# def rectangle(number):
#     result = ""
#     for i in range(number):
#         for i in range(number):
#             result += "X" 
#         result += "\n"
#     return result
# print(rectangle(number))
        
# %% Count the number of "X"
# string=str(input())
# def countLetterX(string):
#     countX = 0
#     for i in range(len(string)):
#         if string[i] == "X":
#             countX += 1
#     return countX
# print(countLetterX(string))

# %%

array2D=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
newArray =array2D[0]
result =[]
number=0
for i in range(1,len(array2D)):
    for j in range(len(array2D[i])):
        number=newArray[i]+array2D[j][i]
    result.append(number)
    # newArray.append(number)
    number=0
print(result)
        

