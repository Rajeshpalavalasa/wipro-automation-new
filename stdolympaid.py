class Student:
    def __init__(self, sid):
        self.sid = sid

    def is_even(self):
        return int(self.sid[-3:]) % 2 == 0 # -3 extracts last 3 digits

    def __str__(self):  #spl method used when printing an object
        return self.sid
class Qualification:
    def __init__(self, students):
        self.students = students

    def conduct_rounds(self):
        even_stage = tuple(s for s in self.students if s.is_even())
        odd_stage = tuple(s for s in self.students if not s.is_even())
        return even_stage, odd_stage
students = tuple(
    Student(f"std_{i:03d}") for i in range(1, 11) #formats num as 3digits
)
engine = Qualification(students) #Creates a QualificationEngine object and passes all students to it.

even_ids, remaining_ids = engine.conduct_rounds()

print("Round 1 Qualified (Even IDs):")
for s in even_ids:
    print(s)

print("\nRemaining Students:")
for s in remaining_ids:
    print(s)
