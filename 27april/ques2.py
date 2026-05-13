a, b = map(int, input().split())

count = 0

for i in range(a, b+1):
    if i % 7 == 0:
        count += 1

print("Count =", count)
