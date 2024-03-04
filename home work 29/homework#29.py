# """
# - Decorators -
# A. Write a decorator function print_decorator that prints a message 
# before and after the decorated function is called. The message should 
# indicate the start and end of the function call. Apply this decorator 
# to a function named example_function that takes no arguments and simply 
# prints "Hello, world!".
def print_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("Finish")
    return wrapper

@print_decorator
def example_function():
    print("Hello, world!")

example_function()

# B. Write a decorator function star_decorator that decorates the output 
# of the decorated function with a pattern of "*****" before and after the output.
# Apply this decorator to a function named example_function that takes 
# no arguments and simply returns the string "Hello, Decorators!".
def star_decorator(func):
    def wrapper():
        result = func()
        decorated_result = f"*****\n{result}\n*****"
        return decorated_result
    return wrapper

@star_decorator
def example_function():
    return "Hello, Decorators!"

result = example_function()
print(result)

# C. Write a decorator function that is used to double the output of the
# decorated fucntion.
def double_output_decorator(func):
    def wrapper():
        result = func()
        doubled_result = result * 2
        return doubled_result
    return wrapper

@double_output_decorator
def example_function():
    return "Hello"

result = example_function()
print(result)

# Quiz.
# 1. What is a decorator in Python?
#     a) A design pattern used in object-oriented programming.
#     = b) A function that takes another function and extends its behavior without modifying the function itself.
#     c) A built-in Python feature used to create graphical interfaces.
#     d) A method to add attributes to a class.

# 2. Which symbol is commonly used to denote a decorator in Python?
#     = a) @
#     b) #
#     c) $
#     d) !
    
# 3. What is the purpose of a decorator?
#     = a) To modify the behavior of an existing function without modifying the function itself.
#     b) To create a new function.
#     c) To remove a function's behavior.
#     d) To replace an existing function.
    
# 4. Which of the following is a valid use case for decorators?
#     a) Adding a new method to a class.
#     b) Reducing code complexity by removing functions.
#     = c) Adding additional functionality to an existing function.
#     d) Creating a new class instance.

# 5. In Python, can a function have multiple decorators?
#     = a) Yes
#     b) No
    
# 6. When using multiple decorators on a function, in which order are they applied?
#     = a) From top to bottom, starting with the innermost decorator.
#     b) From bottom to top, starting with the innermost decorator.
#     c) It's random.
#     d) It's not possible to use multiple decorators on a single function.

# 7. Which of the following is true about decorator functions?
#     = a) They can accept arguments.
#     b) They cannot return values.
#     c) They cannot be nested.
#     d) They can modify the decorated function.
    
# 8. What is a closure in Python?
#     a) A function that takes no arguments.
#     = b) A nested function that captures and remembers the environment in which it was created.
#     c) A function that takes multiple arguments.
#     d) A function that returns a class instance.
    
# 9. Which of the following is a correct way to use a decorator?
#     = a) @my_decorator
#     b) @my_decorator()
#     c) @my_decorator(argument)
#     d) my_decorator()

# 10. What will be the output of the code?
def star_decorator(func):
    def wrapper():
        print("*****")
        func()
        print("*****")
    return wrapper

@star_decorator
def greet():
    print("Hello, world!")

greet()

#     = a) ***** Hello, world! *****
#     b) Hello, world!
#     c) *****
#     d) ***** Hello, world!

# 11. What will be the output of the code?
def repeat_decorator(func):
    def wrapper():
        func()
        func()
    return wrapper

@repeat_decorator
def say_hello():
    print("Hello!")

say_hello()

#     = a) Hello! Hello!
#     b) Hello!
#     c) Hello! Hello! Hello!
#     d) Hello! Hello!
# """