
print("===== STUDENT RESULT CALCULATOR =====")

# Student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Enter subject marks
subjects = ["English", "Physics", "Chemistry", "Mathematics", "Computer"]

marks = []

for subject in subjects:
    mark = float(input(f"Enter marks in {subject} (out of 100): "))
    marks.append(mark)

# Calculate result
total = sum(marks)
percentage = total / len(subjects)

# Display result
print("\n========== STUDENT RESULT ==========")
print("Student Name:", name)
print("Roll Number:", roll_no)

print("\nSubject-wise Marks:")

for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

print("\nTotal Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")

# Grade calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Final result
if min(marks) >= 33:
    print("Result: PASS")
    print("Grade:", grade)
else:
    print("Result: FAIL")
    print("Grade: F")

print("====================================")
