salary = float(input("Enter salary: "))
exp = int(input("Enter years of experience: "))

bonus = 0.30 if exp > 10 else 0.20 if exp > 5 else 0.10

total_salary = salary + (salary * bonus)

print("Total Salary after Bonus =", total_salary)
