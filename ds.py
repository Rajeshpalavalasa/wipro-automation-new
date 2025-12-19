food=["biriyani","Dosa","Rice","roti","burger","Pizza"]
print(food)
food.append("Chicken")
food.pop(2)
food.remove("roti")
print(food)


#squares of a number
nums=[1,2,3,4,5]
squares=[x**2 for x in nums]
print(squares)

#Dictionary
stud_marks={"Rajesh":99,"Rohit":100,"virat":99,"Ajit":10}
result={name:"Pass" if marks>60 else "failed" for name,marks in stud_marks.items()}
print(result)

capitals={'india':'Delhi',"USA":"Washington DC","china":"beijing"}
print(capitals)
print(capitals.get("Russia"))
capitals.update({"Russia":"Mosow"})
print(capitals)