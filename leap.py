"""
A python program that checks whether a year is leap year or not. 

1. Use Python nested if...else to solve this problem.

2. Use Python Operators

Note: A leap year is exactly divisible by 4 except for century years (years ending with 00). 
The century year is a leap year only if it is perfectly divisible by 400.
"""

#input from user and store the value in the year variable
year = int(input("Please enter the year:"))
#int()function converts whatever the user inputs into an interger

#if the all statements are true

#it is a leap year
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            
            print("%d is a leap year"%year)
            
        #if the all statements are false
        #it is not a leap year
        
        else:
            print("%d is not a leap year"%year)
    
    else:
        print("%d is a leap year"%year)
        
        #it is a leap year 

else:
    print("%d is not a leap year"%year)         
            
            

