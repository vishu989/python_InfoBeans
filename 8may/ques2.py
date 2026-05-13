import math

n = int(input("Enter N: "))

for i in range(1, n + 1):
    print(i, "Square =", i**2, "Cube =", i**3, "Square Root =", round(math.sqrt(i), 2))