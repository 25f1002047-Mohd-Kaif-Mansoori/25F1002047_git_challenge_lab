# Function in Python 
# Functions is a block of reusable code (place () after the function name to invoke it)

'''
def add(a,b):    # here (a,b) are the parameter(temporary variable that is used within a function) of the function 
    ans =a+b 
    print(ans)
add(12,13)       # here (12,13) is an argument(value of the parameter) 
add(31,44)
add(32,55)

'''
# return statement in function 
# return are statement that is used to end a function and send the result back to the caller 

'''
def exponent(c,d):
    expo = c**d
    return expo

print(exponent(2,10))

'''
# Example 

'''
def add(a,b):
    ans = a +b
    return ans # Would not work for print ans(because we have called the function but without return it won't work)
a = 5 
b = 15 
print(add(a,b)+10)

'''
# Discount using the functions 

'''
def discount(cost,dis):
    ans = cost-(cost*(dis/100))
    print(ans)

discount(1000,25)
discount(351000,75)
discount (157000,75)

'''

# Function to find the minimum and maximum value in a list 

'''
def list_min(l):
    mini= l[0]
    for i in l:
        if i <= mini:
            mini = i
    return mini

def list_max(l):
    maxi = l[0]
    for i in l:
        if i >= maxi:
            maxi = i 
    return maxi 

print(list_min([12,34,-23,43,53,21,2,43]))
print(list_min([12,113,125,553,-1,54,11,4,35,65,753,3,6]))

print(list_max([12,34,43,-23,53,21,2,43]))
print(list_max([12,113,125,-1,553,54,11,4,35,65,753,3,6]))

'''
# Function to append two list one before the another 

'''
def list_appendbefore(l,z):
    new = []
    for i in range(len(z)):
        new.append(z[i])
    for i in range(len(l)):
        new.append(l[i])
    return new 

x = [12,11,12,3,4,5352,645,3345,66,434,22]
y = [23,234,5654,767,464,34]

print(list_appendbefore(x,y))

'''
# Function to append two list one after the another 

'''
def list_appendafter(l,z):
    new = []
    for i in range(len(l)):
        new.append(l[i])
    for i in range(len(z)):
        new.append(z[i])
    return new 

x = [12,11,12,3,4,5352,645,3345,66,434,22]
y = [23,234,5654,767,464,34]

print(list_appendafter(x,y))

'''

# Function to find the average of a list (Self)

'''
def list_average(l):
    sum = 0 
    count = 0 
    for i in range(len(l)):
        sum = sum + l[i]
        count = count +1 
    return (sum/count)

print(list_average([12,13,14,15,16,17,18,19,20]))

'''
# Function to find the average of a list

'''
def list_average(l):
    sum = 0 
    for i in range(len(l)):
        sum = sum + l[i]
    ans = sum/len(l)
    return ans 

print(list_average([12,13,14,15,16,17,18,19,20]))

'''
# Difference between List and set 
# Searching in set is easy than searching in list 
# List 
'''
l = list(range(10))
print(l)
print(l[5])
l.append("kaif")
l.append(2.44)
print(l)

# Set 

s = set(range(10))
print(s)

'''
# in command 

'''
print(5 in l)               # it searches the whole list for 5 and return boolean logic 
print("KAIF" in l)          # return false because is case sensitive 

l = list(range(100000000))
print(l[0])
print(l[121415])
print(l[len(l)-1])
print("kaif" in l)          #  Will take time to return False as it searches the whole list for the word 
'''
'''
s = list(range(100000000))
print(s[0])
print(s[121415])
print(s[len(s)-1])
print("kaif" in s)          # Will take comparitively less time than in case of list 

'''

# Using sys library the size of list and set can be compared and set usually take 10 times more space than list 

'''
x = list(range(100))
y = set(range(100))
print(x)
print(y)
import sys

print(sys.getsizeof(x))     # size is 856
print(sys.getsizeof(y))     # size is 8408

'''
# Cons of using set is that you cannot visit a particular element in the set 

# x[5] will show 5 but y[5] will show error (set is not subscriptable)

# Addition in set 
'''
z = {'amar','neeru','anamika','varsha','nitin'}
z.add('ramesh')
print(z)

'''

'''
# Tuple in python 
# A tuple is unchangeble but a list can be changed i.e, list is flexible but tuple isn't
# Used when we are sure of the list that we are handling and we are also sure that it never changes,then use a tuple 
t = (2,3,536,3463,253,464)
print(t)

'''
# Tuple Methods 
'''
print(t.count(536))          #count the number of occurence of the element in the tuple 
print(t.index(3463))         # finds the index of the element in the tuple 

'''
# String library 
'''
import string 

s =string.ascii_letters     # Print all the lowercase and uppercase english alphabet 
j = string.ascii_lowercase  # Print all the lowercase english alphabet 
k= string.ascii_uppercase   # Print all the upper case english alphabet 

print(s)
print(set(s))               # Random order 
alpha = tuple(list(s))      # Sorted order

# Program to remove the symbol from the a string 

x = 'my-name+is*mohammad$kaif))(0)mansoori,this is^a program~~to<<remove,,symbols'
r =[]
for p in x:
    if p in alpha:
        r.append(p)
print(r)

'''

