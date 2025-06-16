# calculator_calculations.py

# -----------------------------------------------------------------------------------
# Import Statements
# -----------------------------------------------------------------------------------

# Import ABC (Abstract Base Class) and abstractmethod from Python's abc module.
# Abstract Base Classes (ABCs) allow us to define a contract for our subclasses, specifying 
# methods that they must implement. This helps in establishing a standard interface for 
# similar objects without enforcing specific details on how they should work.
from abc import ABC, abstractmethod

# Import the Operation class from the app.operation module. 
# The Operation class is where our basic mathematical functions (e.g., addition, subtraction) are defined.
# Rather than implementing arithmetic logic within each calculation class, we encapsulate it in a 
# separate class to promote modularity. This makes it easier to modify or extend these functions independently.
from app.operation import Operation

# Abstract Base Class: Calculation
class Calculation(ABC):
    """
    Abstract base class defining a common interface for all calculator operations.

    Purpose:
    - Enforces a consistent structure via the abstract `execute` method.
    - Supports abstraction and polymorphism, allowing interchangeable use of subclasses.
    - Ensures each calculation type implements its own logic.
    """

    def __init__(self, a: float, b: float) -> None:
        """
        Initializes a Calculation instance with two operands (numbers involved in the calculation).
        
        **Why Have an Initializer?**
        - This initializer method ensures that each Calculation object will have two numbers (`a` and `b`) 
          to work with, no matter the specific type of calculation.
        - Encapsulating the operands within an instance allows each Calculation object to maintain its own 
          state (values of `a` and `b`), supporting **Object-Oriented Design** principles.

        **Parameters:**
        - `a (float)`: The first operand.
        - `b (float)`: The second operand.
        """
        self.a: float = a # stores first operand as floating point number
        self.b: float = b # stores second operand as floating point number

    @abstractmethod
    def execute(self) -> float:
        """
        Abstract method to perform the calculation. Subclasses will provide specific 
        implementations of this method, defining the arithmetic for each operation.

        **Why Use an Abstract Method?**
        - Enforces that each subclass provides its own specific version of `execute`, 
          which is crucial for following the interface defined by Calculation.
        - Abstract methods define "must-have" methods for subclasses. By including `execute` here, 
          we ensure that any class inheriting from Calculation will have this method, making 
          it easier to work with multiple types of calculations in a flexible way.
        
        **Returns:**
        - `float`: The result of the calculation.
        """
        # In Python, the comment # pragma: no cover is used in the context of code coverage tools, 
        # like coverage.py, to tell the tool:
        # “Ignore this line when calculating test coverage.”
        pass # actual implementation will be provided by the subclass # pragma: no cover

    def __str__(self) -> str:
        """
        Provides a user-friendly string representation of the Calculation instance, 
        showing the operation name, operands, and result. This enhances **Readability** 
        and **Debugging** by giving a clear output for each calculation.

        **Returns:**
        - `str`: A string describing the calculation and its result.
        """
        # run the calculation to get the result
        result = self.execute()

        # It gets the name of the class the current object belongs to (like "AdditionCalculation"), 
        # then removes the word "Calculation" from that name. So "AdditionCalculation" becomes just "Addition".
        operation_name = self.__class__.__name__.replace('Calculation', '')

        # It creates and returns a formatted string that looks like this:
        # ClassName: a OperationName b = result
        # For example: "AdditionCalculation: 5 Addition 3 = 8"
        return f"{self.__class__.__name__}: {self.a} {operation_name} {self.b} = {result}"
    
    def __repr__(self) -> str:
        """
        Provides a technical, unambiguous representation of the Calculation instance 
        showing the class name and operand values. This is useful for debugging 
        since it gives a clear and consistent format for all Calculation objects.

        **Returns:**
        - `str`: A string containing the class name and operands.
        """

        # If you have an object of class AdditionCalculation where a = 5 and b = 3,
        # this would return the string: "AdditionCalculation(a=5, b=3)"
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"
    
