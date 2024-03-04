# """
# - Functions -
# A. Create a function 'greet_user' that takes a name as an argument and 
# prints a greeting message with the provided name. The function should 
# have a default parameter of "User" for the name.
def greet(name="User"):
    print(f"Hello, {name} Welcome!")

greet("Alice")

# B. Create a function calculate_sum that calculates the sum of an 
# arbitrary number of integers passed as arguments. The function should use 
# the *args parameter to accept a variable number of arguments.
def calculate(*args):
    total = 0
    for num in args:
        total += num
    return total

result = calculate(1, 2, 3, 4, 5)
print(result)

# C. Create a function display_info that takes a person's information 
# (name, age, and city) as keyword arguments and prints the information.
def display_info(**kwargs):
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['city'])

display_info(name="Rasim", age=30, city="Sumgait")

# D. Create a function make_sandwich that takes the type of sandwich, and 
# optional toppings and prints the details of the sandwich. The function 
# should have a default parameter for the sandwich type and use keyword 
# arguments for toppings.
def make_sandwich(sandwich_type="turkey", **toppings):
    print(sandwich_type)
    for topping, amount in toppings.items():
        print(amount, topping)

make_sandwich(lettuce=1, tomato=2, cheese=2)

# E. Create a function show_details that takes a person's name as a fixed 
# parameter, followed by an arbitrary number of hobbies using the *args 
# parameter. The function should print the person's name and their hobbies.
def show_details(name, *hobbies):
    print(name)
    for hobby in hobbies:
        print(hobby)

show_details("Rasim", "Reading", "Cooking", "Hiking")

# F. Implement a function sort_numbers that takes a list of numbers as an 
# argument and returns a sorted list in ascending order. Use the * operator 
# to unpack the list.
def sort_numbers(*number_list):
    return sorted(number_list)

numbers = [4, 2, 7, 1, 9, 5]
sorted_numbers = sort_numbers(*numbers)
print(sorted_numbers)

# G. Create a function create_user that takes the user's name, age, and email 
# as keyword arguments and prints a message welcoming the user. Ensure to handle 
# missing or invalid email addresses.
def create_user(name, age, email=None):
        print(name, age, email)
create_user(name="Rasim", age=30)

# H. Create a function generate_invoice that generates an invoice for a customer's 
# purchase. The function should take the customer's name and purchase amount as 
# required arguments, with an optional discount as a keyword argument. Calculate 
# the final amount after applying the discount if provided.
def generate_invoice(customer_name="Rasim", purchase_amount=150, discount=0):
    final_amount = purchase_amount - discount
    print(customer_name)
    print(final_amount)

generate_invoice(discount=20)

# I. Create a function create_circle that creates a circle with specified properties 
# (radius and color). Use keyword arguments to allow specifying these properties and 
# validate the input.
import math

def create_circle(radius, color):    
    return {'radius': radius, 'color': color}

def circle_area(circle):
    return math.pi * circle['radius'] ** 2

circle = create_circle(5, 'blue')
print(circle['radius'], circle['color'], circle_area(circle))

# J. Implement a function calculate_score that takes a student's scores in various 
# subjects as keyword arguments and calculates their total score. Use the ** operator 
# to handle an arbitrary number of subject scores.
def calculate_score(**subject_scores):
    total_score = sum(subject_scores.values())
    return total_score

total_score = calculate_score(math=90, physics=85, chemistry=80)
print(total_score)

# K. Write a function calculate_volume that calculates the volume of a cylinder using 
# its radius and height. Use keyword arguments for the radius and height.
import math

def calculate_volume(radius, height):    
    volume = math.pi * radius ** 2 * height
    return volume

volume = calculate_volume(3, 5)
print(volume)

# L. Create a function print_person_info that takes a person's name as a positional 
# argument and their age and city as keyword arguments. Print the person's name, age, and city.
def print_person_info(name, **kwargs):
        print(name)
        print(kwargs['age'])
        print(kwargs['city'])

print_person_info("Alice", age=30, city="New York")

# M. Implement a function show_order_details that takes the order number as a positional argument, 
# followed by a dictionary of order items as keyword arguments. Print the order number and the 
# items in the order.
def show_order_details(order_number, **order_items):
    print(order_number)
    for item, quantity in order_items.items():
        print(quantity, item)

show_order_details("ORD123", apple=3, banana=2, orange=1)

# N. Write a function that checks whether the given pattern from the user is a substring of
# the 'Cybersecurity in Programming' phrase.
def check_substring(pattern):
    phrase = "Cybersecurity in Programming"
    if pattern in phrase:
        return True
    else:
        return False

user_pattern = input()
if check_substring(user_pattern):
    print("Yes")
else:
    print("No")

# O. Write a function that raises all numbers from the passed list to the power of two.
def square_numbers(numbers):
    squared_numbers = [num**2 for num in numbers]
    return squared_numbers

numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(numbers)
print(squared_numbers)

# - Lambda Functions -
# A. Write a brief explanation of what a lambda function is and when it's useful.
# A lambda function in Python is a small anonymous function defined using the lambda keyword. 
# Lambda functions are useful in situations where you need a small function for a short period of time

# B. Create a lambda function that adds two numbers and test it with example inputs.
add_numbers = lambda x, y: x + y

result = add_numbers(3, 5)
print(result)

result = add_numbers(-1, 10)
print(result)