# More on List 

'''
l1 = [1,2,3]
l2 = [10,20,30]
l12 = l1 + l2
l21 = l2 + l1
print(l12,l21)         # Concatenation of list 

print([0]* 10)         # Multiplcation of list 

l3 = [1,2,3]
l4 = [2,3,1]

print(l1==l3)          # comparison of list 
print(l4==l3)          # False because order matters  
'''

# Rules for comparison 

#Compare the first elements:
#If they’re unequal → that determines the result.
#If they’re equal → move to the next pair.
#If one list runs out of elements first → the shorter list is considered less than the longer one.

'''
print([1,2]<[2,1])     # True because the comparison occurs element by element 
print([1]<[1,2,3])     # True because the second one have more element 
print([2,3]<[3])       # True because the first get compared to the first element 
print([]<[1])          # True becuase the empty list is less than a list with element 

'''
# Mutability 

'''
# list are mutable i.e, changeble 
l = [1,2,4]
print(l)
l[2]=3
print(l)

# Strings are not mutable 
s= "abcde"
print(s[3])   # Will show the element on that particular index 
#s[3]="f"
# print(s)      # Will show error as string object are immutable 

'''
# Memory location 
'''
x =5 
y =x
x =10          # here the computer overwrite the value of x to be 10 and remove the previous value i.e, 5
print(x,y)     


l1 =[1,2,3]
l2 = l1        # When two list are assigned same value change in one get reflected on the other 
l1[0] = 100    # Hence changing the value of index 0 to 100 is seen in both the list l1 and l2
print(l1,l2)   

'''
# Creating new memory location for list using 3-method 

'''
l1 = [1,2,3]
l2 = list(l1)     # Method 1
l3 = l1[:]        # Method 2 
l4 = l1.copy()    # Method 3

l2[0] = 100 
l3[1] = 200
l4[2] = 300

print(l1,l2,l3,l4)

'''
# is operator in python 

'''
l1 = [1,2,3]
l2 = list(l1)
l3 = l1[:]
l4 = l1.copy()
l5 = l1

print(l1 is l2)    # check if both are stored in the same memory location and return boolean value      
print(l1 is l3)
print(l1 is l4)
print(l1 is l5)
'''

# How list works in a function 

'''
def add(x):
    x = x+1
    return x 

x = 5 
print(add(x))       # prints 6  # Belong to the local space 
print(x)            # prints 5  # Belongs to the global space 

# This type of argument calling usinging integers is called as call by value 

def addition(y):
    y.append(1)
    return y

y = [5]
print(addition(y))  # Print [5,1] because 1 got appended to the 5 
print(y)            # print [5,1] because append function have appended one the the original list that only contained [5]

# This type of argument passing using list is called as call by reference 

'''
# List methods 

'''
l = [1,2,3,4,5,6]
print(l)

l.append(4)        # add the element at the end of the list 
print(l)           # [1,2,3,4,5,6,4]

l.remove(2)        # Remove the element from the list 
print(l)           # [1,3,4,5,6,4]

x = l.copy()       # create a copy of the list 
print(x,l)         # [1,3,4,5,6,4][1,3,4,5,6,4]

l.insert(2,9)      # (index,element) insert the element 9 in the 2nd index 
print(l)           # [1,3,9,4,5,6,4]

l.pop(0)           # Remove the element of the given index 
print(l)           # [3,9,4,5,6,4]

l.sort()           # Sort the list in the ascending order 
print(l)           # [3,4,4,5,6,9]

l.reverse()        # Reverse the order of the list 
print(l)           # [9,6,5,4,4,3]

'''

# More on Tuples 

# Concept of packing and unpacking using Tuples

'''
t = 1,2,3
print(t,type(t))      # computer by default create a tuple by packing these element into a single entity 

x,y,z  = t 
print(x,y,z,type(x))  # Here computer by default unpacks the tuples into three independent integer value 

'''
# Creating tuples in python 

'''
l= [10]
print(l,type(l))

i = (10)
print(i,type(i))      # Here even though we have used round bracket the computer stores single value as a integers rather than tuple

t = (10,)
print(t,type(t))      # To create a single element tuple we use comma after the element ]] 

'''
# List inside Tuple 

