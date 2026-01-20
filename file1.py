# # # firstName = "Ali"
# # # age = 21
# # # marital_status = True
# # # fee = 50
# # # dob = "2005-05-20"

# # # print("FirstName: ",firstName)
# # # print("Age: ",age)
# # # print("Maried: ",marital_status)
# # # print("Fee: ",fee)
# # # print("DOB: ",dob)

# # # name = input("Enter your name: ")
# # # num1 = int(input("Enter number 1: "))
# # # num2 = int(input("Enter number 2: "))
# # # result = num1 * num2
# # # print(name)
# # # print(result)

# # # x = 12
# # # y = 3

# # # result = x + y

# # # print(result)
# # # if result == 15:
# # #     print("Fifteen")

# # # if result != 15:
# # #     print("No Fifteen")

# # # if result > 14:
# # #     print("Greater then 14")

# # # if result != 15:
# # #     print(0)
# # # else:
# # #     print(1)

# # # areaCode = int(input("Enter Code: "))

# # # if areaCode == 90:
# # #     print("Turkey")
# # # elif areaCode == 91:
# # #     print("India")
# # # elif areaCode == 92:
# # #     print("Pakistan")
# # # elif areaCode == 93:
# # #     print("Afghanistan")
# # # else:
# # #     print("Try again !!!")

# # # age = int(input("Enter your age: "))
# # # verified = bool(input("Verify -> Yes = 1 / No = 0: "))

# # # # if age > 17 and verified == True:
# # # #     print("You have been selected!")
# # # # else:
# # # #     print("Try Next time...")

# # # if age > 17 or verified == True:
# # #     print("You have been selected!")
# # # else:
# # #     print("Try Next time...")

# # num1 = int(input("Enter number: "))

# # if num1 <= 800:
# #     print(num1 * 2)
# # elif num1 > 800 and num1 <= 1600:
# #     num2 = num1 - 800
# #     num1 = num1 - num2

# #     total = (num1 * 2) + (num2 * 3)
# #     print(total)

# # elif num1 > 1600 and num1 <= 2800:
# #     x2 = 800 * 2
# #     x3 = 800 * 3
# #     num1 = num1 - 1600

# #     total = x2+x3+(num1 * 5)
# #     print(total)
# # else:
# #     x2 = 800 * 2
# #     x3 = 800 * 3
# #     x5 = 1200 * 5
# #     num1 = num1 - 2800

# #     total = x2+x3+x5+(num1 * 7)
# #     print(total)
    

# # x = 10
# # while x > 1:
    
# #     # if x % 2 != 0:
# #     #     print(x)
# #     # x+=1
# #     print(x)
# #     x-=1

# # x = 1
# # while x < 20:

# #     if x == 10:
# #         continue
# #     print(x)
# #     x+=1


# # for x in range(2,20,2):
# #     if (x == 5) or (x == 6):
# #         continue
# #     print(x)

# # for x in range(5):
    
# #     if x == 3:
# #         pass


# # while True:
# #     num1 = float(input("Enter number1: "))
# #     ope = input("Enter operator: +, -, *. /, % : ")
# #     num2 = float(input("Enter number2: "))

# #     if ope == "+":
# #         print("Result: ", (num1 + num2))
# #     elif ope == "-":
# #         print("Result: ", (num1 - num2))
# #     elif ope == "*":
# #         print("Result: ", (num1 * num2))
# #     elif ope == "/":
# #         print("Result: ", (num1 / num2))
# #     elif ope == "%":
# #         print("Result: ", (num1 % num2))
# #     else:
# #         print("Try again!!!")

# # y = int(input("Enter number for multiplication: "))
# # len = int(input("Enter number for length of multiplication: "))

# # for x in range(1,len+1):
# #     print(y," * ",x," = ",x * y)









# # def greet(msg):
# #     print(msg)

# # greet("Good Afternoon")


# # def afternoon():
# #     print("Hey! I am studying Python at Fanaven Technology")


# # # with parameter with return
# # # without parameter
# # # with return
# # # without return


# # def sum(x):
# #     if x == 5:
# #         return 0
# #     return x

# # print(sum(12))

# # afternoon()



# def sum(x,y):
#     msg = "Result: "
#     return msg,x + y

# def minus(x,y):
#     return x - y

# def mult(x,y):
#     return x * y

# def divide(x,y):
#     return x / y

# num1 = int(input("Enter number1: "))
# ope = input("Enter operator +,-,*,/ : ")
# num2 = int(input("Enter number2: "))

# if ope == "+":
#     print(sum(num1,num2))
# elif ope == "-":
#     print(minus(num1,num2))
# elif ope == "*":
#     print(mult(num1,num2))
# elif ope == "/":
#     print(divide(num1,num2))
# else:
#     print("Try next time!")


# student = {
#     "name":"Ali",
#     "age": 20,
#     "dob": "2000/01/01",
#     "email": "ali@gmail.com",
#     "fee": 100
# }
# # print(student)
# # print(student.get("fee","Not found"))
# # print(student.keys())
# # print(student.values())
# # print(student.items())
# student.update({"gender":"Male"})

# # print(student)
# student.pop("fee")

# print(student.values())


student = {
    "ali": {"grade":70,"gender":"male","fee":100},
    "dawood": {"grade":70,"gender":"male","fee":110},
    "seyar": {"grade":70,"gender":"male","fee":120}
}

print(student["ali"]["fee"])
print(student["dawood"]["fee"])
print(student["seyar"]["fee"])
