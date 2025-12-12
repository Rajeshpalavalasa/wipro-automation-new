# Armstrong number
num=int(input("Enter the num - "))
temp=num
sum=0
digits=len(str(num))
while temp>0:
    digit=temp%10
    sum+=digit**digits
    temp//=10
if num==sum:
    print("the num is armstrong")
else:
    print("The num isnt armstrong")