
# My code
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation
from decimal import Decimal
from typing import Callable

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        calculation = Calculation(a, b, operation)
        Calculations.add_calculation(calculation) # Assuming add_calculation is a method to append -----
        return calculation.perform()

    @staticmethod
    def add(a:Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, add)
    
    @staticmethod
    def subtract(a:Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, subtract)
    
    @staticmethod
    def multiply(a:Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, multiply)
    
    @staticmethod
    def divide(a:Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, divide)

class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def execute(self):
        return self.operation(self.a, self.b)

class Calculator:
    @staticmethod
    def add(a, b):
        calculation = Calculation(a, b, add)
        return calculation.execute()

    @staticmethod
    def subtract(a, b):
        calculation = Calculation(a, b, subtract)
        return calculation.execute()

    @staticmethod
    def multiply(a, b):
        calculation = Calculation(a, b, multiply)
        return calculation.execute()

    @staticmethod
    def divide(a, b):
        calculation = Calculation(a, b, divide)
        return calculation.execute()




# Professor code

# from calculator.calculation import Calculation
# from calculator.operations import add, subtract, multiply, divide


    
# class Calculator:
#     @staticmethod
#     def add(a,b):
#         calculation = Calculation(a, b, add) # Pass the add function from calculation
#         return calculation.get_result()
    
        
#     @staticmethod
#     def subtract(a,b):
#         calculation = Calculation(a, b, subtract) # Pass the subtract function from calculation
#         return calculation.get_result()
    
#     @staticmethod
#     def multiply(a,b):
#         calculation = Calculation(a, b, multiply) # Pass the multiply function from calculation
#         return calculation.get_result()
    
#     @staticmethod
#     def divide(a,b):
#         calculation = Calculation(a, b, divide) # Pass the divide function from calculation
#         return calculation.get_result()