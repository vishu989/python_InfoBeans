a, b = map(int, input().split())

for i in range(a, b+1):
    if i % 10 == 5:   # check last digit is 5
        print(i, end=" ")
