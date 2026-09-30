tuple = (10, 20, 30, 40, 50)
n = int(input())
if n in range(len(tuple)):
    print(tuple[n])
else:
    print("Index out of range")