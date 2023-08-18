# Ex:1
# def greaterNumber(array):
#     value = False
#     for arr in array:
#         if arr > 10 and arr <= 20 and arr != 15:
#             value = True
#     return value
# listOfarray = eval(input())
# result = greaterNumber(listOfarray)
# print(result)


# Ex:2
# def ascendingNumber(array):
#     value = True
#     for i in range(1,len(array)):
#         if array[i-1] > array[i]:
#             value = False
#     return value        
        
# listOfarray = eval(input())
# result = "ERROR"
# if ascendingNumber(listOfarray):
#     result = "ASCENDING"
# print(result)



# Ex:3
# listOfbooks=[
#             {'name': "Jackma", 'status': True},
#             {'name': "Kolap baelen", 'status': False},
#             {'name': "Tom Teav", 'status': False},
#             {'name': "Elon mask", 'status': False},
#             {'name' :"Leadership", 'status' : True}
#             ]
# count=0
# for dict in listOfbooks:
#     if dict["status"] == True:
#         count+=1
# print(count)

# Ex:4
def ingredient(weNeed,kitchent):
    for dict in kitchent:
        if weNeed["ingredient"] == dict["ingredient"]:
            if weNeed["quantity"] < dict["quantity"]:
                return True
            else:
                return False
ingredientsNeed=[
                {"ingredient" : "rice","quantity" : 100},
                {"ingredient" : "beef", "quantity" : 300}
                ]

ingredientsKitchen=[
                    {"ingredient" : "banana", "quantity" : 100},
                    {"ingredient" : "beef", "quantity" : 200},
                    {"ingredient" : "rice", "quantity" : 300}
                    ]
result = True
for dict in ingredientsNeed:
    if not ingredient(dict,ingredientsKitchen):
        result=False
print(result)

# students={"2021A": 10, "2021B": 20, "2021C": 30}
# newNb=2
# classroom="2021C"
# for key in students:
#     if classroom==key:
#         students[key]+=newNb
# if classroom not in students:
#     students[classroom]=newNb
# print(students) 

        


