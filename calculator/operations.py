# My code
from decimal import Decimal
# Define the arithmetic functions here
def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b



# professor code
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

