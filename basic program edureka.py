# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#FILE HANDLING PROGRAM
print("Vinayagar")
fptr=open("D:\\Education\\python\\file.txt",'w+')
fptr.write("Priya is a good girl");
print(fptr.read())
fptr.close()


#PALINDROME  PROGRAM
def pal(num):
    x=num[::-1]
    if x==num:
        print('PALINDROME')
    else:
        print('NOT A PALINDROME')
        
pal('MADAM')


#FACTORIAL PROGRAM
def fact(n):
    if(n==1):
        return n
    else:
        return n*fact(n-1)
    
no=int(input('Enter the no to find factorial'))
print(fact(no))


#FIBONACCI SERIES PROGRAM
a=int(input("Enter the first no"))
b=int(input("Enter the second no"))
n=int(input("Enter the no of integer"))
print(a," ",b)

while n-2:
    c=a+b
    a=b
    b=c
    n=n-1
    print(c," ")
    
    
#ARMSTRONG NUMBER 
n=int(input("Enter the no"))
temp=n
s=0
while temp>0:
    a=temp%10
    s+=a**3
    temp//=10
if(s==n):
    print('ARMSTRONG NUMBER')
else:
    print('NOT AN ARMSTRONG NUMBER')
    
    
   
#PATTERN PROGRAM
num=5
m=(num*2)-2
for i in range(0,num):
    for j in range(0,m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
    

#LEAR YEAR
n=int(input("Enter the year"))
if n%400==0:
    print("Leap year")
elif n%4==0:
    print(" leap year")
elif n%100==0:
    print('Not a leap year')
else:
    print("Not a leap year")


#PRIME NUMBER
n=int(input("Enter the number"))
for i in range(2,n):
    if n%i==0:
        print("NOT A PRIME NUMBER")
        break
    else:
        print("PRIME NUMBER")
        break
    
#REVERSE A LIST
list=[1,2,3,4,5,6]
print(list[::-1])
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    








