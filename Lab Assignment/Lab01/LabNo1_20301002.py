#Name- Moinul Hossain Bhuiyan
# CSE 220 Section-06
#Lab Assignment 01
#===============================================

#Task_01
#Code Started
string = input ("Please Insert The Valid Integers: ")
list = string.split (",")
source = []
for i in list:
    source.append(int(i))
k=int(input("Please Insert The Valid Shift Value: "))
def shiftLeft(source,k):
    n=k
    i=0
    j=len(source)
    while i<j:
        if(n<j):
            source[i]=source[n]
        else:
            source[i]=0
        i+=1
        n+=1
shiftLeft(source,k)
print(source)
#Process finished with exit code 0
#The End

#===============================================

#Task 02
#Code Started
string = input ("Please Insert The Valid Integers: ")
list = string.split (",")
source = []
for i in list:
    source.append(int(i))
k=int(input("Please Insert The Rotate Value: "))
def leftRotation(source, k):
    b=len(source)
    for i in range(0,k,1):
        a=0
        temp=source[a]
        f=0
        while f<=(b-1):
            source[f]=source[f+1]
            f+=1
            if(f==(b-1)):
                source[f]=temp
                break
leftRotation(source,k)
print(source)
#Process finished with exit code 0
#The End

#===============================================

#Task 03
#Code Started
string = input ("Please Enter Insert The Valid Integers: ")
list = string.split (",")
source = []
for i in list:
    source.append(int(i))
size=int(input("Please Insert The Valid Size Value: "))
idx=int(input("Please Insert The Valid Index: "))
def remove (source,size,idx):
    b=len(source)
    for i in range(0,size,1):
        if(i>=idx):
            source[i]=source[i+1]
        elif(i== size-1):
            source[i]=0
remove(source, size, idx)
print(source)
#Process finished with exit code 0
#The End

#===============================================

#Task 04
#Code Started
string = input ("Please Insert The Valid Integers: ")
list = string.split (",")
source = []
for i in list:
    source.append(int(i))
size=int(input("Please Insert The Valid Size Value: "))
element=int(input("Please Insert The Valid Element: "))
def removeAll(source,size,element):
    b=len(source)
    for i in range(0, b, 1):
        if(element== source[i]):
            source[i]=0
    removedSource=[]
    for i in range(0,b,1):
        if(source[i]==0):
            continue
        else:
            removedSource.append(source[i])
    for i in range(b):
        if(i>=len(removedSource)):
            removedSource.append(0)
    return(removedSource)
source=removeAll(source,size, element)
print(source)
#Process finished with exit code 0
#The End

#===============================================

#Task 5
#Code Started
string = input ("Please Insert Valid Separated Integers: ")
list = string.split (",")
A=[]
for i in list:
    A.append(int(i))
def beam_balance(A):
    booleanmethod=False
    b=len(A)
    sum1=0
    for i in range(0,b,1):
        sum1+=A[i]
        sum2=0
        for j in range(i+1,b,1):
            sum2+=A[j]
        if(sum1==sum2):
            booleanmethod=True
            break
    return(booleanmethod)
print(beam_balance(A))
#Process finished with exit code 0
#The End

#===============================================

#Task 6
#Code Started
n=int(input("Please Insert The Number:"))
def parameter(n):
    GRP1=[]
    GRP2=[]
    for i in range(0,n,1):
        GRP1.append(0)
    for i in range(1,n+1,1):
        for j in range(0,n,1):
            if(j==(n-i)):
                GRP1[n-i]=i
                GRP2=GRP2+GRP1
    return(GRP2)
print(parameter(n))
#Process finished with exit code 0
#The End

#===============================================

#Task 7
#Code Started
string = input ("Please Insert The Valid Integers: ")
list = string.split (",")
array = []
for i in list:
    array.append(int(i))
