n = int(input("Enter n: "))

space = n - 1

for i in range(1, n + 1):

    if i % 3 == 1:
        star = 1
    elif i % 3 == 2:
        star = 2
    else:
        star = 3

    print(" " * space + "*" * star)
    space -= 1