"""#1
def squares_generator(N):
    for i in range(N):
        yield i ** 2

# Example usage:
N = 5
squares = squares_generator(N)

# Iterate over the generated squares
for square in squares:
    print(square)"""
#2
"""def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Get input from the console
n = int(input("Enter a number: "))

# Generate even numbers and print them in comma-separated form
even_numbers = even_numbers_generator(n)
print(','.join(map(str, even_numbers)))"""
#3
"""def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage:
n = 100
for num in divisible_by_3_and_4_generator(n):
    print(num)"""
#4
"""def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Example usage:
a = 1
b = 5
for square in squares(a, b):
    print(square)"""
#5
"""def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Example usage:
n = 10
for num in countdown(n):
    print(num)
"""


