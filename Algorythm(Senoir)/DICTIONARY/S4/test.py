# Ex:1
# classrooms={"2021A":20,"2021B":30,"2021C":15}
# nbOfstudent=int(input("number of student:"))
# classroomAdd=str(input("Class:"))
# count=0
# for key in classrooms:
#     if classroomAdd==key:
#         count=1
# if count==0:
#     classrooms[classroomAdd]=0
# for key in classrooms:
#     if key == classroomAdd:
#         print("Class",key,"has",classrooms[key]+nbOfstudent,"students")
#     else:
#         print("Class",key,"has",classrooms[key],"students")

  
        
     
# Ex:2
# def teacherList(teacher):
#     total=0
#     for key in teacher:
#         total+=teacher[key]
#     return total

# teachers=eval(input())
# result="No teacher here!"
# if teachers != {}:
#     result=teacherList(teachers) / len(teachers)
# print(result)





# Ex:3
# def teacherList(teacher):
#     total=0
#     for key in teacher:
#         total+=teacher[key]
#     return total
    
# teachers=eval(input())
# result="No teacher here!"
# if teachers != {}:
#     result=teacherList(teachers) / len(teachers)
# print(result)



# <-----Quiz------>
# dict={"class":{"student":{"name":"Mike","mark":{"physic":70,"history":80}}}}
# for key in dict:
#     dict2=dict[key]
#     for key2 in dict2:
#         print(dict2[key2]["mark"]["history"])


# studentsData =  [
#                 {"name":"Bun","score":90},
#                 {"name":"sal","score":75},
#                 {"name":"me","score":95},
#                 ]
# studentScore=studentsData[0]["score"]
# studentName=studentsData[0]["name"]
# students="All student is 75"
# for i in range(1,len(studentsData)):
#     if studentsData[i]["score"] > studentScore:
#         studentName=studentsData[i]["name"]
# print(studentName)
# for dic in studentsData:
#     if dic["score"] < 75:
#         students=""
# print(students)
    
    

            
        
    

