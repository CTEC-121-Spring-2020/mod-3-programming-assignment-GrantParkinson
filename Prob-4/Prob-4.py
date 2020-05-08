# Module 3
#   Programming Assignment 4
#     Prob-4.py

# <Grant Parkinson>

# Author: Bruce Elgort
# Date: July 12, 2017

"""
The Elgorte coffee shop sells coffee at $16.50 a pound
plus the cost of shipping. Each order ships for $0.76
per pound plus $1.25 fixed cost for overhead. If the
number of pounds of the coffee order exceeds 10, then
the shipping cost is waived. Write a program that
calculates the cost of an order. Name your function
coffeeProcessor()
"""


def coffeeProcessor():

    # define variables
    overHead = 1.25
    priceOfCoffee = 16.50

    # Get number of pounds from user
    # Replaced evaluate with eval
    # Added another parentheses to end of line
    # Added end quote on end of string
    # Added space to end of string to make it print prettier
    quantity = eval(
        input("How many pounds of coffee would you like to order? "))

    # Check number of pounds ordered
    # If less than or equal to 10 pounds we must charge for shipping
    # Added semicolon to end of else statement
    if quantity <= 10:
        shippingPerPound = .76
    else:
        shippingPerPound = 0

    # Calculate cost of order
    # Deleted unecessary tabs
    # Replaces "quntity" with valid variable name quantity
    # Deleted backslash
    costOfOrder = (quantity * priceOfCoffee) + \
        (quantity * shippingPerPound) + overHead

    # Print result
    # Added beginning parentheses
    print("The cost of the order is: ", costOfOrder)


# Start the program
# Deleted "go" from front of function
coffeeProcessor()
