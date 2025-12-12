a=int(input("Enter the num :"))
b=int(input("Enter thje sec num :"))2
if a>b:
      print("A is larger")
else:
      print("B is larger")

list=[1,2,3,4,5]
largest=list[0]
for n in list:
      if n>largest:
            largest=n
print(largest)

list=[1,2,3,4,5]
smallest=list[0]
for n in list:
      if n<smallest:
            smallest=n
print(smallest)

num=int(input("enter the num"))
if num%2==0:
      print("the num is even")
else:
      print("the num is odd")
      

a=4
b=6
c=8
if a>b and a>c:
      print("A is larger")
elif b>a and b>c:
      print("B is largest")
else:
      print("C is largest")  

import math
r=float(input("Enter the radius : "))
area=math.pi*r*r
print("area of circle is : "+ area)

str="helloworld"
rev=str[::-1]
print(rev)

text=str(input("enter the text :"))
vowels="aeiouAEIUO"
count=0
for char in text:
      if char in vowels:
            count=count+1
print("no of vowels"+count)

def fib(n):
      if n<=1:
            return n
      else:
            return fib(n-1)+fib(n-2)

n=int(input("enter the num"))
print("fibonacci series :")
for i in range(n):
      print(fib(i),end="")

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact*= i 

print(f"The factorial of {num} is {fact}")

nums=[2,5,3,7,5,9,1,19]
nums.sort()
print(nums)

nums=[1,2,2,2,3,3,4,5,6,6,7]
new_nums=list(set(nums))
print(new_nums)

str=input("enter the text")
rev_str=str[::-1]

if str==rev_str:
      print("its a palindrome")
else:
      print("No")

sentence=input("enter the text")
words=sentence.split()
num_words=len(words)
print(num_words)

nums=[10,20,30,40]
total=sum(nums)
print(total)

nums=[10,20,30]
total=0
for n in nums:
      total+=n
print(total)


celcius=int(input("enter the value :"))
fahrenheit=(celcius*9/5)+32
print(f"{celcius}c is equal to {fahrenheit}f")

char=input("enter a character :").lower()
if char in 'aeiou':
      print("char is vowel")
elif char.isalpha:
      print("char is a consonant")

with open("example.txt",'r') as file:
      content=file.read()
print(content)