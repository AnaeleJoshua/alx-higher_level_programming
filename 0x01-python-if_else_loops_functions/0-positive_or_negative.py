#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#if number is greater than zero, print is positive
if number > 0 :
	print(f'{number} is positive')
# if number is zero; print is zero
elif number == 0:
	print(f'{number} is zero')
#if number is less than zero, print is negative
else:
	print(f'{number} is negative')
