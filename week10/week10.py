# myList=[76,92.3,"hello",True,4,76]
# print(myList)
# myList.append("apple")
# print(myList)
# myList.append(76)
# print(myList)
# myList.insert(3,"cat")
# print(myList)
# myList.insert(0,99)
# print(myList)
# print(myList.index("hello"))
# print(myList.count(76))
# myList.remove(76)
# print(myList)
# myList.pop(myList.index(True))
# ---------------------------------------------------------------------------
# def sumOfSquares(numbers):
#     sum = 0
#     for number in numbers:
#         sum += number ** 2
#     return sum
# numbers = [3,4,5]
# print(sumOfSquares(numbers))
# -----------------------------------------------------------------------
# def isEven(number):
#     even = 0
#     for i in number:
#         if i % 2 == 0:
#             even += 1
#     return even
# numbers = [3,4,5,8,4,2,5,346,5,756,7,54,]
# print(isEven(numbers))
# ------------------------------------------------------------------------------
# def countWords(words):
#     count = 0
#     for word in words:
#         if  len(word) == 5:
#             count+=1
#     return count
# words = ["ali","burak","murat","gül","sena"]
# print(countWords(words))
# ----------------------------------------------------------------------------
# def sumUntilEven(numbers):
#     sum = 0
#     for number in numbers:
#         if number % 2 == 0:
#             break
#         sum += number
#     return sum
# print(sumUntilEven([1,3,3,7,5,6,7,9]))
# ----------------------------------------------------------------------------
# def countWords(Words):
#     count = 0
#     for word in Words:
#         count +=1
#         if word == "sam":
#             break
#     return count
# words = ["burak","gül","sena","ali","mehmet","sam"]
# print(countWords(words))
# # ---------------------------------------------------------------------------
# def replace(s, old, new):
#     pieces = s.split(old)
#     print(pieces)
#     print(new.join(pieces))
#     return new.join(pieces)
# def test (actual,expected):
#     if actual == expected:
#         print("Passed!")
#     else:
#         print("Fail!")
# test(replace("Mississippi","i","I"),"MIssIssIppI")
# --------------------------------------------------------------------------------
def findMax (list):
    maxValue = list[0]
    for i in list:
        if i > maxValue:
            maxValue = i
    return maxValue
List=[3,2,1,4,5,10,32,7,15,31]
print(findMax(List))

