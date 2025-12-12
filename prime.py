num =10
count = 0  
for i in range(1, num + 1):  
    if num % i == 0: 
        count += 1 
if count == 2:  
        print("Prime number")  
else: 
        print("Not a prime number")



def is_prime(n):
      if n<=1:
            return False
      if n<=3:
            return True
      if n%2==0 or n%3==0:
            return False
      