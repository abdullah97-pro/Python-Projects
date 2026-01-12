# # # # x = int(input("Enter your number1: "))
# # # # y = int(input("Enter your number2: "))
# # # # z = int(input("Enter your number3: "))

# # # # x = x + y
# # # # y = y - z
# # # # z = x + y * z

# # # # print(x)
# # # # print(y)
# # # # print(z)

# # # calc = eval(input("Enter math expression: "))
# # # print(calc)
# # # print(type(calc))
# # # x = True


# # import math 

# # # print(math.pow(2,10))
# # # print(math.pi)
# # # print(math.sqrt(25))

# # r = float(input("Enter radius: "))
# # area = math.pi * r * r
# # print("Area =", area)


# name = "Fanaven Technology"

# # print(name)
# # print(name[0])
# # print(name[4])
# # print(name[-1])

# # print(name[0:9])
# # print(name[3:])
# # print(name[:15])
# # print(name[:])
# # print(name[5:-1])
# # print(name[-14:-2])

# print(name[::-1])

word = input("Enter string: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

