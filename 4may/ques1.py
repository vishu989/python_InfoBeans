num = input("Enter number: ")

diffs = []
even_count = 0

for i in range(len(num) - 1):
    d1 = int(num[i])
    d2 = int(num[i+1])
    diff = abs(d1 - d2)
    diffs.append(diff)

    if diff % 2 == 0:
        even_count += 1

print("Differences:", *diffs)
print("Even Differences Count =", even_count)
print("Max Difference =", max(diffs))

# Check uniform
if all(d == diffs[0] for d in diffs):
    print("Uniform Difference")
else:
    print("Non-Uniform Pattern")
