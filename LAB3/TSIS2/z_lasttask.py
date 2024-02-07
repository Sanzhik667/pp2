#В этом задании я связал две функции с задания 4 и 7 и написал целый код, который будет выводить значения исходя из условия, которое я отметил внизу.
#Given a list of ints, return True if the array contains a prime number next to a prime number somewhere.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def has_adjacent_primes(nums):
    for i in range(len(nums) - 1):
        if is_prime(nums[i]) and is_prime(nums[i + 1]):
            return True
    return False

# Example usage:
result1 = has_adjacent_primes([1, 6, 4, 8, 9, 10])  # False
result2 = has_adjacent_primes([1, 2, 3, 5, 7])  # True
result3 = has_adjacent_primes([4, 6, 8, 10, 13, 17])  # True

print(result1)
print(result2)
print(result3)








