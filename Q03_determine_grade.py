# Q03_determine_grade.py

# Input
grade = int(input("Enter score: "))

# Programming
if grade < 0:
    print("Invalid! Score must be within 0 - 100. ")
elif grade < 35:
    print("U")
elif grade < 45:
    print("S")
elif grade < 50:
    print("E")
elif grade < 55:
    print("D")
elif grade < 60:
    print("C")
elif grade < 70:
    print("B")
elif grade < 101:
    print("A")
else:
    print("Invalid! Score must be within 0 - 100. ")