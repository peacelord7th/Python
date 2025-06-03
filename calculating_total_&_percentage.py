Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # Accept marks for 5 subjects
>>> subject1 = float(input("Enter marks for subject 1: "))
Enter marks for subject 1: 76
>>> subject2 = float(input("Enter marks for subject 2: "))
Enter marks for subject 2: 77
>>> subject3 = float(input("Enter marks for subject 3: "))
Enter marks for subject 3: 87
>>> subject4 = float(input("Enter marks for sbuject 4: "))
Enter marks for sbuject 4: 88
>>> subject5 = float(input("Enter marks for subject 5: "))
Enter marks for subject 5: 99
>>> 
>>> # Calculate total and percentage
>>> 
>>> total_marks = subject1 + subject2 + subject3 + subject4 + subject5
>>> percentage = (total_marks / 500) * 100 # Assuming each subject is out of 100
>>> 
>>> # Display total and percentage
>>> 
>>> print(f"Total Marks: {total_marks}")
Total Marks: 427.0
>>> print(f"Percentage: {percentage}%")
Percentage: 85.39999999999999%
