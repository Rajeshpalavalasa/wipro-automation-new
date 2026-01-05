# Managers and their 12 employees with performance scores
manager_employees = {
    "Manager_A": {
        "Emp1": 75, "Emp2": 60, "Emp3": 90, "Emp4": 55
    },
    "Manager_B": {
        "Emp5": 80, "Emp6": 45, "Emp7": 70, "Emp8": 65
    },
    "Manager_C": {
        "Emp9": 50, "Emp10": 85, "Emp11": 95, "Emp12": 40
    }
}

# Passing score
passing_score = 60

# Filter employees who meet the passing score using dictionary comprehension + filter + lambda
passing_employees = {
    manager: dict(filter(lambda item: item[1] >= passing_score, employees.items()))
    for manager, employees in manager_employees.items()
}

# Display the result
for manager, employees in passing_employees.items():
    print(f"{manager}:")
    if employees:
        for emp, score in employees.items():
            print(f"  {emp}: {score}")
    else:
        print("  No employees passed.")
