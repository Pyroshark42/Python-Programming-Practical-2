# Q11_find_gcd.py

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

d = 2
total = 1

while d <= n1 and d <= n2:
    if n1 % d == 0 and n2 % d == 0:
        total = total * d
        n1 = n1 / d
        n2 = n2 / d
    else:
        d = d + 1

print(total)