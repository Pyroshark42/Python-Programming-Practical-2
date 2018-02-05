# Q02_triangle.py

# Input
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

# Processing
if a + b <= c:
    print("Invalid triangle! ")
elif a + c <= b:
    print("Invalid triangle! ")
elif b + c <= a:
    print("Invalid triangle! ")
else:
    output = a + b + c
    print("Perimeter =", (output))