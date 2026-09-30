n = str(input("Enter a string: "))
vowels = 0
for char in n:
    if char.lower() in 'aeiou':
        vowels += 1
print("Number of vowels:", vowels)