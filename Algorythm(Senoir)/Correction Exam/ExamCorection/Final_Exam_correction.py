# _____ Exercise 1 _____ #

# numberOfLoop = 5
# toPrint = "WIN"
# for n in range(numberOfLoop):
#     value = int(input())
#     if value <10 or value > 30:
#         toPrint = "LOST"
# print(toPrint)


# _____ Exercise 2 _____ #

# isWin = False
# sumValue = 0
# toPrint = "WIN"
# while not isWin and sumValue < 20:
#     value = int(input())
#     if(value != 10 and value != 12):
#         sumValue += value
# if sumValue > 20:
#     toPrint = "LOST"
# print(toPrint)


# _____ Exercise 3 _____ #

# countLoop = 3
# while countLoop>0:
#     number = int(input())
#     countLoop -= 1
#     if countLoop == 0 and number != 68 :
#         toPrint = "Lost"
#     elif number != 68 :
#         toPrint = "try again!"
#     else:
#         countLoop = 0
#         toPrint = "WIN"
#     print(toPrint)


# _____ Exercise 4 _____ #

# *** note area *** # 
# cha = character 
#*note* count is a python function that we can used it to count something inside itself


# ***** first way ***** #
# word = str(input())
# countA = 0
# countDollar = 0
# for cha in word:
#     if cha == "A":
#         countA += 1
#     elif cha == "$":
#         countDollar += 1

# if countDollar ==2:
#     toPrint = 20
# elif countDollar == 1 and countA == 0:
#     toPrint = 10
# elif countA == 1 and countDollar == 0: 
#     toPrint = 30
# else:
#     toPrint = 0
# print(toPrint)

# ***** second way ***** #

# word = str(input())
# countA = word.count("A")  #*note*
# countDollar = word.count("$")  #*note*
# print(countA, countDollar)

# if countA == 1 and countDollar == 0:      #RULE 1
#     toPrint = 30
# elif countDollar ==2:                     #RULE 2
#     toPrint = 20
# elif countDollar == 1 and countA == 0:    #RULE 3
#     toPrint = 10
# else:
#     toPrint = 0
# print(toPrint)

