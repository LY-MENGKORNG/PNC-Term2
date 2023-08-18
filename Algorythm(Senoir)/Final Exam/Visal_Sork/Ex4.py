arrayOfsubjects=eval(input())
arrayOfteachers=eval(input())
teacherLastname=""
countTeacher=0

for dict1 in arrayOfsubjects:
    for dict2 in arrayOfteachers:
        if dict1["subject"] == "algorithm" and str(dict1["teacher-id"]) == dict2["teacher-id"]:
            teacherLastname+=dict2["last-name"]+" "
            countTeacher+=1
if countTeacher != 0:
    print(teacherLastname)
else:
    print("No teacher in algorithm subject")
    
