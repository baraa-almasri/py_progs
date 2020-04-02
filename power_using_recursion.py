#!/usr/bin/python3
#recursion example!
def power(base, exp):
	if exp == 1:
		return base
	else:
		return base * power(base, exp - 1)

print("Program is Terminated by E.O.F!")
while True:
	number = int(input("Enter a number: "))
	exp = int(input("Enter a power: "))
	print(power(number,exp))
