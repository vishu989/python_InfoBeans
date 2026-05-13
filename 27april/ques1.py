n = int(input("Enter a number: "))

product = 1

for i in range(1, n + 1):
    if i % 2 != 0:   # check if number is odd
        product *= i

print(product)
