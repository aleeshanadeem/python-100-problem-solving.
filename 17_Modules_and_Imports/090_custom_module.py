#Create your own Python module containing a function, then import that function into another Python file and use it.

def add_numbers(a, b):
    return a + b
from my_module import add_numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add_numbers(num1, num2)

print("Sum:", result)