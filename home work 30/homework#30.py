# """
# - Decorators -
# A. Create a decorator named @my_decorator that simply prints a message 
# before and after the decorated function is called.
def my_decorator(func):
    def wrapper():
        print("Hello")
        func()
        print("Python")
    return wrapper

@my_decorator
def example_function():
    print("World")

example_function()

# B. Modify the my_decorator from task 1 to accept arguments. The decorator 
# should be able to take arguments like a message and print it before and 
# after the decorated function is called.
def my_decorator(message):
    def decorator(func):
        def wrapper():
            print(message)
            func()
            print(message)
        return wrapper
    return decorator

@my_decorator("Hello")
def example_function():
    print("World")

example_function()

# C. Create a decorator named @timer that measures the time it takes for a 
# decorated function to run. Print the elapsed time in seconds.
import time
def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
    return wrapper

@timer
def example_function():
    time.sleep(2)
    print("Hello")

example_function()

# D. Extend the timer decorator from Task C to accept a parameter specifying 
# the time units (e.g., seconds, milliseconds, microseconds) for printing the 
# elapsed time.
import time

def timer(time_unit='milliseconds'):
    def decorator(func):
        def wrapper():
            start_time = time.time()
            func()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000

            print(elapsed_time, time_unit)
        return wrapper
    return decorator

@timer()
def example_function():
    time.sleep(2)
    print("Hello")

example_function()

# E. Implement a decorator @log_calls that logs function calls, including 
# function name, arguments, and return value.
def log_calls(func):
    def wrapper(*args):
        result = func(*args)
        return result
    return wrapper

@log_calls
def example_function(x, y):
    return x + y

result = example_function(3, 4)
print(result)

# F. Create multiple decorators and demonstrate how they can be chained to 
# decorate a single function.
def decorator1(func):
    def wrapper():
        print("Hello")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("World")
        func()
    return wrapper

def decorator3(func):
    def wrapper():
        print("Python")
        func()
    return wrapper

@decorator1
@decorator2
@decorator3
def example_function():
    print("Hello")

example_function()

# G. Implement a decorator @check_authentication that checks if a user is 
# authenticated before calling the decorated function. If authenticated, 
# allow the function to execute; otherwise, print an authentication error message.
# Assume this is a function that checks if a user is authenticated
def is_authenticated(user):
    return user.get("is_authenticated")

def check_authentication(func):
    def wrapper(user, *args):
        if is_authenticated(user):
            return func(user, *args)
        else:
            print("Authentication error")
    return wrapper

@check_authentication
def sensitive_operation(user):
    print(f"{user['username']} is authenticated")

authenticated_user = {"username": "Rasim", "is_authenticated": True}
unauthenticated_user = {"username": "Ruslan", "is_authenticated": False}

sensitive_operation(authenticated_user)
sensitive_operation(unauthenticated_user)

# H. Write a decorator @argument_decorator that accepts arguments and prints them 
# before and after calling the decorated function.
def argument_decorator(*args):
    def decorator(func):
        def wrapper():
            print(args)
            func()
            print(args)
        return wrapper
    return decorator

@argument_decorator(1, 2, 3)
def example_function():
    print("Python")

example_function()

# I. Create a decorator @modify_arguments that modifies the arguments passed to the 
# decorated function. For example, double all numerical arguments.
def modify_arguments(func):
    def wrapper(*args):
        args = [arg * 2 for arg in args]
        func(*args)
    return wrapper

@modify_arguments
def example_function(a, b, c):
    print(a, b, c, sep=", ")

example_function(2, 3.5, 4)

# J. Write a decorator @modify_return_value that modifies the return value of the 
# decorated function. For example, append a specific string to the return value.
def modify_return_value(modifier):
    def decorator(func):
        def wrapper():
            result = func()
            return result + modifier
        return wrapper
    return decorator

@modify_return_value("modified")
def example_function():
    return "Original return value "

result = example_function()
print(result)

# - File Import Handling -
# A. Create two Python files, main.py and helper.py. In helper.py, define a function. 
# In main.py, import the function from helper.py and use it.
def greeting(name):
    return name

