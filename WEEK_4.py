# lists 

'''
l = [12,2341,33512,3525,100]
print(l)

l.append(1024) # append function adds elements to the list 
print(l)

l.append(12)   # it can contain same elemnents
print(l)

l.remove(2341) # remove function removes the elements from the list 
print(l)

l.remove(12)   # in case of more than 1 same elements the remove function remove the first occurence of the number 
print(l)

'''

# Nested List 

'''
l =[]
l.append(1)
l.append(2)
l.append(3)
print(l)

x=[]
x.append(l)          # Here the first set of list is a single element of second list 
print(x)
x.append(123)
print(x)

m=[10,20,30]
x.append(m)
print(x)

t=[]
t.append(x)
print(t)
t.append([100,101,102])   # You can append a entire list directly
print(t)
print(t[0])

'''

# Matrix 

'''
m = []
m.append([1,2,3])
m.append([4,5,6])
m.append([7,8,9])
print(m)
print(m[0])
print(m[0][0])
print(m[0][1])
print()

'''
# Diagonal elements in matrix 

'''
print(m[0][0])
print(m[1][1])
print(m[2][2])



import random 

l=[]
l.append(random.random())
print(l)

for i in range(1,10):
    l.append(random.random())
print(l)

'''
# Birthday paradox 

'''
l=[]
for i in range(30):
    l.append(random.randint(1,365))
    l.sort()
    # append random numbers between 1 to 365 
    # append 30 of them 
print(l)
i =0 
flag = 0  # denotes that there is no repetation 
while i<len(l)-1:      # -1 is taken because of indexing 
    if l[i]==l[i+1]:   
        print(l[i],"is repeted")
        flag = 1      # repetation occured 
        break
    i=i+1
if flag ==0:
    print("There is no repetation")

'''

# Naive Search in List(self)

'''
import random
l=[]
a = 2
flag = False 
for i in range(100):
    l.append(random.randint(1,1000))
print(sorted(l))

for i in l:
    if i == a:
        flag = True
    else:
        pass 
if flag:
    print("present")
else:
    print("not present")

'''

# Naive search using in List #1

'''
import random 
a = 500
l = []
for i in range(1000):
    l.append(random.randint(1,1000))
flag = 0 

for i in range(len(l)):
    if a == l[i]:
        print("present")
        flag = 1
        break
if flag == 0:
    print("not present")

    '''

# Naive search using in List #2

'''
import random 
l = []
for i in range(100):
    l.append(random.randint(1,100))
a = 0 
while a > -1:
    print("Enter a number between 1 and 100, Type -1 to exit ")
    a = int(input())
    flag = 0
    for i in range(len(l)):
        if a == l[i]:
            print("Element Found")
            flag = 1 
            break 
    if flag == 0:
        print("Element not found")

        '''
# Sorting List 

# Sorting using default built in function- Method 1 
'''
l = [12,10,7,18,6,14,42,8,35]
l.sort()
print(l)

'''
#Sorting using default built in function- Method 2
'''
print(sorted(l))

'''
#  Sorting using program - Obvious sort 

'''
l=[12,10,7,18,6,14,6,42,8,35]
sorted = []
while len(l)>0:
    least = l[0]
    for i in range(len(l)):
        if l[i]<least:
            least= l[i]
    sorted.append(least)
    l.remove(least)
print(sorted)

'''
# Program to find the dot product

'''
x = [1,7,3,4]
y = [8,6,3,2]
dot_product = 0             # means (1*8)+(7*6)+(3*3)+(4*2)
for i in range(len(x)):
    dot_product = dot_product + x[i]*y[i]
print([dot_product])

'''
# Matrix addition by first principles using manual way
# square matrix with dimension(order) 4X4

