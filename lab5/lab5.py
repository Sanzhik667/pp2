"""#1
import re

# Шаблон регулярного выражения
pattern = r'ab*'

# Строки для проверки
strings = ["ac", "abc", "abbc", "a", "abb"]

# Проверка каждой строки
for string in strings:
    if re.match(pattern, string):
        print(f"Строка '{string}' соответствует шаблону.")
    else:
        print(f"Строка '{string}' НЕ соответствует шаблону.")
#2
import re

# Шаблон регулярного выражения
pattern = r'ab{2,3}'

# Строки для проверки
strings = ["ab", "abb", "abbb", "a", "abc", "abbbb"]

# Проверка каждой строки
for string in strings:
    if re.search(pattern, string):
        print(f"Строка '{string}' соответствует шаблону.")
    else:
        print(f"Строка '{string}' НЕ соответствует шаблону.")
#3
import re

# Sample text
text = "hello_world foo_bar test_sequence not_a_match"

# Regular expression pattern
pattern = r'[a-z]+_[a-z]+'

# Find all matches
matches = re.findall(pattern, text)

# Print the matches
print("Sequences of lowercase letters joined with an underscore:")
for match in matches:
    print(match)
#4
    import re

# Sample text
text = "Hello World python Is Cool"

# Regular expression pattern
pattern = r'[A-Z][a-z]+'

# Find all matches
matches = re.findall(pattern, text)

# Print the matches
print("Sequences of one uppercase letter followed by lowercase letters:")
for match in matches:
    print(match)"""
"""#5
import re

# Sample text
text = "axb acb abbb abb a_bc a_b ab"

# Regular expression pattern
pattern = r'a.*c$'

# Find all matches
matches = re.findall(pattern, text)

# Print the matches
print("Strings that have an 'a' followed by anything, ending in 'b':")
for match in matches:
    print(match)
#6
import re

# Sample text
text = "Hello, world. This is a sample text."

# Regular expression pattern to match space, comma, or dot
pattern = r'[ ,.]'

# Replace all occurrences of space, comma, or dot with a colon
new_text = re.sub(pattern, ':', text)

# Print the modified text
print("Original text:", text)
print("Modified text:", new_text)"""
"""#7
def snake_to_camel(snake_case_str):
    # Split the snake case string into words
    words = snake_case_str.split('_')
    
    # Capitalize the first letter of each word except the first one
    camel_case_words = [words[0]] + [word.capitalize() for word in words[1:]]
    
    # Join the words together to form the camel case string
    camel_case_str = ''.join(camel_case_words)
    
    return camel_case_str

# Example usage
snake_case_str = "hello_world_in_python"
camel_case_str = snake_to_camel(snake_case_str)
print("Snake case:", snake_case_str)
print("Camel case:", camel_case_str)
#8
import re

def split_at_uppercase(string):
    # Use regular expression to split at uppercase letters
    parts = re.findall('[A-Z][^A-Z]*', string)
    return parts

# Example usage
string = "SplitThisStringAtUpperCaseLetters"
result = split_at_uppercase(string)
print("Original string:", string)
print("After splitting at uppercase letters:", result)
#9
import re

def insert_spaces(text):
    # Use regular expression to find words starting with capital letters
    pattern = r'(?<=[a-z])([A-Z])'
    # Insert a space before each capital letter found
    result = re.sub(pattern, r' \1', text)
    return result

# Example usage
text = "ThisIsAStringWithCapitalWords"
result = insert_spaces(text)
print("Original text:", text)
print("Text with spaces inserted:", result)
#10
def camel_to_snake(camel_case_str):
    snake_case_str = ''
    for char in camel_case_str:
        if char.isupper():
            snake_case_str += '_' + char.lower()
        else:
            snake_case_str += char
    # Remove leading underscore if present
    if snake_case_str.startswith('_'):
        snake_case_str = snake_case_str[1:]
    return snake_case_str

# Example usage
camel_case_str = "convertThisCamelCaseStringToSnakeCase"
snake_case_str = camel_to_snake(camel_case_str)
print("Camel case:", camel_case_str)
print("Snake case:", snake_case_str)"""

