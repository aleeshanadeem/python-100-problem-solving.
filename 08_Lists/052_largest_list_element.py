n= int(input())
largest = 0
for i in range(n):
    element = int(input())
    if element > largest:
        largest = element
print(largest)