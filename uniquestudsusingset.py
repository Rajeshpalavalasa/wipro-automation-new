students = [
    ("Rajesh", "Palavalasa"),
    ("Rohit", "Sharma"),
    ("Rahul", "KL"),
    ("Rajesh", "Palavalasa"),
    ("Axar", "Patel"),
    ("Virat", "Kohli"),
    ("Sachin", "Tendulkar"),
    ("Yuvraj", "singh"),
    ("smrithi", "mandhana"),
    ("Ricky", "ponting"),
    ("Jasprit", "Bumrah"),
    ("Nitish", "Reddy"),
    ("Sunil", "gavaskar"),
    ("Rohit","Sharma")
]

unique_students = []
used_names = set()

for student in students:
    first_name = student[0]
    
    if first_name not in used_names:
        unique_students.append(student)
        used_names.add(first_name)

print("Students after removing duplicate first names:\n")
for s in unique_students:
    print(s)