array=eval(input())
count=0
failStudent=""
for dict in array:
    if dict["subject"]=="Algorithm" and dict["score"]<50:
        count+=1
        failStudent+=dict["name"]+ " "
if count==0:
    print(count,"student failed algorithm")
elif count==1:
    print(count,"student failed algorithm:",failStudent)
else:
    print(count,"students failed algorithm:",failStudent)