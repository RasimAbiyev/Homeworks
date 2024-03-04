# """
# - Map -
# A. Create a function that takes a list of numbers and uses the map() function to 
# double each number in the list.
def double_numbers(numbers):
    doubled_numbers = list(map(lambda x: x*2, numbers))
    return doubled_numbers

numbers = [1, 2, 3, 4, 5]
doubled_numbers = double_numbers(numbers)
print(doubled_numbers)

# B. Write a function that takes a list of temperatures in Celsius and uses map() 
# to convert them to Fahrenheit using the appropriate conversion formula.
def celsius_to_fahrenheit(temperatures_celsius):
    temperatures_fahrenheit = list(map(lambda c: c*9/5+32, temperatures_celsius))
    return temperatures_fahrenheit

temperatures_celsius = [0, 10, 20, 30, 40]
temperatures_fahrenheit = celsius_to_fahrenheit(temperatures_celsius)
print(temperatures_fahrenheit)

# C. Implement a function that takes a list of numbers and uses the map() function to 
# calculate the square root of each number.
import math 

def calculate_square_roots(numbers):
    square_roots = list(map(math.sqrt, numbers))
    return square_roots

numbers = [4, 9, 16, 25]
square_roots = calculate_square_roots(numbers)
print(square_roots)

# D. Write a function that takes a list of names and uses map() to format them as "Hello, {name}!".
def greet(names):
    greeting = list(map(lambda name: f"Hello, {name}!", names))
    return greeting

names = ["Elxan", "Ruslan", "Nazim"]
greeting = greet(names)
print(greeting)

# E. Create a function that takes a list of numbers and uses the map() function to generate a 
# power series for each number, up to a specified exponent.
def generate_power_series(numbers, exponent):
    power_series = list(map(lambda num: [num**exp for exp in range(exponent+1)], numbers))
    return power_series

numbers = [2, 3, 4]
exponent = 3
power_series = generate_power_series(numbers, exponent)
print(power_series)

# F. Write a function that takes two lists of strings and uses map() to concatenate the elements 
# of the same index from both lists.
def concatenate_lists(list1, list2):
    concatenated_list = list(map(lambda x, y: x+y, list, list2))
    return concatenated_list

list1 = ["Hello", "Goodbye", "Welcome"]
list2 = ["World", "!", "to the Sumgait"]
result = concatenate_lists(list1, list2)
print(result)

# G. Create a function that takes a list of floats and uses the map() function to round each float 
# to a specified number of decimal places.
def round_floats(numbers, decimal_places):
    rounded_numbers = list(map(lambda x: round(x, decimal_places), numbers))
    return rounded_numbers

numbers = [3.14159, 2.71828, 1.61803]
decimal_places = 2
rounded_numbers = round_floats(numbers, decimal_places)
print(rounded_numbers)

# H. Write a function that takes a list of prices and uses map() to apply a discount percentage to each price.
def apply_discount(prices, discount_percentage):
    discounted_prices = list(map(lambda price: price*(1-discount_percentage/100), prices))
    return discounted_prices

prices = [100, 200, 300]
discount_percentage =10
discounted_prices = apply_discount(prices, discount_percentage)
print(discounted_prices)

# I. Implement a function that takes a list of sentences and uses map() to encrypt each sentence using 
# a simple encryption algorithm.
def encrypt_sentences(sentences, shift):
    encrypted_sentences = list(map(lambda sentence: encrypt_sentence(sentence, shift), sentences))
    return encrypted_sentences

def encrypt_sentence(sentence, shift):
    encrypted_sentence = ''
    for char in sentence:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            if char.isupper():
                shifted_char = shifted_char.upper()
            encrypted_sentence += shifted_char
        else:
            encrypted_sentence += char
    return encrypted_sentence

sentences = ["Hello, world!"]
shift = 3
encrypted_sentences = encrypt_sentences(sentences, shift)
print(encrypted_sentences)

# J. Create a function that takes a list of words and uses map() to count the number of vowels in each word.
def count_vowels(words):
    vowel_counts = list(map(lambda word: count_vowels_in_word(word), words))
    return vowel_counts

def count_vowels_in_word(word):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in word if char in vowels)
    return vowel_count

