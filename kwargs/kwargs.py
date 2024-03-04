# """
# - Kwargs -
# A. Create a function that accepts **kwargs and prints out all the key-value pairs passed as arguments.
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

print_kwargs(name="Rasim", age=30, city="Sumgait")

# B. Write a function that accepts **kwargs containing numeric values and returns the sum of all the values.
def sum(**kwargs):
    total_sum = 0
    for value in kwargs.values():
            total_sum += value
    return total_sum

result = sum(num1=10, num2=20, num3=30.5, num5=40)
print(result)

# C. Create a function that filters a dictionary based on the keys provided as **kwargs.
def filter(dictionary, **kwargs):
    filtered_dict = {}
    for key in kwargs:
        if key in dictionary:
            filtered_dict[key] = dictionary[key]
    return filtered_dict

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_result = filter(my_dict, a=1, c=3, e=5)
print(filtered_result)

# D. Write a function that validates input parameters using **kwargs. For example, ensure that a function 
# only accepts specific keyword arguments and raises an error if any invalid argument is passed.
def function(**kwargs):
    valid_arguments = ['arg1', 'arg2', 'arg3']
    invalid_args = [arg for arg in kwargs if arg not in valid_arguments]
    if invalid_args:
        raise ValueError
    print(kwargs)

function(arg1=10, arg2=20, arg4=30)

# """