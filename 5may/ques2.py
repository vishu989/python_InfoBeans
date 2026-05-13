marks = int(input("Enter marks: "))

grade = "A+" if marks >= 90 else "A" if marks >= 75 else "B" if marks >= 60 else "C" if marks >= 50 else "Fail"

print("Grade =", grade)
