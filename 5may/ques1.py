customer = input("Enter customer type (premium/regular): ").lower()
amount = float(input("Enter purchase amount: "))

discount = (0.20 if amount > 5000 else 0.10) if customer == "premium" else (0.10 if amount > 3000 else 0.05)

final_amount = amount - (amount * discount)

print("Final Payable Amount =", final_amount)
