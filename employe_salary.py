Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Accept Basic salary from the User
>>> 
>>> basic_salary = float(input("Enter the Basic Salary: "))
Enter the Basic Salary: 700000.150
>>> 
>>> # Calculate other Components of the Salary
>>> 
>>> grade_pay = 2 * basic_salary
>>> da = 0.7 * basic_salary # DA is 70% of Basic
>>> 
>>> ta = 200 #TA is fixed at RM 200
>>> 
>>> hra = 0.2 * basic_salary # HRA is 20% of Basic
>>> 
>>> # alculate total Salary
>>> 
>>> total_salary = grade_pay + da + ta + hra
>>> # Display the calculated Salary
>>> print(f"Grade Pay: RM {grade_pay}")
Grade Pay: RM 1400000.3
>>> print(f"Dearness Allowance (DA): RM {da}")
Dearness Allowance (DA): RM 490000.105
>>> print(f"Travel Rent Allowance (HRA): RM {hra}")
Travel Rent Allowance (HRA): RM 140000.03
>>> print(f"Total Salary: RM {total_salary}")
Total Salary: RM 2030200.435
