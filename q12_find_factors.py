# q12_find_factors.py

n = int(input("Enter number: "))
m = 2
former = True

while n >= m:
    if n % m == 0:
        n = n / m
        if former == True:
            print(m, end='')
            former = False
        else:
            print(",", m,  end='')
    else:
        m = m + 1
print()
