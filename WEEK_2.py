# Variables 
# Make variables self explanatory 

'''
ram_bank_bal = 10000
ram_loan = 50000

lakshman_bank_bal = 200000
lakshman_loan = 100000

net_income = ram_bank_bal + lakshman_bank_bal
net_liability = ram_loan + lakshman_loan

final_value = net_income + net_liability
print("the family has",final_value)

'''
# Dynamic typing 

'''
a = 10 
print(a,type(a))

a = "name"
print(a,type(a))                   # the previous value of a is replaced and lost 


n = 10 
print(n, type(n))
n = n/1
print(n,type(n))                  # the previous value of n is replaced and changed to float 

'''
# Variable name 

# We cannot use keywords as a variable name 
# and = 10 
#print(and)                  # this line will show error 

# similarly we cannot use "or", "not", "True" , "False", "for",etc

# We can only use digits (0-9),alphabet (a-z ,A-Z) and unders(core(_)
# The varible name cannot start with digits , only underscore(_) and alphabet can be use as the first word in variable name 

# Variable name is case sensitive 

'''
roll = 5
ROLL = 10 
Roll = 21 

print(roll, ROLL, Roll)
'''
# Multiple assignment in python 

'''
x,y = 1,2 
print(x)
print(y)

a,b,c,d,e = 10,9,8,7,6                # sequence of variable and value should be same 
print(a)
print(b,c)
print(d,e)


a = b = c = 10 
print (a, b, c)

'''
# Swapping the number using this concept 

'''
x , y = 123,456
print(x,y)
x,y = y,x
print(x,y)

a, b, c = 10, 20, 30 
print(a, b, c)

a, b, c = b, c, a
print(a,b,c)

'''
# removing a variable 

'''
x = 20 
print(x)
del x 
# print(x)                 # will not work(variable not defined) because it is removed/ deleted 

'''
# Shorthand operator 

'''
count = 12 
count += 13
print(count)         # count = count + 13 

count -= 12
print(count)         # count = count - 12 

count *= 2        
print(count)         # count = count * 2 

count /= 4         
print(count)         # count = count / 4 

'''
# in operator (return Boolean value)

'''
print("alpha" in "A variable name can only contain alpha-numeric character and underscore")
print("alpha" in "a varible name cannot start with digits ")

print ("i" in "apple")
print ("a" in "apple")

'''
# Chaining operator (return boolean value)
# All codition must be true 

'''
x= 5
print(1< x < 10 )
print(10 < x < 20)
print(x < 10 < x *10 < 100)
print(10 > x <= 9)
print(5 == x > 4)

'''
# Escape character 


# print('it's a beautiful  day')           will show error because the single quote in it's will close the string 

print('it\'s a beautiful day')             # use backslash to before the ' to fix the problem 
print("it's a beautiful day")
print("we are from \"IIT\" Madras")
print("My name is Kaif.\t i am from Uttar pradesh")     # \t give tab space, where it is used 
print("My Name is KAif.\t\t  i am from jaunpur") 
print("My name is Kaif. \n I am from India")            # \n changes line, from where it is used 


x = 'this is a string with single quote'
y = "this is a string with a double quotes"
z =  '''this a string with triple quotes
#we can change line using triple quote string '''
a = """this is a double - triple quote
works exactly like triple quotes """

print(x)
print(y)
print(z)
print(a)


# String methods 

'''
x = 'pytHON sTrIng mEthOdS'

print(x.lower())                   # converts a sttring into lower case 
print(x.upper())                   # coverts a string into upper case 
print(x.capitalize())              # converts the first character to upper case, other becomes lower case 
print(x.title())                   # converts the first character of each word to upper case, other becomes lower case 
print(x.swapcase())                # lower case becomes upper and vice versa 


# boolean return value 

x = 'Python'
print(x.islower())                 # Returns True if all the character of string is in lower case   
print(x.isupper())                 # Returns True if all the character of string is in upper case 
print(x.istitle())                 # Returns True if string follows title rule(Capital first letter)

x = "123abc"

print(x.isdigit())                 # Returns True if ALL the character in string is digit 
print(x.isalpha())                 # Returns True id ALL the character in string is alphabet 
print(x.isalnum())                 # Returns True if ALL the character are either alphabets or digits(numeric)

'''
# Stripping in python 

