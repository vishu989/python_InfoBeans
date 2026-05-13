start = int(input("Enter starting year: "))
end = int(input("Enter ending year: "))

print("Leap Years are:")

for year in range(start, end + 1):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year)