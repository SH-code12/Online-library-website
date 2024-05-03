print("Eng/Shahd Elnassag")

from math import *  # library

# this is declar variable name String

# name = "Learn python"

# a = "Shahd Mohamed Elnassag"


# x = []

# print("You "+ name +" Now")

# print("Shahd\nMohamed")

# print(name[0:6])

# print(name.upper())

# print(name.lower())

# print(name.split(" ",0))

# print(name1.index("h"))

# print(len(name))

# print(len(a))

# print(a.replace("Mohamed" , "M"))

# Numbers

# print(3^2)

# print(type(9j))  # Type --> complex

# print(str(5*5) + " Years")

# print(round(7.6))
# print(floor(7.9))
# print(ceil(7.1))

# print(pow(3,3))

# name = input("Enter your name: ")

# pross = input(" 1.sum(+) \n 2.Max \n 3.Min \n 4.Substract(-) \n 5.Multiple(*) \n 6.power(x^y)")

# num1 =input("Enter num1: ")

# num2 =input("Enter num2: ")
# sumtion = (float(num1) + float(num2))

# print( "Welcome,"+ name + " Your Sumtion = "+ str(sumtion))

#List and its Methods

# lista = ["Shahd" , 100 , True , [1,2,3,[4,5]]]

# lista[2] = False   # change Values

# print(lista)
# print(lista[3])

# print(lista[3][3])

# print(lista[3][3][1])


# x = [1,2,3]

# y = [5 , 10 , 12]

# x.append(4)

# x.insert(1,5)

# x.extend(y)

# print(x)

# x.sort( reverse=True)

# x.remove(12)

#x.clear()

# print(x)

#Tuples ()  Not allowed to change any values

# tuples = (1,2,3)

# print(tuples)

#Dictionary {}

# info = {
    
#     "name":"Shahd",
#     "age" : 20,
#     "City" : "Cairo"
# }

# print(info["City"])

# print(info.get("id","Not Found"))

#Set and its Methods

# myset = {"Shahd",20,"Cairo"}
# print(myset)

# a = {1 ,2 ,5}
# b = {6,7,8}

# print(a.union(b))

# a.add(6)
# print(a)

# print(a|b)

# a.remove(6)
# print(a)

# b.add(15)
# print(b)

# b.discard(20)
# print(b)

# b.discard(15)
# print(b)

# a.clear()
# print(a)

#Functions

# def myfun(name):
#     print("My name is " + name)

# def calc(num1 , num2):
#     result = num1 + num2
#     return result

# print(calc(15 , 20))
# myfun("Shahd")


# def calc(age):
#     AgeDay = float(age) * 365
#     return AgeDay
    
# age = input("Enter Your age in years: ")

# print( "Your age "+str(calc(age)) +" Dayes")

# if 

# name = input("Enter Your name: ")
# password = int(input("Enter Your Passwoed: "))

# if name == "shahd" and password == 12345:
#     print("Correct Name and Password")
    
# elif name == "shahd" and password != 12345:
#     print("Incorrect password")
# elif name != "shahd" and password == 12345:
#     print("Incorrect Name")
# else:
#     print("Incorrect Name and Password")

# grade = int(input("Enter your Grade: "))

# if grade >= 95 and grade <= 100:
#     print("You Got: A+")
# elif grade >= 90 and grade < 95:
#     print("You Got: A")
# elif grade >= 80 and grade < 90:
#     print("You Got: B+")
# elif grade >= 75 and grade < 80:
#     print("You Got: B")
# elif grade >= 70 and grade < 75:
#     print("You Got: C+")
# elif grade >= 65 and grade < 70:
#     print("You Got: C")
# elif grade >= 60 and grade < 65:
#     print("You Got: D+")
# elif grade >= 50 and grade < 60:
#     print("You Got: D")
# else:
#         print("You Fail")

#loops

# i = 1
# while(i<=10):
#     print(i)
#     i +=1 

# answer = "Cairo"
# ans_user = ""

# i = 3
# while(answer != ans_user and i>=1):
#     ans_user = input("What is Capital of Egypt? ")
#     # print("Incorrect answer,Try again")
#     i -= 1
#     if answer == ans_user:
#         print("You Win ^_^")
#         break
#     elif i == 0 and answer != ans_user:
#         print("You lose")
#     else:
#         print("Try again,Remain "+str(i)+" chance")
#         continue

# for name in "shahd":
#     print(name)

# mylist = ["php ","css","java ","JS"]

# for i in mylist:
#     print(i)
# name = "shahd"
# for i in range(len(mylist)):
#     print(mylist[i])

# info = {
#     "name":"Shahd",
#     "age": "20",
#     "city":"cairo"
# }
#print values of dictionaty
# for x in info:
#     print(info[x])

# Try and except


# try:
#     num = int(input("Enter number: "))
#     print(num)
#     a = 1/0 
# except ZeroDivisionError as error:
#     # print("Not valid to division on zero")
#     print(error)
# except ValueError as value:
#     # print("Invalid Value")
#     print(value)
    
# print("Test")

#Files

files = open("C:/Users/DELL/Desktop/SHaHD/2th_Second term/Web_Technology/My_Project_HTML/Phase1/Modified_Phase2/Python/test.txt" , "r")

print(files.readable())

files.close



# print((29/53)*100)
# print(53-29)


# if(pross == 1){
    
# }