'''
x = "----pyt--hon----"
print(x.strip("-"))               # Returns a trimmed version of the string 
y= "----py-*thon****"

print(y.lstrip("-"))              # Returns a left trimmed version of the string 
print(y.rstrip("*"))              # Returns a right trimmed version of the string 

'''
# Boolean return value 
'''
x= 'Python'

print(x.startswith("P"))        # Returns True if the string starts with the specified value 
print(x.startswith("p"))
print(x.endswith("n"))          # Returns True if the string ends with the specified value
print(x.endswith("on"))


z = 'Python String Methods'

print(z.count('t'))            # Returns the number of times the specified value occurs in a string 
print(z.index('t'))            # Returns the index(position) of the specified value 
print(z.index('s'))            # case sensitive 
print(z.replace('S','s'))      # Replace the first value with second value in string 
print(z.replace('t','T'))      # Replaces every where it is possible 
'''

# Caesar Cipher Encrytion

'''

alpha = 'abcdefghijklmnopqrstuvwxyz'
cipher_word = str(input("Enter the Word for encryption:"))
shift = int(input("enter the number of shift:"))
t = ''
i=0
for i in range(len(cipher_word)):
    new_word =alpha[(alpha.index(cipher_word[i])+shift)%26]
    t = t + new_word 
    i = i + 1 
print("encrypted code:",t)

'''

# if condition 

'''
birth_year = int(input("enter your DOB"))
year = 2025 
age = year - birth_year 
if age < 13:
    print("you are underage to watch a pg13+ movie")      # Anything under the condition will execute if indented 
else:
    print("you are old enough to watch the movie")        # Anything under else condition will execute if indented 

print("have a nice time")                                 # Will execute all time because it is not indented 


'''

# Problem 1 : Find whether the given number is even or odd 

'''
num = int(input("enter the number"))

if num % 2== 0:
    print("the number is even")
else:
    print("the number is odd") 

'''

# Problem 2 : Find whether the given number ends with 0 , 5 or any other number 

'''

num = int(input("enter the number"))

if num % 5 ==0 and num % 10 == 0: 
    print("the number ends with '0'")
elif num % 5 == 0: 
    print("the number ends with '5'")
else:
    print("the number ends with any other number")

'''

# Problem 3 : Find the grade of student based on the marks range from 0 to 100 

'''

marks = int(input("Enter your marks:"))
if marks >= 0 and marks <= 100:
    if marks >=90:
        print("A")
    if marks >=80 and marks < 90:
        print("B")
    if marks >=70 and marks < 80:
        print("C")
    if marks >=60 and marks < 70:
        print("D")
    if marks < 60:
        print("E")
else:
    print("Invalid input")

'''

# Problem 3 : Using else-if(elif) concept

'''

marks = int(input("Enter your marks:"))
if marks >= 0 and marks <= 100:
    if marks >=90:
        print("A")
    elif marks >=80:
        print("B")
    elif marks >=70:
        print("C")
    elif marks >=60:
        print("D")
    else:
        print("E")
else:
    print("Invalid input")

'''

# Problem 4 : Convert the given flowchart into python program 

'''

print("Travel from city A to city B")
time = int(input("Enter time:"))
longer = int(input("Define longer:"))
if time >= longer:
    price = int(input("Enter price:"))
    higher = int(input("Define higher:"))
    if price >= higher:
        print("train")
    else:
        print("coach")
else:
    price = int(input("enter price:"))
    higher = int(input("Define higher:"))
    if price >= higher:
        print("daytime flight")
    else :
        print("red eye flight")
print("Arrive city B")


'''

# Import library / Import function

'''
import math                 # 1.Important to fetch the library before using it's content

print(math.log(10))
print(math.sqrt(16))
print(math.cbrt(8))
print(math.factorial(5))
print(math.pow(10,3))


import random 

print(random.random())      # Random number between 0 and 1 


import calendar 

print(calendar.month(2025,1))
print(calendar.calendar(2026))

'''
# Program to simulate a coin toss 

'''
a = random.random()
if a <=0.5:
    print("head")
else:
    print ("Tail")

# Program to simulate dice (six-faced)

b = random.randrange(1,7)
print(b)

'''

# Different ways to import library 

'''
from calendar import *         # 2.In this method we do not have to write calendar because using star we have already 
print(calendar(2025))          # imported the content of calendar in the program             


from calendar import month     # 3.In this method, where we import only month, statement like "print(calendar(2024))" won't 
print(month(2025,10))          # work because it is not present
 

# To use calendar also we have to mention calendar also in the import statement, as given below 
from calendar import month,calendar 


import math as m                 # 4.In this method we import the library and save it as a key(variable) for easy access 

print(m.factorial(6))    
print(m.cbrt(27))


from calendar import month as m  # 5.In this method we import only a specific content of the library and store it as a variable 

print(m(2024,11))

print()

'''

# Week 2 completed