'''
dimension = 4

r1 = [1,2,3,4]
r2 = [4,5,6,7]
r3 = [7,8,9,14]
r4 = [1,1,2,2]

s1 = [1,2,1,2]
s2 = [6,2,3,15]
s3 = [4,2,1,45]
s4 = [1,7,2,9]

a = []
a.append(r1)
a.append(r2)
a.append(r3)
a.append(r4)

b= []
b.append(s1)
b.append(s2)
b.append(s3)
b.append(s4)

print(a)
print(b)

c = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]       # Addition of and b 

for i in range(dimension):
    for j in range(dimension):
        c[i][j] = a[i][j] + b[i][j]
print(c)

'''
# Matrix Multiplication 

'''
dimension = 3

r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [1,2,1]
s2 = [6,2,3]
s3 = [4,2,1]

a = []
a.append(r1)
a.append(r2)
a.append(r3)

b= []
b.append(s1)
b.append(s2)
b.append(s3)

print(a)
print(b)

# c[2][1] id the dot product of the 2nd row of a and 1st column of b 
c = [[0,0,0],[0,0,0],[0,0,0]]   

for i in range(dimension):
    for j in range(dimension):
        for k in range(dimension):
            c[i][j] = c[i][j] + a[i][k]*b[k][j]
print(c)

'''

# Function: a block of code that perfrom a specific task 

'''
# syntax: 
# def function_name(parameter): --------function defination 
#   body of the function
# return statement 
# function_name(argument)---------------function calling 


# Benefit of function:
# 1. Code reusability 
# 2. code breakup 
# 3. logic hiding 

# Types of functions 
# a. inbuilt 
# b. user defined 

# Important terms:

# 1. return: Function which return something 
# 2. void: function which doesn't return anything (return null)
# 3. parameter: parameter is a variable listed inside bracket in the function defination 
# 4. argument: argument are actual values send while calling a function 

def msg():# without parameter 
    print('hello world')
msg()

def msg1(str):# with parameter 
    print('hello',str)
msg1('virat')


def sqr(int):
    return(int**2)# return function 

print(sqr(5))
print(sqr(4))

# Lenght calculator 

def lenght_cal(input):
    ans = 0
    for i in input:
        ans+=1
    return ans

print(lenght_cal('abcdefghi'))


# Types of arguments 

#1. positional argument 
def sum(a,b):
    return (a+b)
print(sum(10,20))# a=10,b=20 

#2. default argument 
def prod(a,b,c = 1):
    return a*b*c

print(prod(3,5,2))# overwright on the value of c 
print(prod(3,5))# default value of c i.e, 1

#3. keyword argument 
def great(first,last):
    print(f'{first}{last}')
great(last = ' tesla',  first = 'nikola')# position doesn't matter when argument is marked by the parameter 


# IMPORTANT RULES:
#1. while defining function default cannot be followed by non-default 
# (a=1,b,c) will generate error 
#2. while calling positional argument cannot follow keyword argument 
# (last = 'tesla', first = 'nikola') will generate error 


# *args and **kwargs - variable lenght arguments 
# *args - variable lenght non-keyword arg, treated as tuple 
# **kwargs - variable lenght keyword args, treated as dict

# correct order in function defination:
# 1.positional parameter 
# 2. *args (if-any)
# 3. keyword- only parameter 
# 4. **kwarg (if-any)

# args 

def better(*args):
    print(args)

better(1,2,3,4,5,6)# there is no limit to take arguments- creates a tuple of the arguments given 

# Sum using args 
def sum(*args):
    sum = 0
    for i in args:
        sum += i 
    print(sum)

sum(1,2,3,4,5,6,7,8,9)

# kwargs 

def greet(**kwargs):
    print(kwargs)

greet(a=1,b=2)# there is no limit to take keyword arguments- create a dictionary of keys and value 

# sum using kwarg

def sum(**kwargs):
    sum = 0
    for value in kwargs.values():
        sum += value
    print(sum)

sum(a=1,b=2,c=3)


# combination of args and kwargs 

def fun(*args,**kwargs):
    print(args,kwargs)

fun(1,2,3,4,5,a=1,b=2,c=3)# make sure that positional argument is before keyword argument

'''

# Scope of variable:

# Local- variable defined inside a function and thus is only usable in that 
# Global - variable defined in any function and used everywhere 