# C. Create a lambda function that squares a given number and test it with example inputs.
square_number = lambda x: x**2

result = square_number(4)
print(result)

result = square_number(-3)
print(result)

# D. Create a lambda function that takes three parameters (a, b, c) and calculates 'a x b + c'.
calculate_expression = lambda a, b, c: a*b+c

result = calculate_expression(3, 4, 2)
print(result)

# E. Create a lambda function that reverses a given string and test it with example inputs.
reverse_string = lambda s: s[::-1]

result = reverse_string("hello")
print(result)

result = reverse_string("Python")
print(result)

# F. Create a lambda function that capitalizes the first letter of a string and test it with 
# example inputs.
capitalize_first_letter = lambda s: s.capitalize()

result = capitalize_first_letter("hello")
print(result)

result = capitalize_first_letter("python")
print(result)

# G. Create a lambda function that counts the number of vowels (a, e, i, o, u) in a given 
# string and test it with example inputs.
count_vowels = lambda s: sum(1 for char in s if char.lower() in 'aeiou')

result = count_vowels("hello")
print(result)

result = count_vowels("Python Programming")
print(result)

# H. Create a lambda function that counts the number of words in a given string and test it 
# with example inputs.
count_words = lambda s: len(s.split())

result = count_words("Hello, how are you?")
print(result)

result = count_words("Python is a powerful programming language.")
print(result)

# Quiz.
# 1. What is a lambda function in Python?
#     a) A named function defined using the lambda keyword.
#     = b) An anonymous function defined using the def keyword.
#     c) A function that can take multiple arguments.
#     d) A function that returns multiple values.

# 2. Which of the following is a benefit of using a lambda function?
#     a) It allows for complex logic and multiple statements.
#     b) It can be assigned a name for reusability.
#     = c) It is ideal for simple, one-line operations.
#     d) It can accept an arbitrary number of arguments.

# 3. In Python, which type of argument requires the caller to provide a value when calling a function?
#     a) Default argument
#     b) Keyword argument
#     = c) Positional argument
#     d) Lambda argument

# 4. What will the following code output?
def multiply(a, b=2):
    return a * b

result = multiply(3)
print(result)

#     = a) 6
#     b) 9
#     c) 3
#     d) Error

# 5. Which of the following is a valid usage of a lambda function?
#     = a) Sorting a list of integers
#     b) Creating a dictionary
#     c) Defining a class
#     d) Iterating over a list
    
# 6. In Python, what will the len() function return for the string "hello"?
#     = a) 5
#     b) 6
#     c) 4
#     d) 7

# 7. What is the purpose of a function in Python?
#     a) To store variables.
#     = b) To perform a specific task or set of tasks.
#     c) To declare classes.
#     d) To handle exceptions.

# 8. Which of the following is true about functions in Python?
#     a) A function can only be defined using the def keyword.
#     = b) A function can return multiple values.
#     c) A function cannot call other functions.
#     d) A function can only accept a single argument.

# 9. What is the output of the following code?
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)

#     = a) "Hello, Alice!"
#     b) "Hello, name!"
#     c) Error
#     d) "Hello, world!"

# 10. Which of the following statements about keyword arguments is true?
#     a) Keyword arguments must always come before positional arguments.
#     b) Keyword arguments are specified using the key keyword.
#     = c) Keyword arguments provide a default value if not provided by the caller.
#     d) Keyword arguments are mandatory.

# 11. What is the purpose of the *args parameter in a function definition?
#     a) To specify keyword arguments.
#     b) To specify default values for arguments.
#     = c) To allow the function to accept an arbitrary number of positional arguments.
#     d) To allow the function to accept an arbitrary number of keyword arguments.

# 12. In a lambda function, what does 'x' represent?
#     a) The function itself.
#     = b) The argument being passed to the function.
#     c) The return value of the function.
#     d) The number of arguments the function can accept.

# 13. What will the following code output?
text = "hello lambda"
reverse_text = (lambda x: x[::-1])(text)
print(reverse_text)

#     = a) "adamal olleh"
#     b) "ambda"
#     c) "ah"
#     d) Error

# 14. What is a default parameter in a function?
#     = a) A parameter that is automatically assigned a value if no value is provided by the caller.
#     b) A parameter that must always be specified by the caller.
#     c) A parameter that has a fixed value and cannot be changed.
#     d) A parameter that is only used for keyword arguments.

# 15. In which situation would using default parameters be most beneficial?
#     a) When you want to ensure a parameter is always provided by the caller.
#     = b) When you want to assign a specific value to a parameter unless the caller provides a different value.
#     c) When you want to use a different function depending on the provided parameters.
#     d) When you want to force the caller to use only keyword arguments.
    
# 16. What is the main difference between positional and keyword arguments in Python?
#     = a) Positional arguments are provided by specifying the argument value only, 
#     while keyword arguments are specified with the parameter name and value.
#     b) Positional arguments are mandatory, while keyword arguments are optional.
#     c) Positional arguments can be specified using the args keyword, while keyword 
#     arguments use the kwargs keyword.
#     d) Positional arguments can only be used for functions with a single parameter.
    
# 17. When should you use positional arguments over keyword arguments?
#     = a) When you want to provide arguments in a specific order.
#     b) When you want to ensure that the caller always provides a value for that argument.
#     c) When you want to allow the caller to provide arguments in any order.
#     d) When you want to provide a default value for an argument.
# """