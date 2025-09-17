# WHILE LOOP 

# Program to make a password based open system 

'''
print("enter your passsword")
password = int(input())

while password != 12345678:
    print("Incorrect Password, Try again")
    password = int(input())
else:
    print("correct password")
    
'''

# Program 1 :  Program to compute the factorial of a number using while loop

'''
print('Enter the number')
num = int(input())
answer = 1 
b = 1 
# answer = answer * 2 
# answer = answer * 3 
if num < 0 :
    print('not defined')
else:
    while b <= num:
        answer = answer * b 
        b = b +1 
    print("the factorial of",num,"is",answer)
'''

# Program 1* : Program to compute the factorial of a number using while loop 

'''
print('Enter the number')
num = int(input())
fact = 1 
if num < 0 :
    print('not defined')
else:
    while num > 0:
        fact = fact * num
        num = num - 1 

    print('the factorial of',num ,'is',fact)
'''

# Program 2 : Find the number of digit in the given number 

'''
num = abs(int(input("enter number")))      # abs() or absolute function take the absolute value the the number 
digit = 1 
while num > 9 :                            # because below 9 the digit is alraeady initialised to 1 
    num = num // 10                        # removes the last digit of the number 
    digit = digit + 1                      # incrementation of the digit
print(digit)

'''

# Example to understand how floor division of 10 works (it removes the last digit)

'''
nu = 123456765431234567890
while nu > 0 :
    print(nu)
    nu = nu // 10 

'''
# Program 3 : Reverse the digits in the given number

'''
print("enter the number")
nu = int(input())
if nu >= 0:
    num = nu 
    last = num % 10 
    num = num // 10 
    reve = last 
    while num > 0:
        last = num % 10 
        num = num // 10 
        reve = reve*10 + last
    print(reve)
else:
    num = abs(nu) 
    last = num % 10 
    num = num // 10 
    reve = last 
    while num > 0:
        last = num % 10 
        num = num // 10 
        reve = reve*10 + last
    print('-',reve)
    print(reve - (2*reve))                    # double the number the subract it by the half to get the negative sign infront

'''

 # Program 3 : Reverse the digit in the given number 

'''
print("enter the number")
num = int(input())
absnum = abs(num)
rev = absnum % 10 
absnum = absnum // 10 
while absnum > 0 :
    r = absnum % 10 
    absnum = absnum // 10 
    rev = rev * 10 + r 
if num >= 0 :
    print(rev)
else: 
    print(rev-2* rev)


'''

# Program 4 : Find whether the entered number is pallindrome or not 

'''
print("enter the number")
n = abs(int(input()))
no = n 
rev = n % 10 
n = n // 10 
while n > 0 : 
    r = n % 10 
    n = n // 10 
    rev = rev * 10 + r 
if rev == no :
    print("pallindrome")
else :
    print("not a pallindrome") 

'''

# FOR LOOP 

# Program to print something multiple times using for loop 

'''
a = str(input("enter the word to print"))
x = int(input("Enter how many times you wanat to print"))

for i in range(x):
    print(i,a)
    print("##############")

    '''

# Example of for loop 

'''
print("enter a number")
n = int(input())
for i in range(n):
    if i%2 == 0:
        print(i,"Hello world")
    else:
        print(i,"Hi world")

        '''

# Range function 
# in-built function that return a range object which are useful to generate a sequence of numbers which can be casted into a sequence(list,tuple)

'''
print(range(5))
print(type(range(5)))

print(list(range(5)))
print(tuple(range(5)))

print(list(range(-2)))#[] empty list/ empty collection 

print(list(range(10,1)))#[] empty only left to right direction is alllowed 
print(list(range(-10,-1)))#[-10,-9,-8,-7,-6,-5,-4,-3,-2]

print(list(range(0,10,2)))#[0,2,4,6,8]
print(list(range(3,9,-1)))#[]
print(list(range(7,1,-2)))#[7,5,3]
print(list(range(5,10,15)))#[5]
print(list(range(2,int(12.4))))#the input in the parameter can only be integer and not zero 

'''

# Program to print the sum of first n integers 
'''
num = int(input("enter the number"))
a = 0 
for i in range(num):
    a= a + i
print(a)

'''
# Program to execute the table of "2" using for loop 

'''
for i in range(1,11):           # range function can also have lower limit here '1' 
    print("2 X",i,"=",2*i)

    '''

# Program to print a table of a number using for loop 

'''
print("enter the number")
n = int(input())
a = 1
for i in range(10):
    print(n,'X',a,'=',n*a)
    a = a + 1

    '''

# Step value in for loop 

'''
for x in range(1,11,2):         # Start,stop-1,step(jump) 
    print(x) 

# Table of 3 using the step in range function 
i = 0
for y in range(0,31,3):
    print("3 X",i,"=",y)
    i = i + 1 

    '''

