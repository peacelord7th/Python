Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = "yellowheart"
>>> b = a.upper()
>>> c = a.lower()
>>> final_string = b[0:3]+[3:]
SyntaxError: invalid syntax
>>> final_string = b[0:3]+c[3:]
>>> print(final_string)
YELlowheart
