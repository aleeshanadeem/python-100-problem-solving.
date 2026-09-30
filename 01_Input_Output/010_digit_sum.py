a = int(input("Enter your three-digit number:"))
print("The sum of the digits is:", a // 100 + (a // 10) % 10 + a % 10)