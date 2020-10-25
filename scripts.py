#Say "Hello, World!" With Python

print("Hello, World!")


#Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print("Weird")
    if n % 2 == 0 and 2<=n<=5:
        print("Not Weird")
    if n % 2 == 0 and 6<=n<=20:
        print("Weird")
    if n % 2 == 0 and n>20:
        print("Not Weird")


#Python: Division


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    firstline = a//b
    secondline = a/b
    print(firstline)
    print(secondline)


#Loops

if __name__ == '__main__':
    n = int(input())
    for i in range(n) :
        print(i**2)

#Write a function

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 :
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap

#Print function

if __name__ == '__main__':
    n = int(input())
    print (*range(1, n+1), sep='')

#Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n])


#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    arr.sort(reverse=True)
    for i in range(1,n): 
        if arr[i] != arr[0]: 
            print(arr[i])
            break

#Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print("%.2f" %(sum(student_marks[query_name])/len(student_marks[query_name])))

#Lists

if __name__ == '__main__':
    n=int(input())
    lists=[]
    for i in range(n):
        el=[(x) for x in input().split(' ')]
        if el[0]=="insert":
            lists.insert(int(el[1]),int(el[2]))
        if el[0]=="remove":
            lists.remove(int(el[1]))
        if el[0]=="append":
            lists.append(int(el[1]))
        if el[0]=="sort":
            lists.sort()
        if el[0]=="pop":
            lists.pop()
        if el[0]=="reverse":
            lists.reverse()
        if el[0]=="print":
            print(lists)


#Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))


#sWAP cASE

def swap_case(s):
    return s.swapcase()

#String Split and Join

def split_and_join(line):
    # write your code here
    s = line.split()
    s = "-".join(s)
    return s


#What's Your Name?

def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")

#Mutations

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

#String Validators

if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

#Text Alignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap

def wrap(string, max_width):
    str=textwrap.fill(string,max_width)
    return str

#String Formatting

def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))

    for i in range(1, number + 1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w = width))

#Designer Door Mat


N, M = map(int,input().split())
for i in range(0,int(N/2)): 
    print(('.|.'*i).rjust(int((M-2)/2),'-')+'.|.'+('.|.'*i).ljust(int((M-2)/2),'-'))
print('WELCOME'.center(M,'-'))
for i in reversed(range(0,int(N/2))): 
    print(('.|.'*i).rjust(int((M-2)/2),'-')+'.|.'+('.|.'*i).ljust(int((M-2)/2),'-'))

#Alphabet Rangoli

def print_rangoli(size):
    # your code goes here
    str = "abcdefghijklmnopqrstuvwxyz"[0:size]
    for i in range(size-1, -size, -1):
        x = abs(i)
        line = str[size:x:-1]+ str[x:size]
        print ("--"*x+ '-'.join(line)+"--"*x)

#Capitalize!

def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s

#The Minion Game

def minion_game(string):
    # your code goes here
    voc_list = set(['a','e','i','o','u','A','E','I','O','U'])
    voc = 0
    con = 0
    n = len(string)

    for x, y in enumerate(string):
        if y in voc_list:
            voc += n-x   
        else:
            con += n-x
 
    if voc == con:
        print("Draw")
    elif voc > con:
        print("Kevin " + str(voc))
    else:
        print("Stuart " + str(con)) 

#Merge the Tools!

def minion_game(string):
    # your code goes here
    voc_list = set(['a','e','i','o','u','A','E','I','O','U'])
    voc = 0
    con = 0
    n = len(string)

    for x, y in enumerate(string):
        if y in voc_list:
            voc += n-x   
        else:
            con += n-x
 
    if voc == con:
        print("Draw")
    elif voc > con:
        print("Kevin " + str(voc))
    else:
        print("Stuart " + str(con)) 

#Find a string

def count_substring(string, sub_string):
    count = 0
    beg = 0
    while True:
        beg = string.find(sub_string, beg) + 1
        if beg > 0:
            count+=1
        else:
            return count

#Introduction to Sets

