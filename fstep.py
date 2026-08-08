def get_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    return grade 


def get_status(score):
    if score >= 50:
        Status = "PASS"
    else:
        Status = "FAIL"
    return Status

def get_top_student(students):
    scores = [student["score"] for student in students]
    highest = max(scores)

    for student in students:
        if student["score"] == highest:
            return student["name"]

def get_summany(students):
    passed = [student for student in students if student["score"] >= 50]

    total_passed = len(passed)
    total_failed = len(students) - total_passed
    top_student = get_top_student(students)

    return total_passed, total_failed, top_student

def print_report(students):
    print("=====================================")
    print("\t  STUDENT REPORT")
    print("=====================================")

    for student in students:
        print(f'{student["name"]} | Scores: {student["score"]} | Grade: {get_grade(student["score"])} | Status: {get_status(student["score"])}')

    print("=====================================")
    passed, failed, top_student = get_summany(students)
    print(f'PASSED: {passed}')
    print(f'FAILED: {failed}')
    print(f'TOP STUDENT: {get_top_student(students)}')


students = []

while True:
    name = input("Enter student name (or 'done' to stop): ")
    if name == "done":
        break
    score = int(input(f"Enter the score of {name}: "))
    students.append({"name": name, "score": score})

print_report(students)