# Default value for start parameter is 0 and step parameter is 1 in range function 

# Program to reverse the order of numbers 

'''
print("enter the number")
n = int(input())
for i in range(n,-1,-1):
    print(i)

    '''

# For loop without using the range function aka foreach Function 

'''
print("Enter a word")
w = str(input())
for letter in w:
    print(letter)

'''

# FORMATTED PRINTING 

# End function 
# Program to print for loop function in a single line 

for x in range(20):
    print(x, end = ' ')             # Default value is /n (new line), end = " " overwright on it to print in single line 

# Here because of previous code block the output was coming in the same line which i fixed using \n(new line)

# Sep function (seperator)

d = 23 
m = 6 
y = 2025 

print("\ntoday's date is", d,m,y) 

# Q1.problem here is that why we get a space after the d,m,y when not given in input 
# Ans1. Because the default value of sep function is a space 

# Q2. How can we add / or - in between the d,m,y
# Ans2. Using the sep function 

print("today's date is",d,m,y, sep="/")

# Q3. Problem here is that the slash also get printed in between is and date
# Ans3. Use diiferent line for seperator 

print("today's date is")
print(d,m,y,sep="/")

# Q4. Problem now is the new line 
# Ans4. use end fucntion again 

print("today's date is", end = " ")
print(d,m,y,sep="-")


# Different types of formatted printing 

# 1
'''
num = int(input("Enter a number "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

print()
'''

# 2
'''
for i in range(1,11):
    print(f"{num} X {i} = {num*i}") # f refers to formatted print 

print()
# Here every things will be considered as string, except the value in curly brackets which will be considered as variable
'''

# 3 
'''
for i in range(1,11):
    print('{0} X {1} = {2}'.format(num,i,num*i)) # this type of print referred to as print using format function  

print()
# Here every number is replaced by the equivalent value given in the format function 
# order matter 
'''

# 4 
'''
for i in range(1,11):
    print('%d X %d = %d ' % (num, i , num * i)) # this type of print is referred to as print using string modulo operator  

# %d = d stands for integers and each %d will be replaced by respective value
# This is a old way of writing print, followed in c programming 

# %s = string 
# %d = integers 
# %f = float 

'''
# Precedence handling using % operator (Round off)

'''
a = 3.141567
print("%2.4f"%(a)) #Round off to 4 decimals 
print("%2.3f"%(a)) #Round off to 3 decimals 
print("%2.2f"%(a)) #Round off to 2 decimals 

'''
# Example of formatted printing 

'''
pi = 22/7 
print(f'value of pi = {pi}')
print('value of pi = {0}'.format(pi))
print('value of pi = %f' % (pi))           # %f here refers to floor which will give fractional value also

'''
# Format specifiers 

'''
pi = 22/7 
print(f'value of pi = {pi:.3f}')              
print('value of pi = {0:.4f}'.format(pi))
print('value of pi = %.5f' % (pi))

'''
# Example of format specifiers

'''
print('{0:7d}'.format(1))             # Here :7d right align's the value to 7 spaces toward right 
print('{0:7d}'.format(11))
print('{0:7d}'.format(111))
print('{0:7d}'.format(1111))
print('{0:7d}'.format(11111))
print('{0:7d}'.format(111111))
print('{0:7d}'.format(1111111))

'''
# Problem 1: Factorial of a number using for loop (self)

'''
n = int(input("enter the number"))
a = 1
for i in range(1,n+1):
    a = a * i
print(f'the factorial of {n} is {a}')

'''

# Problem 1: Factorial of a number using for loop 

'''
num = int(input("enter a number"))
fact = 1 
if(num<0):
    print("not defined")
else:
    for i in range(num,1,-1):
        fact = fact * i 
    print(fact)

    '''
print()

# Problem 2: Find the number of digits in the given number using for loop  

'''
n = int(input("Enter the number:"))
num =str(n)
lenght = len(num)
count = 0
for i in range(lenght):
    n = n//10
    count = count + 1 
print(f'the digits in the number {num} is {count}')

'''

# Problem 2: Find the number of digits in the given number using for loop 

'''
num = abs(int(input("Enter a number:")))
strnum = str(num)
digits = 0 
for c in strnum:
    digits = digits +1 
print(digits)

'''

# Problem 3: Reverse the digits in the given number using for loop (Self) 

'''
num = int(input("enter the number"))
n = str(abs(num))
num1 = abs(num)
a = num1 % 10 
num1 = num1 // 10 
lenght = len(n)
for  i in range(1,lenght):
    a = a*10 + num1 % 10 
    num1 = num1 // 10
if num >= 0:
    print(f'the reverse of the number {n} is {a}')
else:
    print(f'the reverse of {n} is -{a}') 

'''

