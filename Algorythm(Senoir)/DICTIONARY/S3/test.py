
# Ex:1
# classroom={"2021A":20,"2021B":30,"2021C":15}
# if len(classroom) !=0:
#     for key in classroom:
#         print("Class",key,"has",classroom[key],"students")
# else:
#     print("No class assigned!")





# Ex2:
def material(key):
    if key["quality"] == 'Good':
        return key["quantity"]*key["retail_price"]
    else:
        return 0
        
materials = [
	{"name": 'Computer', "quantity": 20, "retail_price": 400, "quality": 'Good'},
	{"name": 'Computer', "quantity": 10, "retail_price": 200, "quality": 'Not good'},
	{"name": 'Monitor', "quantity": 20, "retail_price": 1000, "quality": 'Not good'},
	{"name": 'Keyboard', "quantity": 10, "retail_price": 150, "quality": 'Good'},
	{"name": 'Speaker', "quantity": 5, "retail_price": 50, "quality": 'Good'}
]

total=0
for dict in materials:
    total+=material(dict)
print(total)




# Ex:3
# def lowStudent(student,room):
#     if student['class'] == room:
#         return student['score']



# array=[
#         {'name':'HIM', 'class':'A', 'score':90},
#         {'name':'Bopha', 'class':'A', 'score':40},
#         {'name':'Tesla', 'class':'A', 'score':80},
#         {'name':'Kunthea', 'class':'B', 'score':100},
#         {'name':'Kolap', 'class':'B', 'score':90},
#         {'name':'Vanna', 'class':'B', 'score':70},
#         {'name':'Chompey', 'class':'C', 'score':50},
#         {'name':'Romchong', 'class':'C', 'score':90},
#     ]

# classroom="B"
# isFound=True
# name=""
# for dict in array:
#     if dict['class'] == classroom and isFound:
#         score= dict['score']
#         name=dict['name']
#         isFound=False
#     elif dict['class'] == classroom and not isFound:
#         if score > dict['score']:
#             name=dict['name']
#             score=dict['score']
# print(name)
    
    
    
    
    








