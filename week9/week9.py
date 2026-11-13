# --------------1-----------------------
# def isOdd(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# print(isOdd(5))
# ----------------2----------------------
# def isLeapYear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
# print(isLeapYear(2026))
# ------------------3---------------------
# def printTriangularNumber(n):
#     total = 0
#     for i in range(1, n+1):
#         total = total + i
#     print(total)
# printTriangularNumber(5)
# printTriangularNumber(6)
# printTriangularNumber(10)
#-------------------4------------------------
# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
# print(isPrime(87))
# ---------------------5------------------------
# def reverse (s):
#     result = ""
#     for chr in s:
#         result = chr + result
#     return result
# print(reverse("hello"))
#
#
# def reeverseSlice(s):
#     return s[::-1]
# print(reeverseSlice("hello"))
# ---------------------6-------------------------
# def removeAll(sub,s):
#     return s.replace(sub,"X")
# print(removeAll("an","banana"))
# print(removeAll("l","HelloWorld"))
# ---------------------7---------------------------
# def subtitute(message,key):
#     alphabet = "abcdefgğhıijklmnoöprsştuüvyz"
#     result = ""
#     for char in message:
#         index = alphabet.find(char.lower())
#         if index != -1:
#             result = result + char
#         elif char.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
# key = "hsajowpğdaweoqmvödşsldeqeramx"
# print(len(key))
# print(subtitute("hello,world",key))
#-----------------------8-----------------------------
# def removeDups(s):
#     result = ""
#     for char in s:
#         if char not in result:
#             result += char
#     return result
# print(removeDups("karmakarmaşık"))