words = ["hello", "world", "apple", "banana"]
vowel_counts = count_vowels(words)
print(vowel_counts)

# K. Write a function that takes a list of strings and uses map() to return a list of lengths for each string.
def length(string):
    string_length = list(map(len, string))
    return string_length

string = ["hello", "world", "python"]
lengths = length(string)
print(lengths)

# - Filter -
# A. Create a function that takes a list of numbers and uses the filter() function to 
# return a new list containing only the even numbers.
def even_numbers(numbers):
    even_number = list(filter(lambda x: x % 2 == 0, numbers))
    return even_number

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number = even_numbers(numbers)
print(even_number)

# B. Write a function that takes a list of numbers and uses the filter() function to 
# return a new list containing only the prime numbers.
def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    return True

def prime_numbers(numbers):
    prime_numbers = list(filter(prime, numbers))
    return prime_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_number = prime_numbers(numbers)
print(prime_number)

# C. Implement a function that filters a list of strings to return a new tuple containing 
# only the words that are palindromes.
def palindrome(word):
    return word == word[::-1]

def palindromes(words):
    palindrome_words = tuple(filter(palindrome, words))
    return palindrome_words

words = ["radar", "level", "python", "noon", "racecar"]
palindrome_words = palindromes(words)
print(palindrome_words)

# D. Given a list of dictionaries representing employees and their salaries, use filter() 
# to create a new list of employees whose salary is above a specified threshold.
def high_salary_employees(employees, salary):
    high_salary = list(filter(lambda emp: emp["salary"] > salary, employees))
    return high_salary

employees = [
    {"name": "Rasim", "salary": 50000},
    {"name": "Ruslan", "salary": 60000},
    {"name": "Ramin", "salary": 45000},
    {"name": "Orxan", "salary": 70000}
]
salary = 55000
high_salary = high_salary_employees(employees, salary)
print(high_salary)

# E. Write a function that takes a list of file names and filters it to return a new list 
# containing only files with a specified file extension.
def files_extension(file_names, extension):
    filtered_files = list(filter(lambda file_name: file_name.endswith(extension), file_names))
    return filtered_files

file_names = ["document.text", "document2.docx", "image1.jpg", "script.py", "data.csv"]
extension = ".txt"
filtered_files = files_extension(file_names, extension)
print(filtered_files)

# F. Create a function that takes a dictionary of student names and their corresponding grades, 
# and uses filter() to return a new dictionary containing only students who passed (grades above 
# a certain threshold).
def passing_students(students_grades, passing):
    passing_student = dict(filter(lambda item: item[1] >= passing, students_grades.items()))
    return passing_student

students_grades = {
    "Rasim": 85,
    "Ruslan": 70,
    "Ramin": 60,
    "Samir": 90
}
passing = 75
passing_student = passing_students(students_grades, passing)
print(passing_student)

# G. Implement a function that takes a mixed list of data types (integers, strings, floats) and 
# filters it to return separate lists for each data type.
def data_types(data):
    int_list = []
    float_list = []
    str_list = []
    
    for item in data:
        if isinstance(item, int):
            int_list.append(item)
        elif isinstance(item, float):
            float_list.append(item)
        elif isinstance(item, str):
            str_list.append(item)
    
    return int_list, float_list, str_list

mixed_data = [1, 2.5, 'hello', 3, 'world', 4.5, 5]
integers, floats, strings = data_types(mixed_data)
print(integers)
print(floats)
print(strings)

# H. Prompt the user to enter a condition, then use the filter() function to filter a given list 
# of numbers based on the user-provided condition.
def numbers_based_on_condition(numbers, condition):
    filtered_numbers = list(filter(condition, numbers))
    return filtered_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

condition_input = input("Enter a condition (e.g., lambda x: x % 2 == 0 for even numbers): ")

condition = eval(condition_input)
filtered_numbers = numbers_based_on_condition(numbers, condition)
print(filtered_numbers)
# I. Write a function that takes a list of strings and filters it to return a new list containing 
# only strings that contain a specific substring.
def strings_containing_substring(strings, substring):
    filtered_strings = list(filter(lambda string: substring in string, strings))
    return filtered_strings

