text=input("Enter")
vowels="aeiouAEIUO" 
count=0 
for char in text: 
    if char in vowels: 
        count=count+1  
print("no of vowels",count) 