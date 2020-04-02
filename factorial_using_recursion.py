#!/usr/bin/python3
#recursion example!
def factorial(number):
	if number <= 1:
		return 1
	else:
		return number * factorial(number - 1)

print("Program is Terminated by E.O.F!")
while True:
	number = int(input("Enter a number: "))
	print(factorial(number))
