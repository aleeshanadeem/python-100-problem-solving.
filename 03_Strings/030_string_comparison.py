str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str1 == str2:
    print("Both strings are same.")
elif len(str1) > len(str2):
    print("First string is longer.")
elif len(str2) > len(str1):
    print("Second string is longer.")
else:
    print("Same length but different strings")