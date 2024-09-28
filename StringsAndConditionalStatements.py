s1 = "hello"
s2 = "world"
print(s1+s2)
print(s1+" "+s2)
string2 = 'This is String'
string3 = """This is a String"""

#newline 
str1 = "We are creating this string in python.\nThis is a code in python"

#tab
str1 = "We are creating this string in python.\tThis is a code in python"

print(str1)
print(len(str1))

len_test = "manish"
print(len(len_test))
len_test1 = "manish "
print(len(len_test1))

print(len_test[0])
print(len_test1[6])


#Slicing :Accessing part of the string
print(len_test1[:int(len(len_test1)/2)])

print(str1[:4])

#functions 

str = "i am studying python"

print(str.endswith("n"))
str = str.capitalize()
print(str)
str = str.replace("a","o")
print(str.find("z"))
print(str.find("o"))

# Get users first name , write length of the same 
str_input = input("Enter your first name")
print("First name of user is", str_input)
print(len(str_input))

