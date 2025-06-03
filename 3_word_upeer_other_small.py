Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#WAP to ask the user to enter the string.Display the first three characters of the string to upper case and rest in lower case.


a="Hello Wolrd, It's Me Sir, Aasbin"
clear
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    clear
NameError: name 'clear' is not defined

>>> 
>>> a=input("Enter Your Name")
Enter Your NameAasbin
>>> print(a.isuppercase("0:3"), a.islowercase("3:"))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(a.isuppercase("0:3"), a.islowercase("3:"))
AttributeError: 'str' object has no attribute 'isuppercase'
>>> a=input("enter String")
enter StringAasbin
>>> print(a.uppercase(a[0:2]), a.lowerccase(a[3:]))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(a.uppercase(a[0:2]), a.lowerccase(a[3:]))
AttributeError: 'str' object has no attribute 'uppercase'
>>> 
>>> a=inputstring("Enter It")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a=inputstring("Enter It")
NameError: name 'inputstring' is not defined
>>> a=input("aasBIN")
aasBIN
>>> print(a)

>>> a="aasBIN"
>>> print(a)
aasBIN
>>> print(a.uppercase"[0:2]")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> 
>>> 
>>> 
>>> 
>>> user_string=input("Enter String")
Enter Stringhellosabin
>>> formatted_string = user_string[:3].upper() + user_strig[3:].lower()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    formatted_string = user_string[:3].upper() + user_strig[3:].lower()
NameError: name 'user_strig' is not defined. Did you mean: 'user_string'?
>>> user_string = input("Enter a String: ")
Enter a String: helloworld
>>> formatted_string = user_string[:3].upper() + user_string[3:].lower()
>>> print("Formatted String:", formatted_string)
Formatted String: HELloworld
