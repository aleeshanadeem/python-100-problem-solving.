n = int(input("Enter the number of elements in the list: "))
count = 0
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    if element % 2 == 0:
        count += 1
print(f"The number of even elements in the list is: {count}")