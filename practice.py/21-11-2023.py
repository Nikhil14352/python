# reverse using by while loop in python
n=int(input('please give a number:'))
print("before reversing the number:%d"%n)
reverse=0
while n!=0:
    reverse=reverse*10 + n%10
    n=(n//10)
print("after reversing the number:%d" %reverse)

# reverse using string slicing in python

num=int(input("enter any number:"))
print("before using reverse method:%d"%num)
rev=int(str(num)[::-1])
print("after reversing the string:%d"%rev)

# check prime using for loop

n= int(input("enter any number:"))
i,temp=0,0
for i in range(2,n//2):
    if n%i ==0:
        temp=1
        break
    if temp ==1:
        print("given number is not prime")
    else:
        print("given number is prime")

#Armstrong number using list comprension

num = int(input("enter any number:"))
digits = [int(digit) for digit in str(num)]
count = len(digits)
sum = sum([digit ** count for digit in digits])
if num == sum:
    print("given",num, "is an armstrong number:")
else:
    print("given",num,"is not armstrong number")

#palindrome program using iterative method

n = int(input("enter any number:"))
reverse,temp=0,n
while temp!=0:
    reverse=reverse*10 + temp%10;
    temp=temp//10;
if reverse==n:
    print("number is palindrome:")
else:
    print("number is not palindrome")

# program to check given number representation is binaryor not
num = int(input("enter any number:"))
while(num>0):
    j=num%10
    if j!=0 and j!=1:
        print("num is not binary ")
        break
    num=num//10
    if num==0:
        print("num is binary")

# checking even or odd numbers

num = int(input("enter any number to check even or odd:"))
if num%2 == 0:
    print("its even")
else:
    print("its odd")

# calculate the power using for-loop

base=int(input('enter the base value:'))
exponent=int(input("enter the exponent value:"))
result=1
print(base,"to power",exponent,'=',end='')
for exponent in range(exponent,0,-1):
     result*=base
print(result)