'''
t = ([1,2],['a','b'])
# t[0] = 10  won't works because tuples are immutable 
t[0][0] =10  # will works because list are mutable 
print(t)     

# This principle in python is reffered to as hashable 
# if value inside tuple is immutable = hashable 
# if value inside tuple is mutable = non hashable 

'''

# More on set 

'''
A = {1,2,3}
# print (stA[0]) will show error as set is not subscriptable 
B = {3, 4,5,4,3,4}
print(A.issubset(B))     # Shows whether a set is a subset or not in boolean logic 

c = {1,2,3,4,5}
print(A.issubset(c))       # Every set is a subsset of itself 

print(A.issuperset(B))   

# union 

c1 = A.union(B)    # Method 1 
c2 = A | B         # Method 2 
print(c1,c2)

# intersection 

c3 = A.intersection(B)
c4 = A & B
print(c3,c4 )

# Set difference 

c5 = A.difference(B)
c6 = A - B
print(c5,c6)

'''

# Functional programming 

'''
# Functional programming for if-else statement 
a = 100
b = 20 

if a<b:
    small = a 
else:
    small = b 

print(small)

small = a if a < b else  b  # the above code can be written in single line like this
print(small)

# Functional programming for while loop 
a = 5 
while a> 0: print(a); a = a-1

# Functional programming for for-loop using list comprehension 
fruits = ["mango","apple","banana","orange","pineapple","watermelon","guava","kiwi"]

newlist = []
for fruit in fruits:
    if "n" in fruit:
        newlist.append(fruit.capitalize())
print(newlist)

newerlist = [fruit.capitalize() for fruit in fruits if "n" in fruit]
print(newerlist)        # the above code block using for-loop can be written in single line 

'''
# Type of function argument  

'''
# Positional argument: The value in the parameter is tied to the position of the parameter
 
def add(a,b,c):        # def refers to the defining of the function 
    return (a+b-c)     # (a,b,c) in the function refers to the parameter 

print(add(20,30,40))   # Function call refers to the execution of the function statemnet 
                       # values in the function call is refered to the argument 

# Keyword argument: The value in the keyword is assigned the given variable irrespective of the position of the parameter 

print(add(b=30,c=50,a=10))    

# Default argument:  # In case there is no argument passed the code itself take the default value provided in the parameter 

def sub(z, x=20, y=30):
    return (x+y-z)

print(sub(12))        
print(sub(40,10))
print(sub(30,40,34))

'''
# Scope of variable 
# When we call a function the computer don't take x to the parameter instead it just take the value of x and put it in the parameter so that x is not changed outside the function 
'''
def myfunction1(x):                             
    x = x*2                                      # This x i.e, 10, is a local variable and is acessible only in this defination function 
    print("value of x in the function1", x)

def myfunction2(x):
    x= x*3                                       # This x i.e, 15, is a local variable and is acessible only in this defination function 
    print("Value of x in function 2", x)

x = 5                                            # Here x is a global variable and is accesible throughout the whole program 
print("value of x before function call", x)
myfunction1(x)  
myfunction2(x)
print("value of x after function call", x)
print()

'''
# How to modify the global variable inside a function 

'''
def myfunction1():                              # First we remove the parameter from the function and function call 
    global x                                    # Then we explicitly mention global and the variable name to make it a global variable inside the function 
    x = x*2                                      
    print("value of x in the function1", x)

def myfunction2():
    global x 
    x= x*3                                       
    print("Value of x in function 2", x)

x = 5                                            
print("value of x before function call", x)
myfunction1()  
myfunction2()
print("value of x after function call", x)

'''
# Type of function 
# Function is always yellowed colored in vs and is followed by parenthesis 
'''
# Inbuilt functions 
print(),input(), len()

# Library functions 
import math , random
math.log(), math.sqrt(), math.random(), random.randrange()

# String methods (functions)
''.upper(), ''.lower(), ''.strip(), ''.count(), ''.index(), ''.replace()

# User defined functions 
def square(x):
    sqr = x**2
    return sqr
print(square(5))

'''
# Matrix 

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[9,8,7],[6,5,4],[3,2,1]]
l = []
l1 = []
for i in range(len(a)):
    for j in range(len(a[0])):
        l.append(a[i][j]+b[i][j])
print(l)






# Step 1: find out the minimum most element in the list 

def min_list(l):
    mini = l[0]
    for i in range(len(l)):
        if l[i]<mini:
            mini = l[i]
    return mini 

def obvious_sort1(l):
    x = []
    while (len(l)>0):
        mini = min_list(l)
        x.append(mini)
        l.remove(mini)
    return l



l = [12,34,46,67,79,57,23,35,1,4,435,46,64,45,3,44,634,64,75,65]
print(obvious_sort1(l))

print("Week 5 ended")

print("end of week 5")