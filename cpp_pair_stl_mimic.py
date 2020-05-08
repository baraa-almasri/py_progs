#!/bin/python3
class Pair:
    first = None
    second = None

    # constructor
    def __init__(self, firstElement = None, secondElement = None):
        # reminder when giving an argument a value, it's considered as overloading
        self.first = firstElement
        self.second = secondElement

    # make_pair function
    def make_pair(self, firstElement, secondElement):
        self.first = firstElement
        self.second = secondElement

    # get function
    def get(object):
        print(object.first, "and", object.second)

    # swap function:
    @staticmethod
    def swap(pairToswap):
        # assigning old values to temp variables
        newFirst = pairToswap.second
        newSecond = pairToswap.first
        # resetting original variables
        pairToswap.first = None
        pairToswap.second = None
        # setting inverted values to original variables
        pairToswap.first = newFirst
        pairToswap.second = newSecond
        # removing new variables from memory :)
        del newFirst
        del newSecond


################################################################
################################################################

# example 1
pairEg = Pair()
pairEg.make_pair("moo", 93)

print("First pair:")
print("first: ", pairEg.first)
print("second: ", pairEg.second)
print("\nFirst pair after swapping:")

Pair.swap(pairEg)

print("first: ", pairEg.first)
print("second: ", pairEg.second)

# example 2

pairEg2 = Pair(16.8, "lol")

print("\nSecond pair:")
print("first: ", pairEg2.first)
print("second: ", pairEg2.second)
print("get() function output: ", end="")

pairEg2.get()

