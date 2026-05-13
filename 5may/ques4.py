units = int(input("Enter units consumed: "))

bill = (units * 5) if units <= 100 else (units * 7) if units <= 300 else (units * 10)

print("Total Bill =", bill)
