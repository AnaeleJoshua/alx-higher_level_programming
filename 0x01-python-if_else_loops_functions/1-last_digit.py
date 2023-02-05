#!/usr/bin/python3
#
import random
number = random.randint(-10000, 10000)
#convert number to str 
number = str(number)
#save last digit of string in last_digit
last_digit = number[len(number) - 1]
#convert last digit to number
last_digit = int(last_digit)
#if last digit is greater than 5, 
if last_digit >  5:
	print(f"Last digit of {number} is {last_digit} and is greater than 5 \n")
#else if string is zero
elif last_digit == 0:
	print(f"Last digit of {number} is {last_digit} and is zero\n")
#is greater than 0 but less than 6
else:
	  print(f"Last digit of {number} is {last_digit} and is greater than 0 but less than 6\n ")