strings = ["apple", "banana", "grape", "orange", "pineapple"]
substring = "apple"
filtered_strings = strings_containing_substring(strings, substring)
print(filtered_strings)

# J. Implement a function that takes a list of strings and filters it to return a new list containing 
# strings with a specified character appearing a certain number of times.
def strings_by_character(strings, char, count):
    filtered_strings = list(filter(lambda string: string.count(char) == count, strings))
    return filtered_strings

strings = ["hello", "world", "python", "apple", "banana"]
char = "o"
count = 1
filtered_strings = strings_by_character(strings, char, count)
print(filtered_strings)

# K. Create a function that takes a list of integers and uses the filter() function to return a 
# new list containing only those numbers for which a specified mathematical function (e.g., square, 
# cube) yields a prime result.
def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    return True

def numbers_prime(numbers):
    return list(filter(prime, numbers))

def square(x):
    return x**2

def cube(x):
    return x**3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
prime_numbers = numbers_prime(numbers)

prime_squares = [square(num) for num in prime_numbers]
prime_cubes = [cube(num) for num in prime_numbers]

print(prime_squares)
print(prime_cubes)

# L. Write a function that takes a list of date objects and filters it to return a new list containing 
# dates within a specified range.
from datetime import datetime

def dates_range(dates, start_date, end_date):
    filtered_dates = list(filter(lambda date: start_date <= date <= end_date, dates))
    return filtered_dates

dates = [
    datetime(2022, 1, 1),
    datetime(2022, 3, 15),
    datetime(2022, 5, 20),
    datetime(2022, 7, 10),
    datetime(2022, 9, 5)
]
start_date = datetime(2022, 3, 1)
end_date = datetime(2022, 8, 31)

filtered_dates = dates_range(dates, start_date, end_date)
print(filtered_dates)

# M. Given a list of cities and their corresponding countries, use filter() to return a new list 
# containing cities from a specific country.
def cities_country(cities_countries, country):
    filtered_cities = list(filter(lambda city_country: city_country[1] == country, cities_countries))
    return filtered_cities

cities_countries = [
    ("New York", "USA"),
    ("London", "UK"),
    ("Paris", "France"),
    ("Tokyo", "Japan"),
    ("Sydney", "Australia")
]
country = "USA"

filtered_cities = cities_country(cities_countries, country)
print(filtered_cities)

# N. Create a function that takes a list of product objects and uses the filter() function to return a 
# new list containing only available products.
def available_products(products):
    available_product = list(filter(lambda product: product['available'], products))
    return available_product

# Example usage:
products = [
    {'name': 'Apple', 'price': 1.99, 'available': True},
    {'name': 'Banana', 'price': 0.99, 'available': False},
    {'name': 'Orange', 'price': 2.49, 'available': True},
    {'name': 'Grapes', 'price': 3.99, 'available': True},
    {'name': 'Mango', 'price': 4.49, 'available': False}
]

available_product = available_products(products)
for product in available_product:
    print(product['name'])

# O. Implement a function that takes a list and uses filter() to return a new list containing only 
# the unique elements.
def unique_elements(lst):
    unique_element = list(filter(lambda x: lst.count(x) == 1, lst))
    return unique_element

original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_element = unique_elements(original_list)
print(unique_element)

# P. Write a function that takes a list of words and filters it to return a new list containing only 
# anagrams of a specified word.
def anagram(word1, word2):
    return sorted(word1) == sorted(word2)

def filter_anagrams(words, target_word):
    return list(filter(lambda word: anagram(word, target_word), words))

word_list = ["listen", "silent", "enlist", "banana", "tan", "ant"]
target_word = "silent"

anagrams = filter_anagrams(word_list, target_word)
print(anagrams)

# Q. Given a list of numeric data, use filter() to return a new list containing elements within a 
# specified range.
def elements(data, min_value, max_value):
    return list(filter(lambda x: min_value <= x <= max_value, data))

datas = [1, 5, 10, 15, 20, 25, 30]
min_value = 10
max_value = 20

filtered_data = elements(datas, min_value, max_value)
print(filtered_data)


# R. Create a function that takes a list of strings and uses filter() to return a new list containing 
# only strings that match a specific regular expression.
import re

