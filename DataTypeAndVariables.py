print("Hello World")
print("Manish Shinde", "Manish is from Maharashtra")
print("My age is 24")
print(23)
print(35)
print(23-35)
print(35-23)
name = "manish"
print(name)
age = 24
price = 25.99
print(age)
print("Price is :", price)
print("My age is",age)
print("My name is :",name)
age2 = age
print(age2)
print(type(name))
print(type(age))
print(type(price))
old = False
print(type(old))
a = None
print(type(a))

a = 2
b = 4
c = a+b

# this is comment 
print("Sum is :",c,a+b)

"""
this is multiline comment
this is multiline comment
"""

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)

print(a == 2)
print(a != 2)
c = 8

print(a > b)
print(a < b)

num = 20
print(num)
num = num + 10
print(num)
num += 10
print("num is :",num)

num *= 10
print("num is :",num)

num **= 10
print("num is :",num)

#logical operators
a = True
print("Value of not a is :",not a)

b = False
print("Value of not b is :",not b)

val1 = True
val2 = False
print("And of val1 and val2 is :", val1 and val2)
print("Or of val1 and val2 is :", val1 or val2)

c = 50
d = 40

print("OR operator :", c==d or c > d)

# Type conversion 

e = 50
f = 10.0

print(int(e+f))

# type casting

a = 3.14
a = str(a)
print(a)
print(type(a))


# input in python 
name_var = input("Enter your name:")
print(name_var)

age_var = input("Enter your age:")
print("Age of person is :", age_var)

# Type casting with input
type_cast_input = int(input("Enter typecast input"))
print("Type cast input is :", type_cast_input)

#1. program for sum of 2 numbers 
a = int(input())
b = int(input())
c = a+b
print(c)

#2. program to input side of a square and print its area

side = float(input("Enter the side of square"))
print("Area of square is :", side*side)

#3 Input 2 float point numbers and print average of them 
r = float(input())
s = float(input())
t = (r+s)/2
print("The average of 2 floating points is :",t)