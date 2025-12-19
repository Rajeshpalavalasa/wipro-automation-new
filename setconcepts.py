myset={"Apple","Mango","Banana","Apple",True,1,2}
mylist=["1","2"]
myset1={"Biriryani","Pulao","Roti"}
myset.update(mylist)
print(myset)
print(myset|myset1)
print(len(myset))
for i in myset1:
    print(i)