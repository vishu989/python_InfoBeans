ch = input("Enter a character: ")

result = "Alphabet" if ch.isalpha() else "Digit" if ch.isdigit() else "Special Character"

print(result)
