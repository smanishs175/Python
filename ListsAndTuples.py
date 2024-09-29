#List 

marks = [1,2,3,4]
print(marks)
print(type(marks))

marks.append(5)
print(marks)
#[1, 2, 3, 4, 5]
marks.sort(reverse=True)
print(marks)
#[5, 4, 3, 2, 1]

list1 = ["e","d","c","b","a"]
list1.reverse
print(list1)
#['e', 'd', 'c', 'b', 'a']
list1.insert(4,"f")
print(list1)
#['e', 'd', 'c', 'b', 'f', 'a']


#Tuple 

tup = (2,1,3,1)
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
