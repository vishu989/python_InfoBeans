n = int(input("Enter n: "))

for i in range(n, 1, -1):
    print(" " * (n - i), end="")

    for j in range(i, 0, -1):
        print(j, end="")

    print()