# factory class: CalculationFactory
class CalculationFactory:
    """
    The CalculationFactory is a **Factory Class** responsible for creating instances 
    of Calculation subclasses. This design pattern allows us to encapsulate the 
    logic of object creation and make it flexible.

    **Why Use a Factory Class?**
    - **Single Responsibility Principle (SRP)**: The factory only deals with object creation. 
      This keeps our code organized, as the logic for creating different calculations is 
      separated from the calculations themselves.
    - **Open/Closed Principle (OCP)**: We can add new calculation types without changing 
      the existing codebase. We simply register new calculation classes, making our 
      code extensible and flexible to future modifications.
    """

    # _calculations is a dictionary that holds a mapping of calculation types
    # like "add" or "subtract" to their respective classes.
    _calculations = {}


    @classmethod
    def register_calculation(cls, calculation_type: str):
        """
        This method is a decorator used to register a specific Calculation subclass 
        under a unique calculation type. Registering classes with string identifiers 
        like "add" or "multiply" enables easy access to different operations 
        dynamically at runtime.

        **Parameters:**
        - `calculation_type (str)`: A short identifier for the type of calculation 
          (e.g., 'add' for addition).
        
        **Benefits of Using a Decorator for Registration:**
        - **Modularity**: By using a decorator, we can easily add new calculations by 
          annotating new subclasses with `@CalculationFactory.register_calculation`.
        - **Dynamic Binding**: This approach binds each calculation type to a class dynamically, 
          allowing us to extend our application without altering the core logic.
        """

        # subclass means the class that the decorator is being applied to.
        # ex: AdditionCalculation is a subclass, "add" is the key (string)
        def decorator(subclass):
            # converts calculation_type to lowercase to ensure consistency
            calculation_type_lower = calculation_type.lower()

            # checks if the calculation type has already been registered to avoid duplication
            if calculation_type_lower in cls._calculations:
                raise ValueError(f"Calculation type '{calculation_type}' is already registered.")
            
            # register the subclass in the _calculations dictionary
            cls._calculations[calculation_type_lower] = subclass
            return subclass # return the subclass for chaining or additional use
        
        return decorator # return the decorator function
    
    @classmethod
    def create_calculation(cls, calculation_type: str, a: float, b: float) -> Calculation:
        """
        Factory method that creates instances of Calculation subclasses based on 
        a specified calculation type.

        **Parameters:**
        - `calculation_type (str)`: The type of calculation ('add', 'subtract', 'multiply', 'divide').
        - `a (float)`: The first operand.
        - `b (float)`: The second operand.
        
        **Returns:**
        - `Calculation`: An instance of the appropriate Calculation subclass.

        **How Does This Help?**
        - By centralizing object creation here, we only need to specify calculation types 
          as strings, making it easy to choose different calculations dynamically. 
        - **Error Handling**: If the specified type is not available, we provide a 
          clear error message listing valid options, helping prevent errors and 
          ensuring the user knows the supported types.
        """
        calculation_type_lower = calculation_type.lower()

        # The dict.get() method tries to retrieve the value (the class) associated with the given key 
        # (calculation_type_lower).
          # If the key exists, it returns the associated class (like AddCalculation).
          # If the key does not exist, it returns None (instead of raising an error like dict[] would).
        calculation_class = cls._calculations.get(calculation_type_lower)
        # If the type is unsupported, raise an error with the available types.
        if not calculation_class:
            available_types = ', '.join(cls._calculations.keys())

            # this is 've' in the print(ve) line!!
            raise ValueError(f"Unsupported calculation type: '{calculation_type}'. Available types: {available_types}")
        # Create and return an instance of the requested calculation class with the provided operands.
        return calculation_class(a, b)    
    
# difference between registering a class and creating a class:
    # register: You store a reference to a class (not an object) somewhere
        # usually in a dictionary or registry — so you can look it up later by a key (like a string).
    # create: You create an object (instance) 
        # from a class by calling the class like a function, passing any needed data (like operands).
    # Registering is like putting a book title and its author on a library catalog card.
    # Creating is like pulling that book off the shelf to actually read it.


# -----------------------------------------------------------------------------------
# Concrete Calculation Classes
# -----------------------------------------------------------------------------------

# Each of these classes defines a specific calculation type (addition, subtraction, 
# multiplication, or division). These classes inherit from Calculation, implementing 
# the `execute` method to perform the specific arithmetic operation. 

# You need that decorator function to use the decorator syntax with @.
# Without it, you’d have to register classes manually, e.g.,
# CalculationFactory._calculations["add"] = AdditionCalculation
@CalculationFactory.register_calculation('add')
class AddCalculation(Calculation):
    """
    AddCalculation represents an addition operation between two numbers.
    
    **Why Create Separate Classes for Each Operation?**
    - **Polymorphism**: Each calculation type can be used interchangeably through the `execute` method.
    - **Modularity**: Encapsulating each operation in a separate class makes it easy to 
      modify, test, or extend without affecting other calculations.
    - **Clear Responsibility**: Each class has a clear, single purpose, making the code easier to read.
    """

    def execute(self) -> float:
        # calls the addition method from the Operation module to perform the addition
        return Operation.addition(self.a, self.b)
    
@CalculationFactory.register_calculation('subtract')
class SubtractCalculation(Calculation):
    """
    SubtractCalculation represents a subtraction operation between two numbers.
    
    **Implementation Note**: This class specifically handles subtraction, keeping 
    the implementation separate from other operations.
    """

    def execute(self) -> float:
        # calls the subtraction method from the Operation module
        return Operation.subtraction(self.a, self.b)
    
@CalculationFactory.register_calculation('multiply')
class MultiplyCalculation(Calculation):
    """
    MultiplyCalculation represents a multiplication operation.
    
    By encapsulating the multiplication logic here, we achieve a clear separation of 
    concerns, making it easy to adjust the multiplication logic without affecting other calculations.
    """

    def execute(self) -> float:
        # calls the multiplication method from the Operation module
        return Operation.multiplication(self.a, self.b)
    
@CalculationFactory.register_calculation('divide')
class DivideCalculation(Calculation):
    """
    DivideCalculation represents a division operation.
    
    **Special Case - Division by Zero**: Division requires extra error handling to 
    prevent dividing by zero, which would cause an error in the program. This class 
    checks if the second operand is zero before performing the operation.
    """

    def execute(self) -> float:
        # before performing division, check if b is zero to avoid ZeroDivisionError
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        
        # calls the division method from Operation module
        return Operation.division(self.a, self.b)
    
@CalculationFactory.register_calculation('power')
class PowerCalculation(Calculation):
    """
    MultiplyCalculation represents a multiplication operation.
    
    By encapsulating the multiplication logic here, we achieve a clear separation of 
    concerns, making it easy to adjust the multiplication logic without affecting other calculations.
    """

    def execute(self) -> float:
        # call the power method from the Operation module
        return Operation.power(self.a, self.b) # pragma: no cover