n = int(input())

remove = []
for i in range(n):
    element = int(input())
    if element not in remove:
        remove.append(element)
print(remove)