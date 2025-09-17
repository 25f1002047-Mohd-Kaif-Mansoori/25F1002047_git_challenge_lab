# Dictionaries 

'''

d = {}
d['sudarshan'] = 1233
d['ramya'] = 1245
d['Ravi'] = 1234

print(d)

# print(d[0]) - Error 
print(d['Ravi'])#1234

malgudi = ['it','was','monday','morning','swaminathan','was','reluctant','to','open','his','eyes','he','considered'\
        ,'monday','specially','unpleasant','in','the','calendar','after','the','delicious','freedom','of','saturday'\
        ,'and','sunday','it','was','difficult','to','get','into','the','monday','mood','of','the','work','and',
        'discipline','he','shuddered','at','the','very','thought','of','school','the','dismal','yellow ','building'
        ,'the','fire','eyed','vednayagam','his','class','teacher','and','the','headmaster','with','his'\
        ,'thin','long','cane']
print(len(malgudi))

# How to find the maximum frequency of a words(self) 
set_malgudi = set(malgudi)
print(set_malgudi,len(set_malgudi))
print()

max = 0
maxfreq = ''
dict_malgudi ={}
for word in set_malgudi:
    count = malgudi.count(word)
    dict_malgudi[word] = count 
    if count >= max:
        max = count
        maxfreq = word
print(dict_malgudi)
print(maxfreq)


print()

# How to find the max frequency word 

s = set(malgudi)
d = {}
for x in s:
    d[x] = 0
for x in malgudi:
    d[x] +=1
print(d)


'''

# List in Dictionary 

d = {}
d['sudarshan'] = [12,34,45,'sudarshan3344@iitrpr.ac.in']
d['priya'] = [11,11,11]
d['ayush'] = [39,45,33]

print(d)
print(d['sudarshan'])
print(d['sudarshan'][0])
print(d['sudarshan'][1])
print(d['sudarshan'][3])



# More on List
# Keys 

# keys can be integers, float, boolean and string
# we cannot use list and dictionary in the keys because it is mutable 
# we cannot use tuple even though it is mutable but allows to have mutable values inside it 
# Dictionary keys have to be immutable and hashable 
# Keys cannot be same for two values because they are use to access the values in a dictionary 

# Values 
# 
# values can be integers, float, boolean, string, list, dictionary, tuple, etc 
# Values can be same for two keys   
d = {'Key':'Value'}

# iteration of a dictionary 

d1 = {0:0,1:1,2:2,3:3}
print(d1)
for keys in d1:
    print(keys, d1[keys])

# Dictionary methods 

print(d1.keys())   # print a list of all the keys in a dictionary 
print(d1.values()) # prints a list of all the values in a dictionary 
print(d1.items())  # prints a list of tuples contain a couples of keys and values of dictionary 


# Functional approach(modular approach) to programming - breaking the complex code into small chunck to solve the problem 

# Example :Sorting (obvious sort)

# find out the minimum most element in the list l 
# append that to a new list 
# remove the minimum from the original list 

# Direct approach 
def obvious_sort(l):

    x =[]
    while(len(l)> 0):
        mini = l[0]
        for i in range(len(l)):
            if l[i] < mini :
                mini = l[i]
        x.append(mini)
        l.remove(mini)
    return x

l = [12,34,46,67,79,57,23,35,1,4,435,46,64,45,3,44,634,64,75,65]
print(obvious_sort(l))



# Modular approach 
# Step 1: find out the minimum most element in the list 

def min_list(l):
    mini = l[0]
    for i in range(len(l)):
        if l[i]<mini:
            mini = l[i]
    return mini 

# Step 2: append the minimum to the new list and delete it from the initial one 

def obvious_sort1(l):
    x = []
    while (len(l)>0):
        mini = min_list(l)
        x.append(mini)
        l.remove(mini)
    return x


l = [12,34,46,67,79,57,23,35,1,4,435,46,64,45,3,44,634,64,75,65]
print(obvious_sort1(l))



# Matrix Multiplication 

'''
# A: [[1,2,3],[4,5,6][7,8,9]] X B: [[10,11,12][13,14,15],[16,17,18]] = C: [[84,90,96],[201,216,231],[318,342,366]]

A = [[1,2],[3,4]]
B = [[4,5],[6,7]]

C = [[0,0],[0,0]]

dim = 2

# C[i][j] is the dot product of ith row of A and jth column of B
# Example: the C[2][1] will be the second row of A and the first column of B

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            C[i][j] += A[i][k]*B[k][j]
print(C)
        
'''

# Matrix Multiplication using Functions

# Step 1:  Initializing the matrix 
def intialize_mat(dim):
    C = []
    for i in range(dim):
        C.append([])
    for i in range(dim):
        for j in range(dim):
            C[i].append(0)
    return C

# Step 2: Finding the dot product of two matrices 
def dot_product(u,v):
    dim = len(u)
    ans = 0
    for i in range(dim):
        ans = ans + (u[i]*v[i])
    return ans 

x = [1,2,3]
y = [7,1,2]

# Step 3: Finding the rows and column of a matrix 
def row(M,i):
    dim = len(M)
    l = []
    for k in range(dim):
        l.append(M[i][k])
    return l
   
def column(M,j):
    dim = len(M)
    l=[]
    for k in range(dim):
        l.append(M[k][j])
    return l

# Step 4: Creating the matrix multiplication function
def mat_mul(A,B):
    dim = len(A)
    C = intialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j] = dot_product(row(A,i),column(B,j))
    return C

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,1],[3,1,7],[6,2,3]]
print(mat_mul(A,B))