from homework30 import greeting

def main():
    name = input()
    message = greeting(name)
    print(message)

if __name__ == "__main__":
    main()

# B. Write a Python script that imports a function from another file and executes it 
# if the script is run directly. Use if __name__ == "__main__" to control the execution.
def greeting(age):
    return age

from homework30 import greeting

def main():
    name = int(input())
    message = greeting(name)
    print(message)

if __name__ == "__main__":
    main()

# C. Extend task 2 by passing arguments to the function imported from another file. 
# Demonstrate how the imported function can interact with the arguments provided in the main script.
def greeting(name, time_of_day):
    return time_of_day, name

from homework30 import greeting

def main():
    name = input()
    time_of_day = input()
    message = greeting(name, time_of_day)
    print(message)

if __name__ == "__main__":
    main()

# D. Write a Python script that imports all functions from another module using from module import *. 
# Demonstrate the usage of these imported functions.
def function1():
    print("Hello")

def function2():
    print("World")

def function3():
    print("Python")

from homework30 import *

def main():
    function1()
    function2()
    function3()

if __name__ == "__main__":
    main()

# Quiz.
# 1. Which of the following is a valid example of a decorator in Python?
#     a)
#     def my_decorator():
#         print("Decorating function")
#     = b)
#     def my_decorator(func):
#         def wrapper():
#             print("Before function call")
#             func()
#             print("After function call")
#         return wrapper
#     c)
#     def my_decorator(func):
#         print("Before function call")
#         func()
#         print("After function call")
#     d)
#     def my_decorator():
#         def wrapper():
#             print("Before function call")
#             func()
#             print("After function call")
#         return wrapper

# 2. Consider the following decorator and decorated function snippet. 
# What does the decorator @my_decorator do when applied to my_function?
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator: Before function call")
        result = func(*args, **kwargs)
        print("Decorator: After function call")
        return result
    return wrapper

@my_decorator
def my_function(arg1, arg2):
    print(f"Function called with args: {arg1}, {arg2}")

my_function("hello", 42)

#     = a) Prints "Decorator: Before function call", calls the decorated function, 
#     prints "Decorator: After function call".
#     b) Calls the decorated function, prints "Decorator: Before function call", 
#     prints "Decorator: After function call".
#     c) Prints "Decorator: Before function call", calls the decorated function, 
#     prints "Decorator: After function call", and then prints the arguments passed 
#     to the decorated function.
#     d) Calls the decorated function and then prints the arguments passed to the 
#     decorated function.

# 3. In the context of passing arguments to a decorated function, what does the 
# *args parameter in the decorator's wrapper function represent?
#     a) It allows passing multiple positional arguments to the decorated function.
#     b) It allows passing a dictionary of keyword arguments to the decorated function.
#     c) It represents the decorated function itself.
#     d) It represents the arguments passed to the decorator.

# 4. Consider the following Python script. What will be the output if the script is run directly?
def my_function():
    print("My function in main script")

if __name__ == "__main__":
    print("Script running directly")
    my_function()

#     a) My function in main script
#     = b) Script running directly
#     My function in main script
#     c) My function in main script
#     Script running directly
#     d) Script running directly

# 5. In the context of using if __name__ == "__main__", why is this construct useful in Python scripts?
#     = a) It allows the script to define a main function and execute it only when the script is run directly.
#     b) It is a requirement for defining any functions in a Python script.
#     c) It controls the visibility of the script's functions to other modules.
#     d) It allows the script to define multiple entry points for execution.

# 6. Consider the following Python script and another script importing it. 
# What will be the output when the importing script is run?
    # my_module.py:
    #     def my_function():
    #         print("My function in my_module")

    #     if __name__ == "__main__":
    #         print("Script running directly in my_module")
    #         my_function()

    # main_script.py:
    #     import my_module

    #     if __name__ == "__main__":
    #         print("Script running directly in main_script")
    #         my_module.my_function()

#     = a) Script running directly in main_script
#     b) Script running directly in my_module
#     c) My function in main_script
#     d) My function in my_module        
# """