def strings(strings, pattern):
    return list(filter(lambda string: re.match(pattern, string), strings))

string_list = ["apple", "banan", "cherry", "dog", "elephant"]
regex_pattern = r'^[a-zA-Z]{5}$'

filtered_strings = strings(string_list, regex_pattern)
print(filtered_strings)

# - Reversed -
# A. Write a function that takes a list of elements and uses the reversed() function to reverse the 
# order of elements in the list.
def reverse_list(elements):
    return list(reversed(elements))

original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(reversed_list)

# B. Create a function that takes a string and uses reversed() to reverse the characters in the string.
def reverse_string(input_string):
    return "".join(reversed(input_string))

original_string = "hello world"
reversed_string = reverse_string(original_string)
print(reversed_string)

# C. Implement a function that takes a tuple and uses reversed() to reverse the order of elements in the tuple.
def reverse_tuple(input_tuple):
    return tuple(reversed(input_tuple))

original_tuple = (1, 2, 3, 4, 5)
reversed_tuple = reverse_tuple(original_tuple)
print(reversed_tuple)

# D. Write a function that takes a sentence and uses reversed() to reverse the order of words in the sentence.
def reverse_sentence(input_sentence):
    words = input_sentence.split()
    reversed_words = " ".join(reversed(words))
    return reversed_words

original_sentence = "Hello world how are you"
reversed_sentence = reverse_sentence(original_sentence)
print(reversed_sentence)

# E. Create a function that takes a dictionary and uses reversed() to reverse the order of keys and values.
def reverse_dictionary(input_dict):
    reversed_dict = {value: key for key, value in input_dict.items()}
    return reversed_dict

original_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = reverse_dictionary(original_dict)
print(reversed_dict)

# F. Implement a function that takes a linked list and uses reversed() to reverse the order of nodes in the linked list.
def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        value, next_node = current
        current[1] = prev
        prev = current
        current = next_node
    
    return prev

head = [1, [2, [3, [4, [5, None]]]]]

reversed_head = reverse_linked_list(head)

current = reversed_head
while current:
    print(current[0], end=" ")
    current = current[1]

# G. Write a function that takes a queue and uses reversed() to reverse the order of elements in the queue.
def reverse_queue(queue):
    temp_list = []
    while queue:
        temp_list.append(queue.pop(0))
    temp_list.reverse()
    for element in temp_list:
        queue.append(element)

original_queue = [1, 2, 3, 4, 5]
reverse_queue(original_queue)
print(original_queue)

# H. Create a function that takes a stack and uses reversed() to reverse the order of elements in the stack.
def reverse_stack(stack):
    temp_list = list(reversed(stack))
    stack.clear()
    for item in temp_list:
        stack.append(item)

stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)

# I. Implement a function that takes a list of elements and uses reversed() to reverse the elements at odd 
# indices, while keeping the elements at even indices unchanged.
def reverse_elements(lst):
    for i in range(1, 5, 2):
        lst[i] = lst[i][::-1]

elements = ['a', 'bc', 'def', 'ghi', 'jklm']
reverse_elements(elements)
print(elements)

# J. Write a function that takes a binary number as a string and uses reversed() to reverse the binary digits.
def reverse_binary(binary_string):
    reversed_binary = ''.join(reversed(binary_string))
    return reversed_binary

binary_number = "110101"
reversed_binary = reverse_binary(binary_number)
print(reversed_binary)

# K. Create a function that takes a 2D matrix and uses reversed() to reverse the rows of the matrix.
def reverse_rows(matrix):
    reversed_matrix = [list(reversed(row)) for row in matrix]
    return reversed_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
reversed_matrix = reverse_rows(matrix)
for row in reversed_matrix:
    print(row)

# L. Implement a function that takes a string and uses reversed() to reverse the characters in each substring 
# separated by a specific delimiter.
def reverse_substrings(string, delimiter):
    substrings = string.split(delimiter)
    reversed_substrings = ["".join(reversed(sub)) for sub in substrings]
    return delimiter.join(reversed_substrings)

string = "hello.world.how.are.you"
delimiter = "."
reversed_string = reverse_substrings(string, delimiter)
print(reversed_string)

