Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = "Hello"
a.capitalize()
'Hello'
print(a)
Hello
a=
SyntaxError: invalid syntax

a="hello"
a.capitalize()
'Hello'
print(a)
hello

a="hello"
b=a.capitalize()
print(b)
Hello
print(a.capitalize())
Hello


a-"hello"
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a-"hello"
TypeError: unsupported operand type(s) for -: 'str' and 'str'
print(a.count("o"))
1
a="Hello World!"
print(a.count("l",4))
1


a="Hello World"
print(a.count("l",4,9))
0


a="Hello World!"
print(a.startswith("H"))
True
a="Hello World"
print(a.startswith("e"))
False
a="Hello World"
print(a.endswith("!",2,7))
False
KeyboardInterrupt
a="Hello World"
print(a.endswith("w",2,7))
SyntaxError: multiple statements found while compiling a single statement
a="Hello World"
print(a.endswith("w",2,7))
SyntaxError: multiple statements found while compiling a single statement


a="Hello World!"
print(a.find("Hello"))
0
a="Hello World!"
print(a.find("l"))
2



a-"Hello World"
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a-"Hello World"
TypeError: unsupported operand type(s) for -: 'str' and 'str'
a
a="Hello World"
a="Hellow World!"
print(a.find("ello"))
1
print(a.find("ello"))
1


a="Hello World"
print(a.islower(),a.isupper())
False False
a="HELLOW WORLD"
print(a.islower(),a.isupper))
SyntaxError: unmatched ')'
a="HELLOW world"
print(a.islower(),a.isupper())
False False
>>> a="hellow WORLD"
>>> print(a.islower(),a.isupper())
False False
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a="hello"
>>> print(a.isalnum())
True
>>> 
>>> 
>>> a="hello"
>>> print(a.isanum())
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print(a.isanum())
AttributeError: 'str' object has no attribute 'isanum'. Did you mean: 'isalnum'?
>>> 
>>> a="hello"
>>> print(a.isalum())
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print(a.isalum())
AttributeError: 'str' object has no attribute 'isalum'. Did you mean: 'isalnum'?
>>> a="ävaASADF!"
>>> 
>>> 
>>> 
>>> a="hello!1"
>>> print(a.isalnum))
SyntaxError: unmatched ')'
>>> a="ehllo!1"
>>> print(a.isalnum())
False
>>> 
>>> 
>>> 

>>> a-""Hello world"
SyntaxError: unterminated string literal (detected at line 1)
>>> a="hello world"
>>> print(a.isalpha())
False
