def averageScore(scores):
    sum = 0
    for score in scores:
        sum += score
    return sum / len(scores)

numberOfStudents = int(input("Number of students: "))
average = 0
total = 0
for i in range(numberOfStudents):
    topicScore = eval(input("Score list " + str(i) + ": "))
    total += averageScore(topicScore)
average  = int(total / numberOfStudents)
print(average)