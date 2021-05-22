import numpy as np
import os
# # l = [2,4,1,3]
# # l.sort()
# # print(l)
# # l.sort(reverse=True)
# # print(l)

# # #Example 3: Sort the list using key
# # # random list
# # def seconditem(item):
# #     return item[1]
# # random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# # random.sort(key=seconditem)
# # print (random)

# # car =	{
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # print(car.get("model"))
# # print(car["model"])

# # # sorting using custom key
# # employees = [
# #     {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
# #     {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
# #     {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
# #     {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
# # ]
# # #print(employees.get("Name"))
# # def sortby_Name(item):
# #     return item["Name"]
# # test = employees.sort(key=sortby_Name)
# # print(employees, end="\n\n")

# # #Prime number
# # x = list(range(100,200,1))
# # print (x)
# # for i in x:
# #     if all(i%j!=0 for j in range(2,i)):
# #         print(i)
# #list sort without sort function
# # l = [2,4,1,3]
# # new_l = []
# # #min = l[0]
# # while l:
# #     min = l[0]
# #     print(l)
# #     for i in l:
# #         #print(i)
# #         if i<min:
# #             min = i
# #             #print(min,"min")
# #     new_l.append(min)
# #     l.remove(min)
# # #print(new_l) 
# # #Print list in reverse order
# # #  
# # l = [2,4,1,3]
# # x = l[::-1]
# # r_list = []
# # #print(x)
# # while l:
# #     for i in l:
# #         last = i
# #     r_list.append(last)
# #     l.remove(last)
# # print(r_list)

# #palindrom - backward AND FORWARD same (POOP)
# s= "poop"
# r = "".join(reversed(s))
# print (r,s)
# # for i in s:
# #     print(i)
# #     for j in reversed(s)
# #         print(j)

# #set of duplicates in list
# # l = [2,4,1,2,4]
# # dup = []
# # for x in l:
# #     if l.count(x)>1:
# #         dup.append(x)

# # print(set(dup))

# # l = [2,4,1,2,4]
# # s = 4
# # for x in l:
# #     if s==x:
# #         print(x)

# #print(set(dup))
# #remove dupicate character
# '''
# l = "abbcd"
# for i in l:
#     if l.count(i)>1:
#         print(i)  


# total=10
# def sum(a,b):
#     total = a+b
#     print(total)
# sum(10,20)
# print(total)

# #How to convert a list into a string?
# l = ["my","name","is","rekha"]
# s = " ".join(l)
# print(s)
# t = tuple(l)
# print(t)
# '''
# # #6) How to count the occurrences of a particular element in the list?
# # l = [2,4,1,2,4,2]
# # c = l.count(2)
# # print(c)
# # # How can you create Empty NumPy Array In Python?
# # import numpy as np
# # n = np.empty
# # import array
# # a = [1, 2, 3]
# # print (a[-3])
# # print (a[-2])
# # print (a[-1])

# # tell the output
# # names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
# # names2 = names1 # reference
# # names3 = names1[:] # copy value

# # names2[0] = 'Alice'
# # names3[1] = 'Bob'
# # print(names1)
# # print(names2)
# # print(names3)

# # sum = 0
# # for ls in (names1):#, names2, names3):
# #     print(ls)
# #     if ls[0] == 'Alice':
# #         sum += 1
# #     if ls[1] == 'Bob':
# #         sum += 10

# # print(sum)
# # #average
# # l = [23,45,56]
# # #x = sum(l)
# # sum1 = 0
# # for i in l:
# #     sum1 +=i
# # print(sum1/len(l))

# # # reverse a number
# # n = str(143)
# # l = n[::-1]
# # print (l)
# # n = 143
# # rev = 0
# # while n>0:
# #     dig = n%10
# #     rev=rev*10+dig
# #     print(n)
# #     n=n//10
# #     print(n)
# # print("The reverse of the number:",rev)

# # Multiplication table (from 1 to 10) in Python
# # n=12
# # for i in range(1,11):
# #     s = str(12) + '*' + str(i) + '=' + str(12*i)
# #     print(s)
# #two dimentional array  slicing

# #lambda
# # x=lambda x:x+10
# # print(x(5))

# #
# # s = "G()(al)"
# # s = s.replace("()","o")
# # s = s.replace("(al)","al")

# #print(s)
# #diff between list and generator. list is slower because it keeps all items in memory
# ##using list
# mylist = [1,2,3,4]
# def square_number(vlist):
#     result = []
#     for item in vlist:
#         result.append(item*2)
#     return result
# newlist = square_number(mylist)
# print(newlist)
# ##using generator
# mylist = [1,2,3,4]
# def square_number_gen(vlist):
#     for item in vlist:
#         yield item*2
# newgen = square_number_gen(mylist)
# print(newgen) #generator object
# for item in newgen:
#     print(item)

# #iterator
# def Sentence(mystr):
#     mylist = mystr.split(' ')
#    # for 
#     print(mylist)

#     for w in mylist:
#         yield w
# my_sentence = Sentence('This is a test')
# for word in my_sentence:
#     print(word)
# ###############
# def Sentence(mystr):
#     def __init__(self,str):
#         self.str = str
#         self.index = 0
#         self.word = str.split(" ")

#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.index += 1
#         if self.index<=len(self.word)
#             return self.word 



#     mylist = mystr.split(' ')

#    # for 
#     print(mylist)

# #     for w in mylist:
# #         yield w
# # my_sentence = Sentence('This is a test')
# # for word in my_sentence:
# #     print(word)


arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print (x)
    for y in x:
     print(y)
#total no of lines in  FILE
mylines = 0
f = open("out.csv", "r")
for line in f:
    #print (line)
    mylines = mylines +1
f.close
print('mylines',mylines)
# with open("out.csv", "r") as f:
#     print(f.readlines())
#     mylines = mylines + 1
#     print('mylines',mylines)

#Write a code to sort a numerical list in Python?

list = ["2", "5", "7", "8", "1"]
list_1 = [int(i) for i in list]
print(list_1)
nparr = np.array(list_1)
np_sorted = np.sort(nparr)
print(np_sorted)
#Can you write an efficient code to count the number of capital letters in a file?
f = open("delete.txt", "r")
alllines = f.read()
for letter in alllines:
    #print(letter)
    if letter.isupper():
        print(",",letter)

#Write a code to sum numerical list in Python?

list = ["2", "5", "7", "8", "1"]
list_1 = [int(i) for i in list]
print(list_1)
nparr = np.array(list_1)
np_sum = np.sum(nparr)
print(np_sum)
#another was  to sum list items
import functools
l_sum = functools.reduce((lambda x,y:x+y),list_1)
print(l_sum)

#Write a program in Python to produce Star triangle?
x = '*'
y='&'
for i in range(5):
    y= y+x*2
    print(y)


