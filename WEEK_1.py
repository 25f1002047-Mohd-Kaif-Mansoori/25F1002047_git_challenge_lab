# print command : used to display output in the console 
'''
print("hello world!")
print(12,"iitm",12.000)
'''

# Variables 
'''
a = 10               # a is variable and 10 is literal 
print(a)
b = "hello ladies "
print (b,a)
c = a
print (c)
print(a*100)
d = 200
print(d/a)
print(b*a)
d = d + a
print(d)
'''

# Exponential value 

'''
a = 12e5                # 12*10^5 
print(a)
print(type(a))          # Float 

'''  
# Variable naming conventions 

# Variable name should be descriptive 
# They must start with a letter or an underscore and contain letters, numbers and underscore
# Variable names are case sensitive 


# Input function 
'''
print("enter a number:")
n = int(input())
print(n)
print(n+1)
print(n+2)
print(n+3)

print("type your name")
n = str(input())
print("hello",n, "how are you?")
print("where do you live,",n,"?")
p = str(input())
print ("how is the whether in",p,"?")

'''
#program to print the area of a circle 
'''
radius = int(input("Enter the radius of the circle:"))
area = 3.14 * radius * radius 
print("the area of the circle with radius",radius,"is",area)

'''

# Type function (Concept of datatype)
'''

s = type("name")            # string 
i = type(122)               # integers
f = type(122.0)             # float 
l = type([10,20,30,40,50])  # list
d = 12+2j                   # complex

print(type(d))
print(s,i,f,l)
print("s is of type :",s)       

# Boolean datatype 

b1 = True 
b2 = False 

print(type(b1),type(b2))

# True is internally stored as 1 and False is internally stored as 0 in python 

a = True 
b = True 
c= a+b
print(c)#2

x = False 
y = True 
z = x+y
print(z)#1

'''
# Complex datatype 

''''
a = 15 + 5.6j
print(type(a))
print(a.real)         # real part of the complex number
print(a.imag)         # imaginary part of the complex number

'''
#concept of Indexing - from 'o' to lenght-1

'''
l =[10,20,30]
print(l)
print(l[0])
print(l[1])
print(l[2])

print(type(l[2])) # will show class int because l[2] is integer

'''

# Data conversion (type conversion / type casting)

'''

a = int(34567.3456)
b = int("1234")
print(a, type(a))          # From float and string to integer 
print(b,type(b))

a = float(87) 
b = float("87")      
c = float("87.54")

print(a,type(a))          # From string and integer to float 
print(b,type(b))
print(c,type(c))

a = str(1234)
b = str(123.45)

print(a,type(a))          # From integer and float to string 
print(b,type(b))

print(int(True))          # From boolean to integer True = 1
print(int(False))         # False = 0

print(Float(True))        # From boolean to float True =1.0
print(Float(False))       # False = 0.0

a = bool(10)              # any value except "0" negative or positive is True (0 is False) 
b = bool(0)
c = bool(-10)

print(a, type(a))         # From integers to boolean 
print(b, type(b))
print(c, type(c))

a = 10.44
b = 0.0 
c = -10.345

print(a,type(a))         # any value except "0" negative or posiitve is True (0 is False) (same with float)
print(b,type(b))
print(c,type(c))

a = bool("India")
b = bool("10")
c = bool('-10.4')
d = bool('')

print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))       # any value except " "(empty string) is True in string - boolean datatype 


'''
# operation and expression 

'''
a = "what are you"
b = " doing ? "
print(a+b)               # concatination 

a = [1,2,3]
b = [1,4,2,9]
print(a +b )             # union 


a = 10 + 13 * 2         # 10 + 26 = 36 or 23 * 2 = 46(wrong) 
print(a)                # Operator precendence 
a = (10+13) * 2         # Bracket always solves first (23)*2 = 46


# Replication 

s = "good"
print(s * 5 )           # multiplication of string is possible only with integer 

'''

