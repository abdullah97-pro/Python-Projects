# firstName = "Ali"
# age = 21
# marital_status = True
# fee = 50
# dob = "2005-05-20"

# print("FirstName: ",firstName)
# print("Age: ",age)
# print("Maried: ",marital_status)
# print("Fee: ",fee)
# print("DOB: ",dob)

# name = input("Enter your name: ")
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# result = num1 * num2
# print(name)
# print(result)

# x = 12
# y = 3

# result = x + y

# print(result)
# if result == 15:
#     print("Fifteen")

# if result != 15:
#     print("No Fifteen")

# if result > 14:
#     print("Greater then 14")

# if result != 15:
#     print(0)
# else:
#     print(1)

# areaCode = int(input("Enter Code: "))

# if areaCode == 90:
#     print("Turkey")
# elif areaCode == 91:
#     print("India")
# elif areaCode == 92:
#     print("Pakistan")
# elif areaCode == 93:
#     print("Afghanistan")
# else:
#     print("Try again !!!")

# age = int(input("Enter your age: "))
# verified = bool(input("Verify -> Yes = 1 / No = 0: "))

# # if age > 17 and verified == True:
# #     print("You have been selected!")
# # else:
# #     print("Try Next time...")

# if age > 17 or verified == True:
#     print("You have been selected!")
# else:
#     print("Try Next time...")

num1 = int(input("Enter number: "))

if num1 <= 800:
    print(num1 * 2)
elif num1 > 800 and num1 <= 1600:
    num2 = num1 - 800
    num1 = num1 - num2

    total = (num1 * 2) + (num2 * 3)

    print(total)