def average(array):
    # your code goes here
    s = sum(set(array))
    n = len(set(array))
    result = s/n
    return result

#Symmetric Difference

numbers1 = int(input())
set1 = set(list(map(int,input().split())))
numbers2 = int(input())
set2 = set(list(map(int,input().split())))
set3 = (set1.difference(set2)).union(set2.difference(set1))
for i in sorted(list(set3)):
        print(i)

#Set .add()

N = int(input())
S = set(input() for i in range(N))

print(len(S))

#Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
c = int(input())

for i in range(c):
    op = []
    op = input().split()
    if op[0] == 'pop':
        s.pop()
    elif op[0] == 'remove':
        s.remove(int(op[1]))
    elif op[0] == 'discard':
        s.discard(int(op[1]))
    else:
        print('not a command')

print(sum(s))

#Set .union() Operation

n1 = int(input())
pap1 = set(map(int, input().split()))
n2 = int(input())
pap2 = set(map(int, input().split()))
print(len(pap1.union(pap2)))


#Set .intersection() Operation

n1 = int(input())
pap1 = set(map(int, input().split()))
n2 = int(input())
pap2 = set(map(int,input().split()))
print(len(pap1.intersection(pap2)))

#Set .difference() Operation

n1 = int(input())
pap1 = set(map(int, input().split()))
n2 = int(input())
pap2 = set(map(int,input().split()))
print(len(pap1.intersection(pap2)))

#Set .symmetric_difference() Operation

n1 = int(input())
pap1 = set(map(int, input().split()))
n2 = int(input())
pap2 = set(map(int, input().split()))

print(len(pap1.symmetric_difference(pap2)))

#Set Mutations

n = int(input())
A = set(map(int, input().split()))
nc = int(input())
for i in range(nc):
    s = input().split()
    if s[0] == 'intersection_update':
        A &= set(map(int, input().split()))
    elif s[0] == 'update':
        A |= set(map(int, input().split()))
    elif s[0] == 'symmetric_difference_update':
        A ^= set(map(int, input().split()))
    elif s[0] == 'difference_update':
        A -= set(map(int, input().split()))
    else:
        print("error")
print(sum(A))

#The Captain's Room

K = int(input())
roomL = list(map(int, input().split()))
roomS = set(roomL)
sL = sum(roomL)
sS = sum(roomS)
var = sS*K - sL
res = var/(K-1)
print(int(res))

#collections.Counter()

from collections import Counter
X = int(input())
N = map(int,input().split())
x = int(input())
Sh = map(tuple,(map(int,input().split()) for i in range(x)))
m = 0
n = Counter(N)
for i in Sh:
    if i[0] in n.keys() and n[i[0]]>0:
        n[i[0]] = n[i[0]] - 1
        m = m + i[1]
print(m)

#Collections.namedtuple()

from collections import namedtuple
n = int(input())
Student = namedtuple('Student', input())
aM = sum([float(s.MARKS) for s in [Student(*input().split()) for i in range(n)]])
print('%.2f' %(aM/n))

#Collections.OrderedDict()

from collections import OrderedDict
n = int(input())
od = OrderedDict()
for i in range(n):  
    item = list(input().split())
    iname = ' '.join(item[:-1])
    od[iname] = od.get(iname,0) + int(item[-1])
for i, p in od.items():
    print(i, p)


#Word Order

from collections import Counter
n = int(input())
setW = set()
dictW = {}
for i in range(n):
    n1 = input()
    if n1 not in setW:
        setW.add(n1)
        dictW[n1] = 1
    else:
        dictW[n1] += 1

print(len(setW))
print(*dictW.values())

#Collections.deque()

from collections import deque
d = deque()
n = int(input())
for i in range(n):
    k = input().split()
    if k[0] == 'append':
        d.append((k[1]))
    if k[0] == 'pop':
        d.pop()
    if k[0] == 'popleft':
        d.popleft()
    if k[0] == 'appendleft':
        d.appendleft((k[1]))

#Pilling Up!

