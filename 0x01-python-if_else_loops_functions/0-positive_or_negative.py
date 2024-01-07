#!/usr/bin/python3
import random
number = random.randint(-10, 10)
x = number
if x < 0:
	print(x, ' is Negative')
elif x == 0:
	print(x, ' is Zero')
else:
	print(x, ' is Positive')
