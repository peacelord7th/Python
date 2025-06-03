Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Accepting input from user
>>> 
>>> a = int(input("Enter first number: "))
Enter first number: 3
>>> b = int(input("Enter second number: "))
Enter second number: 8
>>> 
>>> # Swapping without a third variable
>>> 
>>> a = a + b
>>> b = a - b
>>> a = a - b
>>> 
>>> # Printing results
>>> 
>>> print(f"After swapping: a = {a}, b = {b}")
After swapping: a = 8, b = 3