# Complete operator precendence 

# parenthesis                                 ()
# exponent                                    **
# bitwise Nor                                 ~X
# mul,div,floor div, mod                      * / // %    
# add, subs                                   + - 
# bitwise and                                 & 
# bitwise not                                 ^
# bitwise or                                  |
# comparison, identity operators              < <= > >= = == != is is not
# logical operator                            not 
# logical operator                            and 
# logical operator                            or 
# if else 
# lambda 
# =,+=,-=,*=,/=

# In case when two operator have same operator precendence python follows the concept of associativity 
'''
# For exponents - right to left 
print(2**3**2) # 2**9 = 512 

# For others - left to right 
print(5*2//3) # 10//3 = 3
'''

# Arithematic operator in python (+ - / * // % **)

'''
print("addition :", 12+12)
print("substraction:", 1 - 23)
print("multiplication:", 23 * 2) 
print("division:", 7 /5)

print("floor division", 7//5)           # removes the point values 
print("modulus",7%5)                     # gives remainder of the division
print("exponentiation:", 6**2)           #  6 ^ 2 

'''
# Relational operator (< > <= >= == !=)
# Relational operator always returns a Boolean value 

'''
print(5>10)
print(5<10)
print(5>=10)
print(5<=5)              
print(10 == 10)
print(10 != 10)

'''

# Logical operators  (and , or ,not)

'''
# both operators should be True for True else False 
print (True and True)                    
print (True and False)
print (False and True )
print (False and False)

# atleast one should be True to print True 
print (True or True)                    
print (True or False)
print (False or True )
print (False or False)

# not 
print(not(True))
print(not(False))
print(not True)

'''

# Strings - Strings are immutable sequence of unicode characters defined by(single quotes'')(duoble quotes" ") and (triple code ''' ''')

'''
# String characteristics
# Ordered 
# immutable 
# allows duplicates 

# String operations 

# concatenation 
print('ab'+'bd')

# repetition 
print('ac'*3)

# membership 
print('a' in 'ac')

# comparison - lexicographical comparison(based on unicode)
print('ac'>'ad')


# String functions-
s = 'bacdefgih'

# len()
print(len(s))

# ord()- shows the unicode value of the string(only for single character)
print(ord('s'))

# max()- based on the unicode value 
print(max(s))

# min()- based on the unicode value 
print(min(s))

# chr()- shows the character when the unicode value is passed(Exactly opposite of ord())
print(chr(104))

# String Method:

s1 = 'My name is kaif and I live in INDIA '

# upper()- capitalizes all of the string
print(s1.upper())

# lower()- makes all the string value small
print(s1.lower())

# capitalize()- makes the first element of the string capital 
print(s1.capitalize())

# title()- Makes the first letter of every word in the string capital 
print(s1.title())

# swapcase()- swap the case of all the charcxter in the string i.e, lowecase becomes uppercase and viceversa 
print(s1.swapcase())

# split()- creates a list by splitting the words from the given parameter (by default - space ' ')
print(s1.split())

# join()- joins the list using the parameter given 
l = ['study','iitm.ac.in']
print('@'.join(l))

# count()- COunts the number of time the letter has appeared in the string 
print(s1.count('a'))

# find()- finds index of the element in the given string, in case of more appearance it returns the first index 
print(s1.find('a'))
print(s1.find('z'))# find the element is not present in the string, it returns -1

# strip()- Removes the spaces or any character from behind and ahead of the string
s2 = '     ........HELLO WORLD     .....'
print(s2.strip())# in case no character is given by default it strips empty space ' '
print(s2.strip('.'))# in case the parameter is given it removes that paramter from behind and ahead of the string 

# startswith()/endswith()- checks if the string starts or ends with the given parameter and return boolean result
print(s1.startswith("My"))
print(s1.startswith("my"))

print(s1.endswith('india'))
print(s1.endswith('INDIA '))# space is also included 


s3 = 'abcdef'
s4 = '1234'
s5 = '123abc'
s6 = '@abc'
s7 = 'e12'

# isalpha()- returns true if there is only aplhabet in the string else false 
print(s3.isalpha())
print(s4.isalpha())
print(s5.isalpha())
print(s6.isalpha())
print(s7.isalpha())
print()

# isalnum()- returns true if the strings contain either alphabet or number or both else false
print(s3.isalnum())
print(s4.isalnum())
print(s5.isalnum())
print(s6.isalnum())
print(s7.isalnum())
print()

#isdigit()- returns true if there is only digits in the string else false 
print(s3.isdigit())
print(s4.isdigit())
print(s5.isdigit())
print(s6.isdigit())
print(s7.isdigit())
print()
'''

