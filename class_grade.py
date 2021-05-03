"""

Start.
Create list to store 5 numbers(float).
Get user's input for their grades.
Append number to the list per user input.
Sort list ascending, splice starting at second index.
Once we get top three numbers, sum them up, divide by three.
Output message to user.
End.

"""




"""

Create list

Capture input
Append number to list

Capture input
Append number to list

Capture input
Append number to list

Capture input
Append number to list

Capture input
Append number to list

"""



grades = []

grade = input("Enter first grade: ")
grades.append(float(grade))

grade = input("Enter second grade: ")
grades.append(float(grade))

grade = input("Enter third grade: ")
grades.append(float(grade))

grade = input("Enter fourth grade: ")
grades.append(float(grade))

grade = input("Enter fifth grade: ")
grades.append(float(grade))

grades.sort()

grades = grades[2:]
grades = sum(grades)

result = grades / 3

print("Average grade {0:.2f}%".format(result))
print(grades, "results", result)