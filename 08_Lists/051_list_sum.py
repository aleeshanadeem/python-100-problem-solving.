n = int(input("Enter the number of elements in the list: "))
lst = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    lst.append(element)
print(f"The sum of the elements in the list is: {sum(lst)}")