# String Slicing 

'''
s = "coffee"
t = "bread"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])


st = "python" 
print(st[::])#python- by default value is 0 to len(st) and step=1
print(st[0:5])#pytho
print(st[0:5:1])#pytho
print(st[0:5:2])#pto
print(st[5:0:-1])#nohty
print(st[5:0:-2])#nhy
print(st[5:0])# nothing
print(st[-6:3])#pyt
print(st[-6:3:2])#pt

'''

#String reversing using slicing

'''
h = "python"
print(h[::-1])
print(h[-1:-7:-1])

'''
# Negative indexing 

'''
print(s[-1])                # e
print(s[-2])                # e 
print(s[-3])                # f
print(s[-4])                # f 
print(s[-5])                # o
print (s[-6])               # c

# lenght function in string 

print (len(s))             # lenght or total character of string (doesn't start with zero)


print(s[0:5])              # includes lower index and exclude upper index 
print(s[0:6])

a = "0123456789"
c = a[4]
b = a[7]
print(c+b)            # concatination (because of string value)

d = int(c)
e = int(b)
print(d + e)          # addition because of integer value 

'''
# String comparison 
'''
s = "India"
print(s == "India")
print(s == "india")           # Python is case sensitive 


print ("apple" > "one")       # Computer starts comparison letter by letter in string (alphabetical order)
print ("four" < "ten")
print ("ab" < "az")           # first letter is same so the second letter is compared 
print ("abcde" < "abcdef")    # f cannot is less than nothing 

'''
# The string comparison is based on the unicode of the string character 
# Ord function : This is a built in function in python to check the unicode of the character
'''
print(ord("a"))   
print(ord("A"))
print(ord("b"))
print(ord("9"))
print(ord("K")) 
'''

#Line continuation 

'''
total = 1+2+3+4+5+6+\
7+8+9
print(total)

'''

# Substrings 
# A string is a substring  of another string if the first string is contained in the second 
# In operator 
'''
a = "good"
b = "very good "
print(a in b)
print(b in a)

'''

# Cases where the boolean datatype returns false 

'''
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(0+0j))
print(bool(0j))
print(bool())
print(bool([]))
print(bool(''))
print(bool(""))
print(bool({}))
# Except these cases the bool always return true 

'''
# incerment operator 
'''
a = 10
print(++a)   # ++ = +10 
print(--a)   # -- = +10 
print(-+a)   # -+ = -10 

'''

# identity operator (is and not is)

'''
a = 10 
b = 20 
c = 10 

print(a is b)              # Check whether both variable store the same value or not 
print(a is c)
print(a is not b)

# id function : Used to check the reference location of a variable 

print(id(a))
print(id(b))
print(id(c))               # Here both a and c have same id because they both refer to same value 

'''

# Diiference between (is) identity operator and ==(comaprison) operator 
'''
# equality operator is used to compare the values 
# identity operator is used to compare the IDs.

a = 20 
b = 20 
print(a is b)#True 
print(a == b)#True 

x = [1,2,3]
y = [1,2,3]
print(x is y)#False 
print(x ==y)#True 
print(id(x))
print(id(y))

'''

# Week 1 completed 