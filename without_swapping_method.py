Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Accept two numbers from the user
>>> a = int(input("Enter the first number: "))
Enter the first number: 11
>>> b = int(input("Enter the second number: "))
Enter the second number: 33
>>> temp = a
>>> a = b
>>> b = temp
>>> print(f"After swapping (Method 1): a = {a}, b = {b}")
After swapping (Method 1): a = 33, b = 11
>>> 

# Method 2: Without using a temporary variable
a, b = b, a
print(f"After swapping (Method 2): a = {a}, b = {b}")


# Method 3: Using arithmetic operations
a = a + b
b = a - b
a = a - b
print(f"After swapping (Method 3): a = {a}, b = {b}")

