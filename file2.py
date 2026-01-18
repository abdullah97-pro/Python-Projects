# # # # # # # # x = int(input("Enter your number1: "))
# # # # # # # # y = int(input("Enter your number2: "))
# # # # # # # # z = int(input("Enter your number3: "))

# # # # # # # # x = x + y
# # # # # # # # y = y - z
# # # # # # # # z = x + y * z

# # # # # # # # print(x)
# # # # # # # # print(y)
# # # # # # # # print(z)

# # # # # # # calc = eval(input("Enter math expression: "))
# # # # # # # print(calc)
# # # # # # # print(type(calc))
# # # # # # # x = True


# # # # # # import math 

# # # # # # # print(math.pow(2,10))
# # # # # # # print(math.pi)
# # # # # # # print(math.sqrt(25))

# # # # # # r = float(input("Enter radius: "))
# # # # # # area = math.pi * r * r
# # # # # # print("Area =", area)


# # # # # name = "Fanaven Technology"

# # # # # # print(name)
# # # # # # print(name[0])
# # # # # # print(name[4])
# # # # # # print(name[-1])

# # # # # # print(name[0:9])
# # # # # # print(name[3:])
# # # # # # print(name[:15])
# # # # # # print(name[:])
# # # # # # print(name[5:-1])
# # # # # # print(name[-14:-2])

# # # # # print(name[::-1])

# # # # word = input("Enter string: ")

# # # # if word == word[::-1]:
# # # #     print("Palindrome")
# # # # else:
# # # #     print("Not Palindrome")

# # # # age = 16.5 # statment

# # # # if age < 17: 
# # # #     age = f"{age}"
# # # #     y = "You are young and you are "+age+" years old"
# # # #     print(y)
# # # #     print(type(age))

# # # # age = 16.5 

# # # # if age > 17:
# # # #     print("You are verified")
# # # # else:
# # # #     if (17 - age) > 1:
# # # #         print("Still need to wait for",(17 - age),"yrs")
# # # #     else:
# # # #         x = 17 - age
# # # #         # if x == 1:
# # # #         #     x = x / 12
# # # #         #     x = f"{x}"

# # # #         #     x = (x == "0.08333333333333333")



# # # #             # print("Still need to wait for",x,"month")
# # # #         for i in range(x,13):
# # # #             pass
# # # #         print("Still need to wait for",i,"month")




# # # age = 16.5

# # # if age >= 17:
# # #     print("You are verified")
# # # else:
# # #     remaining_years = 17 - age

# # #     if remaining_years >= 1:
# # #         print("Still need to wait for", round(remaining_years, 1), "years")
# # #     else:
# # #         remaining_months = int(remaining_years * 12)
# # #         print("Still need to wait for", remaining_months, "months")


# # names = ["RAM","CPU","Monitor","SSD"] #list
# # # print(names)

# # # names[1] = 22
# # # print(names)

# # names.append("SSD NVMe")
# # names.insert(2,"Share Grahpic")
# # names.remove("Monitor")
# # print(names)

# # print(names[:3])
# # print(names[0:4])
# # print(names[-5:])

# # del names
# # print(names)


# # squares = [x**2 for x in range(5)]
# # print(squares)

# # even = [x for x in range(10) if x % 2 == 0]
# # print(even)

# a = [1,2,3]
# b = a
# c = [1,2,3]

# # print(a == b)
# # print(b == c)
# # print(c == a)

# # print(a is b)
# # print(b is not c)
# # print(c is a)

# # print(2 not in c)
# # print(2 in b)
# # print(2 in a)

# name = "Fanaven Technology"
# # a = 2
# # n = 3
# # e = 2



# tupleCode = (1,2,3)
# # tupleCode[0] = 11
# print(tupleCode)


my_dict = { (1, 2): "a pair", (3, 4): "another", 'phone': "0781234567" }
print(my_dict['phone']) 
