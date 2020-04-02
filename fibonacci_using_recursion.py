#!/usr/bin/python3
#recursion example!
def fibonacci(number):
	if number == 1 or number == 0:
		return number
	else:
		return fibonacci(number - 1) + fibonacci(number - 2)

print("Program is Terminated by E.O.F!")
while True:
	number = int(input("Enter a number: "))
	print(fibonacci(number))
