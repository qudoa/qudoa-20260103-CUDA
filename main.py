```python
def factorial(n):
      if n == 0:
                return 1
else:
        return n * factorial(n - 1)

# Function to check if a number is prime
def is_prime(num):
      if num <= 1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                      if num % i == 0:
                                    return False
                            return True

# Function to find the largest prime number less than or equal to n
def largest_prime(n):
      for i in range(n, 1, -1):
                if is_prime(i):
                              return i

# Function to calculate the sum of squares of first n natural numbers
def sum_of_squares(n):
      return n * (n + 1) * (2 * n + 1) // 6

# Function to check if a string is a palindrome
def is_palindrome(s):
      return s == s[::-1]

# Function to convert a number to its octal representation
def to_octal(num):
      return oct(num)[2:]

# Function to reverse a string
def reverse_string(s):
      return s[::-1]

# Function to find the maximum and minimum values in a list
def max_min(lst):
      return max(lst), min(lst)

# Function to calculate the factorial of a number using recursion
def factorial_recursive(n):
      if n == 0:
                return 1
else:
        return n * factorial_recursive(n - 1)

# Function to calculate the sum of digits of a number
def sum_of_digits(num):
      return sum(int(digit) for digit in str(num))

# Function to check if a number is even or odd
def even_odd(num):
      return "Even" if num % 2 == 0 else "Odd"

# Function to find the second largest number in a list
def second_largest(lst):
      lst = list(set(lst))
    if len(lst) < 2:
              return None
    return max(lst) if lst.count(max(lst)) == 1 else None

# Function to calculate the factorial of a number using an iterative approach
def factorial_iterative(n):
      result = 1
    for i in range(2, n + 1):
              result *= i
    return result

# Function to check if a number is a perfect square
def is_perfect_square(num):
      return int(num ** 0.5) ** 2 == num

# Function to calculate the power of a number
def power(base, exp):
      result = 1
    for _ in range(exp):
              result *= base
    return result

# Function to find the greatest common divisor of two numbers
def gcd(a, b):
      while b:
                a, b = b, a % b
    return a

# Function to check if a string is alphanumeric
def is_alphanumeric(s):
      return s.isalnum()

# Function to remove duplicates from a list
def remove_duplicates(lst):
      return list(dict.fromkeys(lst))
```
