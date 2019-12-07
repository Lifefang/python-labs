# *************************************************************************************

print(
    "This program is going to ask the user for their homework score, exam score and whether or not they did the project")
homework = float(input("Please input the homework score:"))  # grabbing the input for homework
exam_score = float(input("Please input row_3 exam score:"))  # grabbing the input got exam score

outside_project = input("Please indicate weather or not you did the outside project with 'Yes' or row_3 'No':")
if outside_project == "Yes":  # if yes then the value of the assignment is true and +5 points
    outside_project = True

elif outside_project == 'No':
    outside_project = False
grade = (homework * .4) + exam_score * .6
if outside_project == False:
    grade = grade - 11
if outside_project == True:
    grade += 5
if grade < 60:
    print("your letter grade is:F")
if 60 < grade <= 70:
    print("your letter grade is:D")

if 70 < grade <= 80:
    print("your letter grade is:C")

if 80 < grade <= 90:
    print("your letter grade is:B")

if 90 < grade <= 105:
    print("your letter grade is:A")
print(grade)
# *************************************************************************************
