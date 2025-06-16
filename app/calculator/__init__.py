"""
This module provides a professional-grade calculator that can add, subtract,
multiply, and divide numbers based on user input. It leverages the Calculation
classes for operations and includes additional features like help commands and
history tracking to enhance user experience.

This code also demonstrates two common programming paradigms in Python:
- LBYL (Look Before You Leap)
- EAFP (Easier to Ask Forgiveness than Permission)

Throughout the code, comments explain where and why these paradigms are used,
providing a comprehensive learning experience for students.
"""

import sys
import readline # enables command history and editing features
from typing import List
from app.calculation import Calculation, CalculationFactory

def display_help() -> None: # returns no value
    """
    Displays the help message with usage instructions and supported operations.
    """
    
    help_message = """
Calculator REPL Help
--------------------
Usage:
    <operation> <number1> <number2>
    - Perform a calculation with the specified operation and two numbers.
    - Supported operations:
        add       : Adds two numbers.
        subtract  : Subtracts the second number from the first.
        multiply  : Multiplies two numbers.
        divide    : Divides the first number by the second.

Special Commands:
    help      : Display this help message.
    history   : Show the history of calculations.
    exit      : Exit the calculator.

Examples:
    add 10 5
    subtract 15.5 3.2
    multiply 7 8
    divide 20 4
    """

    print(help_message)

def display_history(history: List[Calculation]) -> None: # returns no value
    """
    Displays the history of calculations performed during the session

    Parameters:
        history (List[Calculation]): A list of Calculation objects representing past calculations
    """

    if not history:
        print("No calculations performed yet.")
    else:
        print("Calculation History:")
        for idx, calculation in enumerate(history, start=1):
            print(f"{idx}. {calculation}")

def calculator() -> None: # returns no value
    """
    Professional REPL calculator that performs addition, subtraction,
    multiplication, and division using Calculation classes.

    This function demonstrates both LBYL and EAFP programming paradigms.
    """

    # initialize an empty list to keep track of calculation history
    history: List[Calculation] = []

    # welcome message to the user
    print("Welcome to the professional calculator REPL!")
    print("Type 'help' for instructions, 'history' for history of calculations, or 'exit' to quit. \n")

    # continuously prompt user to enter an operation and two numbers
    while True:
        try:
            # prompt the user to enter an operation and two numbers
            # returns entered text as string and removes leading and trailing whitespace
            user_input: str = input(">> ").strip()

            # LBYL: Look before you leap
            # before attempting to process the input, we check if its empty
            # this prevents unnecessary processing and potential errors
            if not user_input:
                # input is empty, so we skip processing and prompt again
                continue # pragma: no cover

            # makes user_input all lowercase
            command = user_input.lower()

            # LBYL is used here to check if the user input matches any special commands
            if command == "help":
                display_help()
                continue
            elif command == "history":
                display_history(history)
                continue
            elif command == "exit":
                print("Exiting calculator. Goodbye!\n")
                sys.exit(0) # exit program gracefully (instead of using 'break')

            # EAFP (easier to ask for forgiveness than permission)
            # instead of checking if the input is correctly formatted (which can be complex),
            # we attempt to parse it and handle any exceptions that arise
            try:
                # attempt to split user input into operation and operands
                operation, num1_str, num2_str = user_input.split()

                # convert operand strings into floats
                num1: float = float(num1_str)
                num2: float = float(num2_str)
            except ValueError:
                # ValueError runs if:
                    # user_input.split() doesn’t return exactly 3 parts
                    # Either operand string isn't convertible to a float
                # catches user error and handles exceptions
                # characteristic of EAFP
                print("Invalid input. Please follow the format: <operation> <num1> <num2>")
                print("Type 'help' for more information.\n")
                continue
            
            # attempt to create a Calculation instance using the factory
            try:
                calculation = CalculationFactory.create_calculation(operation, num1, num2)
            except ValueError as ve:
                # handle unsupported operations
                print(ve)
                print("Type 'help' to see the list of supported operations.\n")
                continue # prompt user again

            # attempt to execute the calculation
            try:
                result = calculation.execute()
            except ZeroDivisionError:
                # handle division error by zero specifically
                print("Cannot divide by zero!")
                print("Please enter a non-zero divisor.\n")
                continue # prompt user again
            except Exception as e:
                # Handle any other unforeseen exceptions
                print(f"An error occurred during calculation: {e}")
                print("Please try again.\n")
                continue  # Prompt the user again
        
            # prepare the result string for display
            result_str: str = f"{calculation}"
            print(f"Result: {result_str}\n")

            # append the calculation object to history
            history.append(calculation)

        except KeyboardInterrupt:
            # EAFP example for handling unexpected interruption
            # instead of checking if the user pressed Ctrl+C before each input,
            # we handle the KeyboardInterrupt exception
            print("\nKeyboard interrupt detected. Exiting calculator. Goodbye!")
            sys.exit(0)
        except EOFError:
            # exception for handling EOF (Ctrl+D)
            # similar to KeyboardInterrupt we handle the EOFError Exception
            print("\nEOF detected. Exiting calculator. Goodbye!")
            sys.exit(0)

# if this script is run directly, start the calculator REPL
if __name__ == "__main__":
    calculator() # pragma: no cover

            

            