# Problem 3: Reverse the digits in the given number using for loop 

'''
num = int(input("enter the number:"))
absstrnum = str(abs(num))
rev = ''
for i in absstrnum:
    rev = i + rev 
if num >= 0:
    print(rev)
else:
    print('-'+rev)

'''

# Problem 4: Find whether the entered number is pallindrome or not

'''
num = int(input("enter the number"))
n = str(abs(num))
num1 = abs(num)
a = num1 % 10 
num1 = num1 // 10 
lenght = len(n)
for  i in range(1,lenght):
    a = a*10 + num1 % 10 
    num1 = num1 // 10

if a ==abs(num):
    print('Pallidrome')
else:
    print("Not a pallindrome")

'''

# Problem 4: Find whether the entered number is pallindrome or not 

'''
num = int(input("enter the number:"))
absstrnum = str(abs(num))
rev = ''
for i in absstrnum:
    rev = i + rev 
if num < 0 :
    rev = '-'+rev
if num ==int(rev):                 # we have to convert rev back to integer to compare it with the num 
    print("Pallindrome")
else:
    print("Not a pallindrome")

    '''


# Nested for loop 

'''
s = 'VIBGYOR'
t = 'VIBGYOR'
count = 0
for i in range(7):
    for j in range(7):
        print(i,j,s[i],s[j])
        count = count + 1 
print("the total ways in which the combination of two color can be done is",count)

'''

# Problem 1: Find all the prime numbers less than the entered number

'''
num = int(input("Enter a number:"))
if num >2:
    print(2,end = ' ')
for i in range(3,num):
    flag = False 
    for j in range(2,i):
        if(i%j==0):
            flag = False 
            break 
        else:
            flag = True
    if flag:
        print(i,end =' ')

print()

'''

# Problem 2: Find the total profit/loss of each trader working in a trading firm.
# Information regarding number of traders and number of transaction is unknown 
# (self)

'''
print("Enter id ")
id = input()
profit = 0
loss = 0
while id != "-1":
    print("Enter amount ")
    amount = int(input())
    while amount != 0:
        if amount > 0:
            profit = profit + amount 
        else:
            loss = loss + abs(amount)
        print("Enter next amount ")
        amount = int(input())
    print(profit - loss)
    profit = 0 
    loss = 0
    print("Enter next id ")
    id = input()   

    '''

# Problem 2: Find the total profit/loss of each trader working in a trading firm.
# Information regarding number of traders and number of transaction is unknown 

'''
emp_id = input("enter employee ID")
while emp_id != "-1":
    trade = int(input("Enter the trade amount:"))
    profit_loss = 0
    while trade != 0:
        profit_loss = profit_loss + trade 
        trade = int(input("Enter the trade amount "))
    print(f'profit/loss for employee {emp_id} is {profit_loss}')
    emp_id = input("\nEnter employee ID ")


  '''

# Problem 3: Find the day wise total rainfall for the entered duration of time e.g. week,month,month,etc.

'''
day = int(input("Enter the number of days: "))
for i in  range(1, day+1):
    total = 0 
    rainfall = int(input("Enter the rainfall "))
    while rainfall != -1:
        total = total + rainfall 
        rainfall = int(input("Enter the rainfall: ")) 
    print("total rainfall for day {0} is {10}".format(i,total))

'''

# Problem 4: Find the lenght of the longest word from the set of words entered by the user 
# self - slightly different because of misinterpretation of question 

'''
word = input("Enter the word: ")
cnt = 0 
large = 0 
for i in word:
    if i == " ":
        if cnt >= large: 
            large = cnt 
            cnt = 0 
        else:
            cnt = 0
    else:
        cnt = cnt + 1
if cnt >= large:
    large = cnt 
print(large)

'''

# Problem 4: Find the lenght of the longest word form the set of the words entered by the user 

'''
word = input("Enter the word:").strip()
maxlen = 0 
while (word != '-1'):
    count = 0 
    for letter in word:
        count = count + 1 
    if count > maxlen : 
        maxlen = count 
    word = input("Enter the word:").strip()
print("the lenght of longest word is %s" %maxlen)

'''

# break in python 

'''
email = input("Enter email")
for c in email:
    if(c =="@"):
        break       # when the if condition is true the execution of for loop stops
    print(c, end ="")        
print()

'''
# continue in python 

'''
email = input("enter email:")
for c in email:
    if c == "@":
        print()
        continue    # when the if condition is true the computer skips that iteration and moves to next character 
    print(c,end = "")
print()

'''
# pass in python 

'''
for x in range(11):
    if x%3 == 0 :
        print(x)
    else: 
        pass       # keyword pass is just a placeholder an used when we don't want to do anything 
                   # it perform no operation and is a null statement in python 

'''









