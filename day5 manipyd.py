# ! common function for list
#l1 = [6, 7, 8, 9, 0,]
#print(len(11))

#print(max(l1))
#print(min(l1))

#l1 = [6, 7, 8, 9, "p", "u"]
#print(max(l1))

#print(max(l1))
#print(l1.index(9))

#counting---->

#l1= [6, 7, 6, 8, 9, 2, 4, 9, 6]
#print(l1.count(6))

# ! some functions which is specifically used for list

# To add element inside list
#l1 = [6,6,6,7, 8, 9, 0, 8.96, -5, 0.78]

# ? To deleat element from list
#l1 = [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]
#l1.pop()
#print(l1)

 #pop(index_value) --> used to delete element at specific index
#11.pop(4) #4 is index value
#print(11)

# clear()----> to deleat all the elements from the list
#l1.clear()
#print((l1))

# remove()----> to complete deleat all element in list
#l1.remove()
#print(l1)

#del-> to delete the list
#del 11 ttor del (11) print(11)
#print(l1)

#? join 2 lists

#l1 = [9, 0, 8]
#l2 = ["p", "o", "t", 34]
#print(l1+l2)

#* extend()-> to combine 2 lists
#11.extend(12)
#print(11)

# ?-----> copy()

#11 = [6, 7, 8, 9, 3]
#12 = 11.copy()
#print(12)
#print(11)

#print(id(11))
#print(id(12))

#! diff between shallow copy and deep copy
#shallow copy
#import copy
#l1 = [8, 9, 0,[5, 6], [3, 2, 1]]
#print(l1[-1][1])
#l2 = copy.copy(l1)
#l1.append(890)
#print(l1)
#print(l2)

#* Deep copy
#import copy
#l1= [8, 9, 8, [5, 6], [3, 2, 1]]
#print(11[-1][1]) --> to index nested list

#12 copy.copy (11)
#11.append(890)
#print(11)
#print(12)

# ? sort---> arrange elements in list in asending or desemding order

#11 [9, 7, 45,0,-6, 5, 12]
#11.sort() # to arrange in ascending order
#print(11)

#11.sort(reverse=True) # to sort in descending order print(11)
#11= ['z', '1', 'o', 'p', 9]
#11.sort()
#print(11) #--> error

# ? list constructor
#list()-> to conver other collection datatype to list
#13 ((8, 9, 0))
#print(list(13))

#14 =(8,9)
#print(list(14))

#---> nested list
#l1 = [8, 9, 10, 8, 7], ["p", "o",'y'], [8, 't']
#print(l1[-2][1])----->o

#l1 = [8, 9, 10, 8, 7], ["p", "o",'y'], [8, 't']
#print(l1[1:4])
#print(l1[1:-1])

# ? to deleat "t" from l1

#l1 = [8, 9, 10, 8, 7], ["p", "o",'y'], [8, 't']
#l1[-1].remove('t')
#print(l1)

# ? combine these ["p", "o", 'y'], [8, 't'] list in l1 to ["p", "o", 'y', 8, 't']
#l1 = ["p", "o", 'y'], [8, 't']
#l1[-2].extend(l1[-1])
#l1.pop(-1)
#print(l1)

# ! -----> Tuple
# * char of tuple

# 1.) Tuple have to be surrounded by()
# 2.) The elements inside tuple are not changable
#3.) The elements inside tuple are indexed
# 4.) The element will be excuted in order
# 5.) It is a hetrogenous
# 6.) It allow duplicate elements

# Eg:

#t1 =(8, 8, 9, 6, 5,78, [9, 8], (6, 8), "hey", 9+6j)
#print(tl)
#print(type(t1))
#
#? Indexing, slicing are all same as list

#l1 = (8)
#print(type(l1)) # int

##t1 = (8,)
##print(type(t1))

##t2 = 8,9
##print(type(t2))

##len(), min(), index(), count()---> all same as list

##to add element inside tuple ----> cannot add
##cannot deleat any element from tuple

##* join 2 tuple
##t1 = (8, 9, 0)
##t2 = (6, 7, 8)
##print(t1+t2)
##
##* To add all element inside list and tuple
##sum()
##l1 = (8, 9, 7, 6)
##print(sum(L1))

#*   sort tuple
##t1 = (8, 9, 0, 89, 12)
##print(tuple(sorted(t1)))
##print(tuple(sorted(t1, reverse=True)))

#? Iterate list and tuples
#Iterate based on Elements
#11 [9, 8, 8, 6, 5]
# for i in 11:
# print(i)

#Iterate based on index value
##l1 =[9, 8, 0, 6, 56]
##for i in range(0, len(l1)):
##     print(l1[i])

# !----> string

##s1 ='0'
##print(type(s1))

##s1 = "helloworld"
#* To access string
# print(s1)
# 
# indexing and slicing--> same as list and tuple
#
# print(s1[0:5])

# !--------> comman function

# len(), min(), max(), index(), count()
##s1 = "hello world"
##print(len(s1))
##print(max(s1))
##PRINT(MIN(S1))

###ord() ----> used to find the ASCII value of a character
##s1 = 'u'
##print(ord(s1))

##functions of string
##s1 = "hello world

# ? to convert all character to upper case
#print(s1.upper())

# ? to convert to lower case
##s1 = "HFRDGiou"
##print(s1.lower())

# ? strip() ----> to eliminate the space in beginning and end of string
##s1 = "where are you? "
##print(s1.lstrip())
##print(s1.lstrip())
##print(s1.lstrip())

# split()----->
#s1 = "where are you"
#print(s1.split(" "))

# * replace()
#s1 = "where are you"
#print(s1.replace('r', '&&'))

# swapcase()------>to convert capital to small and small to capital at a time
##s1 ="HEY there"
##print(s1.swapcase())


#s1 = "hey there dont sleep"
##s1 = 'never giveup'
##print(s1.title())

# * join the string
##s1 = "hello"
##s2 = "world"
##print(s1+s2)

# s1 = "hello there dont sleep"

 #find()-> to find the index based on a charachter
#51 "hello world"
#print(s1.find('z'))
#print(sl.index('z'))

#join()->
#11 ["hey", "there"]
#print(" ".join(11))
#print("$".join(11))

##s1 = "Welcome to all"
##print(s1.endswith('l'))
##print(s1.startswith('W'))

##s1 = "welcome to all"
##print(s1[::-1])

# !----> Eg:1
#wap to find the number of lower case letters

##s1 = "HEY there you aRE"
##count = 0
##for i in s1:
##    if i.islower():
##        count+=1
##print("The total num of lower case letters: ",count)

# !----> Eg:2
#1 Eg:2 r --> "$"
##s1 = 'restarter"
##fst = s1[8]
##bal = s1[1:]
##txt = bal.replace(fst, "$")
##print (fst+txt)


# !----> Eg:3
s1 = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including
versions of Lorem Ipsum.'''
s1 = s1.strip()   
chracters = len(s1)
print(chracters)

words = s1.split(" ")
print(len(" words "))

sentenses = s1.split('.')
for val in sentenses:
    if val =='':
        index = sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))

for val in s1:
    if val ==" ":
        space=space+1
print(space)






