t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    min_index = l.index(min(l)) 
    left = l[ : min_index]
    right = l[min_index : ]
    if left == sorted(left, reverse = True) and right == sorted(right, reverse = False):
        print('Yes')
    else:
        print('No') 

#Calendar Module

import calendar
m,d,y = map(int, input().split())
days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print(days[calendar.weekday(y,m,d)])

#Time Delta

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    formatt = '%a %d %b %Y %H:%M:%S %z'
    t_1 = datetime.strptime(t1, formatt)
    t_2 = datetime.strptime(t2, formatt)
    return str(int(abs(t_1-t_2).total_seconds()))

#Exceptions

n = int(input())
for i in range(n):
    try:
        a,b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)

#Birthday Cake Candles

def birthdayCakeCandles(candles):
    # Write your code here
    counter = 0
    mx = max(candles)
    for i in range(len(candles)): 
        if candles[i] == mx:
            counter += 1 
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (x1 < x2 and v1 < v2) or v2-v1 == 0:
        return "NO"
    else: 
        if (x1-x2) % (v2-v1) == 0:
            return "YES"
        else:
            return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Viral Advertising

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    people = 5
    sumad = 0
    for i in range(n):
        people = int(people//2)
        sumad += people
        people *= 3
    return sumad

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Recursive Digit Sum

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    dig = list(map(int, n))
    return getDig(str(sum(dig)*k))

def getDig(n):
    if len(n) == 1:
        return n
    else:
        dig = list(map(int, n))
        return getDig(str(sum(dig)))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#Insertion Sort - Part 1

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    for i in reversed(range(1, n)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
                arrS = [str(x) for x in arr]
                print(' '.join(arrS))
        arr[j+1] = key
        arrS = [str(x) for x in arr]
        print(' '.join(arrS))
        break
        
        
        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#Insertion Sort - Part 2

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j>= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        arrS = [str(x) for x in arr]
        print(' '.join(arrS))  
           

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

#Map and Lambda Function

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a = 0
    b = 1
    count = 0
    l = []
    while count < n:
        l.append(a)
        c = a + b
        a = b 
        b = c
        count += 1
    return l

#Re.split()

regex_pattern = r"[,.]"	# Do not delete 'r'

#Zipped!

n, x = map(int, input().split())
marks = []
for m in range(x):
    marks += [map(float, input().split())]
for i in range(n):
    for s in zip(*marks):
        print(sum(s)/x)

#ginortS

s = input()
lower = []
upper = []
odd = []
even = []
for c in s:
    if c.islower():
        lower.append(c)
    if c.isupper():
        upper.append(c)
    if c.isdigit():
        if int(c)%2 == 0:
            even.append(c)
        else:
            odd.append(c)
print(''.join(sorted(lower)+sorted(upper)+sorted(odd)+sorted(even))

#Arrays

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    return numpy.array(arr,float)

#Shape and Reshape

import numpy

n = list(input().split())
rs = numpy.array(n, int).reshape(3,3)
print(rs)

#Transpose and Flatten

import numpy as np

n, m = map(int, input().split())
arr = np.array([input().strip().split() for i in range(n)], int)
print(arr.transpose())
print(arr.flatten())

#Concatenate

import numpy as np

n, m, p = map(int, input().split())
arr1 = []
arr2 = []

arr1= np.array([input().strip().split() for i in range(n)], int)
arr2= np.array([input().strip().split() for i in range(m)], int)

print(np.concatenate((arr1,arr2), axis=0))

#Zeros and Ones

import numpy

n =tuple(map(int, input().split()))
print(numpy.zeros(n, int))
print(numpy.ones(n,int))

#Eye and Identity

import numpy

n,m = map(int, input().split())
print(str(numpy.eye(n,m)).replace('1', ' 1').replace('0',' 0'))

#Array Mathematics

import numpy

n, m = map(int, input().split())
a =[]
b =[]
for i in range(n):
    a.append(input().split())
for i in range(n):
    b.append(input().split())

a = numpy.array(a, int)
b = numpy.array(b, int)

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(a//b)
print(numpy.mod(a, b))
print(numpy.power(a, b))

