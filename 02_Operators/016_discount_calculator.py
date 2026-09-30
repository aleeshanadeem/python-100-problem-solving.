a = int(input("Enter your first number: "))
b = int(input("Enter the discount percentage: "))
discount = (a * b) / 100
final_price = a - discount
print("Discount:", discount)
print("Final price:", final_price)