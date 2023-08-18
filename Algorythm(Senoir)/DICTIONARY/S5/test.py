


# def newClass(dic1,dic2):
#     newKey=""
#     count=0
#     value=False
#     for key in dic2:
#         for key2 in dic1:
#             if key == key2:
#                 count+=1
#         if count==0:
#             newKey=key
#             newNb=dic2[key]
#             value=True
#         else:
#             count=0
#     return newKey, newNb, value
    

# for key in studentsDic1:
#     for key2 in studentsDic2:
#         if key == key2:
#             studentsDic1[key]=studentsDic1[key]+studentsDic2[key2]
# new=newClass(studentsDic1,studentsDic2)
# if new[2]:
#     studentsDic1[new[0]]=new[1]
# print(studentsDic1)
        
studentsDic1={"2021A":20,"2021B":30,"2021C":15}
studentsDic2={"2021A":15,"2021C":10,"2021D":99}


def newClass(dic1,dic2):
    newKey=""
    count=0
    value=False
    for key in dic2:
        for key2 in dic1:
            if key == key2:
                count+=1
        if count==0:
            newKey=key
            newNb=dic2[key]
            value=True
        else:
            count=0
    return newKey, newNb, value

for key in studentsDic1:
    for key2 in studentsDic2:
        if key == key2:
            studentsDic1[key]=studentsDic1[key]+studentsDic2[key2]
if newClass(studentsDic1,studentsDic2)[2]:
    studentsDic1[newClass(studentsDic1,studentsDic2)[0]]=newClass(studentsDic1,studentsDic2)[1]
print(studentsDic1)