def bunch(array):
    n=len(array)
    GRP1=[array[0]]
    GRP2=[]
    i=0
    for i in range (n):
        if i+1 < n:
            if(array[i] == array[i+1]):
                GRP1.append(array[i+1])
            else:
                GRP2.append(GRP1)
                GRP1=[]
                GRP1.append(array[i+1])
        else:
            GRP2.append(GRP1)
    grp_all=[]
    f=len(GRP2)
    for i in range(0,f,1):
        maximum=0
        for j in range(0,len(GRP2[i]),1):
            maximum+=1
        grp_all.append(maximum)
    num=max(grp_all)
    if(num==1):
        print("There is no bunch")
    else:
        print(num)
bunch(array)
#Process finished with exit code 0
#The End

#===============================================

#Task 8
#Code Started
string = input("Please Insert The Valid Integers: ")
list = string.split(",")
array = []
for i in list:
    array.append(int(i))
def repeat(array):
    a = len(array)
    GRP1 = []
    GRP2 = []
    GRP3 = []
    maximum = 0
    for i in range(0, a, 1):
        if (array[i] in GRP2):
            continue
        else:
            GRP1 = [array[i]]
            maximum = 1
            for j in range(i + 1, a, 1):
                if GRP1[0] == array[j]:
                    GRP1.append(array[j])
                    maximum += 1
            GRP2 = GRP2 + GRP1
            GRP3.append(maximum)
            GRP1 = []
            maximum = 0
            if (i + 1 < a):
                GRP1 = [array[i + 1]]
    boolean_method = False
    for i in range(len(GRP3)):
        for j in range(i + 1, len(GRP3)):
            if GRP3[i] == GRP3[j] and GRP3[i] != 1:
                boolean_method = True
    print(boolean_method)
repeat(array)
#Process finished with exit code 0
#The End

#===============================================

#Circular Arrays===

#===============================================

#Circular Array
#Task 1
#Code Started
string = input ("Please Insert The Valid Integers: ")
list = string.split (",")
array = []
for i in list:
    array.append(int(i))
start=int(input("Please Insert The Index Where to start:"))
size=int(input("Please Insert The Size:"))
def palindrome(array,start,size):
    b=len(array)
    GRP1=[]
    i=start
    a=0
    while a<size:
        GRP1.append(array[i])
        i=(i+1)%b
        a+=1
    GRP2=[]
    for i in range(len(GRP1)-1,-1,-1):
        GRP2.append(GRP1[i])
    if(GRP1 == GRP2):
        return(True)
    else:
        return(False)
print(palindrome(array,start,size))
#Process finished with exit code 0
#The End

#===============================================

#Circular Array
#Task 2
#Code Started
string = input ("Please insert the first Valid set Integers ")
list = string.split (",")
integers1 = []
for i in list:
    integers1.append(int(i))
start_1=int(input("Please Insert the Valid Index to starting:"))
size_1=int(input("Please Insert the Valid Size:"))

string2= input ("Please Insert the Valid Second set of Integers: ")
list = string2.split (",")
integers2 = []
for i in list:
    integers2.append(int(i))
start_2=int(input("Please Insert the Valid Index to starting:"))
size_2=int(input("Please Insert the Valid Size:"))
def common(integers1,integers2,size_1,size_2,start_1,start_2):
    b1=len(integers1)
    grp1=[]
    i1=start_1
    j1=0
    while j1<size_1:
        grp1.append(integers1[i1])
        i1=(i1+1)%b1
        j1+=1


    b2=len(integers2)
    grp2=[]
    i2=start_2
    j2=0
    while j2<size_2:
        grp2.append(integers2[i2])
        i2=(i2+1)%b2
        j2+=1


    grpx=[]
    for element1 in grp1:
        for element2 in grp2:
            if element1 == element2:
                grpx.append(element1)
    print(grpx)

common(integers1,integers2,size_1,size_2,start_1,start_2)
#Process finished with exit code 0
#The End

#===============================================

#Circular Array
#Task 3
#Code Started
import random

li = ["A","B","C","D","E","F","G"]

def Musical_ChairGame(m):
    temp=li[-m]
    m = li[m:]
    m = temp+m
    return m
n = 7
while n>1:
    music=[0,1,2,3]
    result=random.choice(music)
    if result==1:
        r = n//2
        value = li[r-1]
        li.remove(value)
        n-=1
        print(li)
#Process finished with exit code 0
#The End

#===============================================
#===============================================
#===============================================