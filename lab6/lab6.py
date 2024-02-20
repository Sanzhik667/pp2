#1
import math

def multiply_numbers(numbers):
    # Use math.prod() to multiply all numbers in the list
    result = math.prod(numbers)
    return result

# Example usage
numbers = [1, 2, 3, 4, 5]
result = multiply_numbers(numbers)
print("List:", numbers)
print("Result of multiplying all numbers:", result)
#2
def count_upper_lower(string):
    # Initialize counters for uppercase and lowercase letters
    upper_count = 0
    lower_count = 0
    
    # Iterate through each character in the string
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count

# Example usage
string = "Hello World! This is a Test String."
upper_count, lower_count = count_upper_lower(string)
print("String:", string)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
#3
def is_palindrome(string):
    # Reverse the string using slicing
    reversed_string = string[::-1]
    # Check if the original string is equal to its reverse
    return string == reversed_string

# Example usage
string = "radar"
result = is_palindrome(string)
if result:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")
#4
import time
import math

def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    return result

# Sample Input
number = 25100
milliseconds = 2123

# Calculate square root after delay
result = delayed_square_root(number, milliseconds)

# Sample Output
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
#5
def all_true(elements):
    return all(elements)

# Example usage
tuple1 = (True, True, False, True)
tuple2 = (True, True, True)

print("All elements in tuple1 are true:", all_true(tuple1))
print("All elements in tuple2 are true:", all_true(tuple2))
