grade_points = {"A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
                "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0}

grades = []
total_grade_points = 0
num_grades = 0

while True:
    grade = input("Enter a letter grade (or press Enter to finish): ").upper()

    if grade == "":
        break 
    #use dict, recall from list and bind into grade
    grade_point = grade_points.get(grade, None)
    
    if grade_point is not None:
        total_grade_points += grade_point
        num_grades += 1
    else:
        print(f"Invalid grade entered: {grade}")
        # invalid if user entered other letter, example: Z, T,...
# calc and print GPA
if num_grades > 0:
    gpa = total_grade_points / num_grades
    print(f"The Grade Point Average (GPA) is: {gpa:.2f}")
else:
    print("No grades entered.")
