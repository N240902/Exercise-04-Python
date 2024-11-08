 # Question 1: Using a for loop with a list

# # TODO: Create a list of fruit
# fruit=("banana", "orange", "mango")
# for fruit in list(fruit):

# # TODO: Use a for loop to print each fruit in the list
#     print(fruit)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
# count=6
# while count>0:
#     count -=1
#     print(count)

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
# for number in range(1,11):
#     print(number**2)


#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
# import random

# TODO: Create a list of colors
# colors=("pink", "yellow", "blue", "black")

# # TODO: Use a for loop to select and print 3 random colors from the list
# colors=("orange", "purple", "orange")
# for colors in list(colors):
#     print(colors)

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations

print(math_operations.add(2,3))

print(math_operations.subtract(2,3))

print(math_operations.multiply(2,3))

print(math_operations.divide(2,3))

# TODO: Use a while loop to create a simple calculator
