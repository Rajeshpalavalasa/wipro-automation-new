import csv
import json
import pytest

# -------------------------
# Employee Data Handling
# -------------------------

def read_employees(filename):
    employees = []
    try:
        with open(filename, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(row)
    except Exception as e:
        raise RuntimeError(f"File read error: {e}")
    return employees

def is_valid(employee):
    try:
        emp_id = int(employee["EmployeeID"])
        salary = int(employee["Salary"])
        name = employee["Name"].strip()
        dept = employee["Department"].strip()
        if emp_id <= 0 or salary <= 0:
            return False
        if not name or not dept:
            return False
        return True
    except (ValueError, KeyError):
        return False

def process_employees(data):
    valid = [e for e in data if is_valid(e)]
    total = len(valid)
    avg_salary = round(sum(int(e["Salary"]) for e in valid)/total, 2) if total else 0
    return valid, total, avg_salary

def write_json(filename, data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise RuntimeError(f"Write error: {e}")

# -------------------------
# Main Execution
# -------------------------

if __name__ == "__main__":
    employees = read_employees("employees.csv")
    valid, total, avg = process_employees(employees)

    print(f"Valid employees processed: {total}")
    print(f"Average salary: {avg}")

    write_json("valid_employees.json", valid)
    print("Output written to valid_employees.json")

# -------------------------
# Pytest
# -------------------------

@pytest.fixture
def sample_csv(tmp_path):
    file = tmp_path / "employees.csv"
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["EmployeeID", "Name", "Department", "Salary"])
        writer.writerow([101, "Alice", "IT", 60000])
        writer.writerow([102, "Bob", "HR", 55000])
        writer.writerow([103, "Charlie", "Finance", 0])
        writer.writerow([104, "", "Marketing", 50000])
        writer.writerow([105, "David", "IT", -45000])
        writer.writerow([106, "Eva", "HR", 52000])
        writer.writerow([107, "Frank", "", 48000])
        writer.writerow([108, "Grace", "Finance", 65000])
    return file

def test_valid_records(sample_csv):
    data = read_employees(sample_csv)
    valid, total, _ = process_employees(data)
    assert total == 4

def test_invalid_records(sample_csv):
    data = read_employees(sample_csv)
    valid, _, _ = process_employees(data)
    assert all(is_valid(e) for e in valid)

def test_average_salary(sample_csv):
    data = read_employees(sample_csv)
    _, _, avg = process_employees(data)
    assert avg == 58000

@pytest.mark.xfail(reason="Future salary normalization feature")
def test_future_validation():
    assert False
