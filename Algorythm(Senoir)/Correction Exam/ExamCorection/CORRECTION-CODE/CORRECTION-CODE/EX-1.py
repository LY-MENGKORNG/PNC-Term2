listPeople = eval(input("Enter a list of people: "))

for i in range(len(listPeople)) :
    count = 0
    names = listPeople[i]
    for j in range(len(names)):
        if names[j] == "A" or names[j] == "a":
            count += 1
    print("Number of A in " + str(names) + " is " + str(count))