def get_valid_score(name):
    while True:
        try:
            score = int(input(f"Enter score for {name}: "))
            if score < 0 or score > 100:
                print("Score must be between 0 and 100!")
            else:
                break
        except:
            print("Invalid input! Please enter a number.")
    return score  # ← add this

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

# def get_grade_report(students):
#     result = [student["name"] + ": " + get_grade(student["score"]) for student in students]
#     return result 

# # print(get_grade_report(students))

def get_status(score):
    if score >= 50:
        status = "PASS"
    else:
        status = "FAIL"
    return status

def get_top_student(students):
    scores = [student["score"] for student in students]
    highest = max(scores)

    for student in students:
        if student["score"] == highest:
            return student["name"]


# print(get_top_student(students))

def get_summary(students):
    passed = [student for student in students if student["score"] >= 50]

    total_passed = len(passed)
    total_failed = len(students) - total_passed
    top_student = get_top_student(students)

    return total_passed, total_failed, top_student

# print(get_summary(students))

# def print_report(students):
#     print("==============================")
#     print("      STUDENT REPORT CARD")
#     print("==============================")

#     for student in students:
#         print(f'{student["name"]} | Score: {student["score"]} | Grade: {get_grade(student["score"])} | Status: {get_status(student["score"])}')

#     print("==============================")
#     passed, failed, top = get_summary(students)
#     print(f"Total Students : {len(students)}")
#     print(f"Passed         : {passed}")
#     print(f"Failed         : {failed}")
#     print(f"Top Student    : {top}")
#     print("==============================")

def save_report(students):
    with open("report.txt", "w") as file:
        file.write("==============================\n")
        file.write("      STUDENT REPORT CARD\n")
        file.write("==============================\n")

        for student in students:
            file.write(f'{student["name"]} | Score: {student["score"]} | Grade: {get_grade(student["score"])} | Status: {get_status(student["score"])}\n')

        file.write("==============================\n")
        passed, failed, top = get_summary(students)
        file.write(f"Total Students : {len(students)}\n")
        file.write(f"Passed         : {passed}\n")
        file.write(f"Failed         : {failed}\n")
        file.write(f"Top Student    : {top}\n")
        file.write("==============================\n")


students = []

while True:
    name = input("Enter student name (or 'done' to stop): ")
    if name == "done":
        break
    score = get_valid_score(name)
    students.append({"name": name, "score": score})
    

save_report(students)
print("Report saved to report.txt ")