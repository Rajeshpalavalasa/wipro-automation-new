def calculate_total(marks):
    return sum(marks)


def calculate_average(total, subjects):
    return total / subjects


def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"


def report_card(name, marks):
    total = calculate_total(marks)
    avg = calculate_average(total, len(marks))
    grade = calculate_grade(avg)

    print("\n----- REPORT CARD -----")
    print("Student Name :", name)
    print("Marks        :", marks)
    print("Total Marks  :", total)
    print("Average      :", avg)
    print("Grade        :", grade)
