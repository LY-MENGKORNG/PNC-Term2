# For loop ways
# def containUpperCase(word):
#     isFindUpperCase = False
#     for char in word:
#         if char.upper() == char and char != " ":
#            isContainUpperCase = True
#     return isFindUpperCase

# While loop ways
def containUpperCase(word):
    isContainUpperCase = False
    i = 0
    while not isContainUpperCase and i < len(word):
        if word[i].upper() == word[i] and word[i] != " ":
           isContainUpperCase = True
        i += 1
    return isContainUpperCase


text = str(input("Enter word:"))

isContainUpperCase = containUpperCase(text)
result = ""
if isContainUpperCase:
    result = "VALID"
else:
    result = "INVALID"

print(result)