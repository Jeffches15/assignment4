class Operation:
    """
    The Operation class groups basic arithmetic operations as static methods for modularity and clarity.

    **OOP Principles:**
    - **Encapsulation**: Keeps related operations together.
    - **Abstraction**: Users only interact with method names, not internal logic.
    - **Reusability**: Static methods can be used without instantiation.
    - **Organization**: Centralizes basic math functions.

    **Why Static Methods?**
    - **Stateless**: Depend only on inputs, not instance data.
    - **Accessible**: Easily callable from anywhere without creating objects.
    """

    @staticmethod
    def addition(a: float, b: float) -> float:
        """
        Adds two floats and returns the result.

        **Params:**  
        - `a`, `b` (float): Numbers to add.

        **Returns:**  
        - `float`: Sum of `a` and `b`.

        **Example:**  
        >>> Operation.addition(5.0, 3.0) → 8.0

        *Static method is used since addition doesn’t rely on instance data.*
        """
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """
        Subtracts `b` from `a` and returns the result.

        **Params:**  
        - `a`, `b` (float): Operands.

        **Returns:**  
        - `float`: Result of `a - b`.

        **Example:**  
        >>> Operation.subtraction(10.0, 4.0) → 6.0

        *Each operation is defined separately to follow the Single Responsibility Principle (SRP).*
        Each function handles one specific task (addition, subtraction, etc.) making it easier to 
        test and modify them independently
        """
        return a - b
    
    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """
        Multiply two floats and return the product.

        Parameters:
        - a (float): First number.
        - b (float): Second number.

        Returns:
        - float: Product of a and b.

        Example:
        >>> Operation.multiplication(2.0, 3.0)
        6.0

        Note:
        As a static method, this utility function can be used without creating a class instance.
        This reduces overhead and makes the methods easily reuseable in other parts of the program
        """
        return a * b
    
    @staticmethod
    def division(a: float, b: float) -> float:
        """
        Divides two floats and returns the quotient.

        Parameters:
        - a (float): Dividend.
        - b (float): Divisor.

        Returns:
        - float: Result of a / b.

        Raises:
        - ValueError: If b is zero.

        Example:
        >>> Operation.division(10.0, 2.0)
        5.0
        >>> Operation.division(10.0, 0.0)
        ValueError: Division by zero is not allowed.

        Note:
        Includes defensive error handling to prevent division by zero, which would cause a runtime error.
        Instead of letting the program fail 
        silently or crash, we handle the error gracefully, ensuring that any part of 
        the program using this function will be alerted to the issue.
        """
        if b == 0:
            # checks if the divisor is zero to prevent undefined divison
            raise ValueError("Division by zero is not allowed.") # raises an error if division by zero is attempted
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
      """
      Raises a floating-point number to the power of another and returns the result.

      **Parameters:**
      - `a (float)`: The base number.
      - `b (float)`: The exponent.
      
      **Returns:**
      - `float`: The result of `a` raised to the power of `b`.

      **Example:**
      >>> Operation.power(2.0, 3.0)
      8.0

      **Advantages of Static Methods in Utility Classes:**
      - Static methods in utility classes like this one provide simple access to functions 
        without requiring an instance of the class. This reduces overhead and makes 
        the methods easily reusable in other parts of the program.
      """
      return a ** b  # Raises a to the power of b and returns the result.