# - Sorted -
# A. Write a function that takes a list of numbers and uses the sorted() function to return a new list with 
# the numbers sorted in ascending order.
def sort_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers

numbers = [4, 2, 7, 1, 9, 5]
sorted_numbers = sort_numbers(numbers)
print(sorted_numbers)

# B. Create a function that takes a list of numbers and uses the sorted() function to return a new list with 
# the numbers sorted in descending order.
def sort_numbers(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers

numbers = [4, 2, 7, 1, 9, 5]
sorted_numbers = sort_numbers(numbers)
print(sorted_numbers)

# C. Implement a function that takes a list of strings and uses the sorted() function to return a new list 
# with the strings sorted by their lengths.
def sort_strings(strings):
    sorted_strings = sorted(strings, key=len)
    return sorted_strings

strings = ["apple", "banana", "cherry", "date", "fig"]
sorted_strings = sort_strings(strings)
print(sorted_strings)

# D. Write a function that takes a list of tuples and uses the sorted() function to return a new list with 
# the tuples sorted based on their second element.
def sort_tuples(tuples_list):
    sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
    return sorted_tuples

tuples_list = [(1, 3), (2, 1), (3, 2), (4, 5), (5, 4)]
sorted_tuples= sort_tuples(tuples_list)
print(sorted_tuples)

# E. Create a function that takes a dictionary and uses the sorted() function to return a new dictionary 
# with its items sorted by their values.
def sort_dictionary(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda x: x[1])
    sorted_dictionary = dict(sorted_items)
    return sorted_dictionary

dictionary = {'a': 3, 'b': 1, 'c': 2, 'd': 5, 'e': 4}
sorted_dictionary = sort_dictionary(dictionary)
print(sorted_dictionary)

# F. Implement a function that takes a list of strings and uses the sorted() function to return a new list 
# with the strings sorted in a case-insensitive manner.
def sort_strings(strings):
    sorted_strings = sorted(strings, key=str.lower)
    return sorted_strings

strings = ["Apple", "banana", "cherry", "Date", "fig"]
sorted_strings = sort_strings(strings)
print(sorted_strings)

# G. Write a function that takes a list of custom objects and uses the sorted() function to return a new list 
# with the objects sorted based on a specified attribute.
def sort_objects(objects, attribute):
    sorted_objects = sorted(objects, key=lambda x: x[attribute])
    return sorted_objects

objects = [
    {"name": "Rasim", "age": 30},
    {"name": "Ramin", "age": 25},
    {"name": "Kamal", "age": 35}
]

sorted_objects = sort_objects(objects, 'age')
for obj in sorted_objects:
    print(obj['name'], obj['age'])

# H. Create a function that takes a list of date objects and uses the sorted() function to return a new list 
# with the dates sorted in chronological order.
from datetime import date

def sort_dates(dates):
    sorted_dates = sorted(dates)
    return sorted_dates


dates = [
    date(2023, 5, 15),
    date(2022, 10, 8),
    date(2024, 3, 20),
    date(2023, 1, 1)
]

sorted_dates = sort_dates(dates)
print(sorted_dates)

# I. Implement a function that takes a list of lists and uses the sorted() function to return a new list with 
# the lists sorted based on the sum of their elements.
def sort_lists(lists):
    sorted_lists = sorted(lists, key=sum)
    return sorted_lists

lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
sorted_lists = sort_lists(lists)
print(sorted_lists)

# J. Write a function that takes a list of integers and uses the sorted() function to return a new list with 
# the integers sorted based on the number of factors they have.
def count_factors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

def sort_integers(integers):
    sorted_integers = sorted(integers, key=count_factors)
    return sorted_integers

integers = [6, 12, 8, 9, 15, 25, 16]
sorted_integers = sort_integers(integers)
print(sorted_integers)

# K. Create a function that takes a list of strings and uses the sorted() function to return a new list with 
# the strings sorted based on their last characters.
def sort_strings(strings):
    sorted_strings = sorted(strings, key=lambda x: x[-1])
    return sorted_strings

strings = ["apple", "banana", "cherry", "date", "fig"]
sorted_strings = sort_strings(strings)
print(sorted_strings)

# L. Implement a function that takes a list of dictionaries and uses the sorted() function to return a new list 
# with the dictionaries sorted based on their keys.
def sort_dictionaries(dictionaries):
    sorted_dictionaries = sorted(dictionaries, key=lambda x: sorted(x.keys()))
    return sorted_dictionaries

dictionaries = [
    {'b': 2, 'a': 1, 'c': 3},
    {'z': 26, 'y': 25, 'x': 24},
    {'foo': 'bar', 'baz': 'qux', 'spam': 'eggs'}
]

sorted_dictionaries = sort_dictionaries(dictionaries)
for dictionary in sorted_dictionaries:
    print(dictionary)

# M. Sort the following list of strings alphabetically by the second letter:
string_list = ["Hello", "World", "Python", "Programming", "Example", "String", "List", "ChatGPT"]

sorted_string = sorted(string_list, key=lambda x: x[1])

print(sorted_string)

# Quiz.
# 1. What is the purpose of the filter() function in Python?
#     = A) To remove elements from an iterable based on a given condition
#     B) To sort elements in an iterable
#     C) To modify elements in an iterable
#     D) To combine elements in an iterable

# 2. Which of the following data types can the filter() function be applied to?
#     A) Lists
#     B) Strings
#     C) Tuples
#     = D) All of the above

# 3. What does the filter() function return?
#     = A) A new iterable containing filtered elements
#     B) The original iterable with filtered elements
#     C) A list of filtered elements
#     D) A tuple of filtered elements

# 4. Which parameter does the filter() function take?
#     A) A filter function
#     B) An iterable
#     = C) Both A and B
#     D) Neither A nor B

# 5. In the context of the filter() function, what does the filter function do?
#     = A) Defines the condition for filtering elements
#     B) Specifies the data type of the iterable
#     C) Sorts the iterable elements
#     D) Combines the iterable elements

# 6. Which of the following statements is true about the filter() function?
#     A) The filter function can only return True or False
#     B) The filter function can return any data type
#     = C) The filter function must return a boolean
#     D) The filter function is not required

# 7. What is the syntax for using the filter() function in Python?
#     A) filter(condition, iterable)
#     B) filter(iterable, condition)
#     = C) filter(function, iterable)
#     D) filter(iterable, function)

# 8. When using the filter() function, what happens if the filter function returns False for an element?
#     = A) The element is removed from the iterable
#     B) The element is included in the iterable
#     C) An error is raised
#     D) None of the above

# 9. Can the filter() function be used to filter elements based on multiple conditions?
#     = A) Yes
#     B) No

# 10. In Python 3, what does the filter() function return by default?
#     = A) A filter object
#     B) A list of filtered elements
#     C) A tuple of filtered elements
#     D) A set of filtered elements

# 11. What is the purpose of the map() function in Python?
#     = A) To apply a given function to each item in an iterable
#     B) To filter elements from an iterable based on a given condition
#     C) To sort elements in an iterable
#     D) To combine elements in an iterable

# 12. Which of the following is an iterable that can be passed to the map() function?
#     A) Lists
#     B) Strings
#     C) Tuples
#     = D) All of the above

# 13. What does the map() function return?
#     = A) A new iterable containing transformed elements
#     B) The original iterable with transformed elements
#     C) A list of transformed elements
#     D) A tuple of transformed elements

# 14. What parameters does the map() function take?
#     A) A mapping function and an iterable
#     B) A single iterable
#     C) A single mapping function
#     = D) A mapping function, followed by one or more iterables

# 15. In the context of the map() function, what does the mapping function do?
#     = A) Defines the transformation to be applied to each element
#     B) Specifies the data type of the iterable
#     C) Sorts the iterable elements
#     D) Combines the iterable elements

# 16. Which of the following is true about the map() function?
#     = A) The mapping function can return any data type
#     B) The mapping function must return a boolean
#     C) The mapping function is not required
#     D) The mapping function must return an integer

# 17. What is the syntax for using the map() function in Python?
#     A) map(mapping_function, iterable)
#     B) map(iterable, mapping_function)
#     = C) map(function, iterable)
#     D) map(iterable, function)    

# 18. When using the map() function, what happens if the mapping function returns None for an element?
#     A) The element is removed from the iterable
#     = B) The element remains unchanged in the iterable
#     C) An error is raised
#     D) None of the above

# 19. Can the map() function be used to transform elements from multiple iterables?
#     = A) Yes
#     B) No

# 20. In Python 3, what does the map() function return by default?
#     = A) A map object
#     B) A list of transformed elements
#     C) A tuple of transformed elements
#     D) A set of transformed elements

# 21. What is the purpose of the reversed() function in Python?
#     = A) To reverse the order of elements in an iterable
#     B) To sort elements in an iterable
#     C) To remove elements from an iterable
#     D) To concatenate elements in an iterable

# 22. Which of the following is an iterable that can be passed to the reversed() function?
#     A) Lists
#     B) Strings
#     C) Tuples
#     = D) All of the above

# 23. What does the reversed() function return?
#     = A) A new iterable containing reversed elements
#     B) The original iterable with reversed elements
#     C) A list of reversed elements
#     D) A tuple of reversed elements

# 24. What parameter does the reversed() function take?
#     = A) An iterable
#     B) A single element
#     C) A number
#     D) A mapping function

# 25. In the context of the reversed() function, what does "reversed elements" mean?
#     = A) The elements are in the opposite order
#     B) The elements are sorted in ascending order
#     C) The elements are concatenated
#     D) The elements are multiplied

# 26. Which of the following is true about the reversed() function?
#     A) The reversed elements are returned as a list
#     B) The reversed elements are returned as a tuple
#     = C) The reversed elements are returned as an iterator
#     D) The reversed elements are returned as a set

# 27. What is the syntax for using the reversed() function in Python?
#     = A) reversed(iterable)
#     B) iterable.reversed()
#     C) reversed(function, iterable)
#     D) reversed(iterable, function)

# 28. When using the reversed() function, can it be applied to strings?
#     = A) Yes
#     B) No

# 29. Can the reversed() function be used to reverse a dictionary?
#     A) Yes
#     = B) No

# 30. In Python 3, what does the reversed() function return by default?
#     = A) A reversed object
#     B) A list of reversed elements
#     C) A tuple of reversed elements
#     D) A set of reversed elements

# 31. What is the purpose of the sorted() function in Python?
#     = A) To sort elements in an iterable and return a sorted list
#     B) To reverse the order of elements in an iterable
#     C) To remove elements from an iterable
#     D) To concatenate elements in an iterable

# 32. Which of the following is an iterable that can be passed to the sorted() function?
#     A) Lists
#     B) Strings
#     C) Tuples
#     = D) All of the above
    
# 33. What does the sorted() function return?
#     A) A new iterable containing sorted elements
#     B) The original iterable with sorted elements
#     = C) A list of sorted elements
#     D) A tuple of sorted elements

# 34. What parameters does the sorted() function take?
#     = A) An iterable
#     B) A single element
#     C) A mapping function
#     D) A mapping function and an iterable

# 35. In the context of the sorted() function, what does "sorted elements" mean?
#     = A) The elements are arranged in ascending order
#     B) The elements are arranged in descending order
#     C) The elements are multiplied
#     D) The elements are concatenated

# 36. Which of the following is true about the sorted() function?
#     A) The sorted elements are returned as a tuple
#     B) The sorted elements are returned as a set
#     C) The sorted elements are returned as an iterator
#     = D) The sorted elements are returned as a list

# 37. What is the syntax for using the sorted() function in Python?
#     = A) sorted(iterable)
#     B) iterable.sorted()
#     C) sorted(function, iterable)
#     D) sorted(iterable, function)

# 38. When using the sorted() function, can you specify a custom sorting order?
#     = A) Yes, by providing a custom sorting function
#     B) No, the sorting order is always ascending
#     C) Yes, by providing a reverse parameter
#     D) No, the sorting order is always descending

# 39. Can the sorted() function be used to sort a dictionary based on its keys or values?
#     = A) Yes
#     B) No

# 40. In Python 3, what does the sorted() function return by default?
#     = A) A list of sorted elements
#     B) A sorted object
#     C) A tuple of sorted elements
#     D) A set of sorted elements
# """