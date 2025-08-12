"""
All texts written in quotations are instructions and examples for you to use. Do not edit them.

Write your code in the functions given below and return the necessary values.

Uncomment out the test cases to test if your function returns the right values.
Comment it back when moving on to the next question
"""

# QUESTION 1
def summation(x):
    """
    Return the sum of values in list, x, without using other built-in Python functions.

    >>> summation([1, 2, 3, 4])
    10
    >>> summation([-1, -1, -1, 0])
    -3
    >>> summation([100, 67, 21, 3, -4]) 
    187
    
    """

    "*** YOUR CODE HERE ***"
    return

print(summation([1, 2, 3, 4]), 10 == summation([1, 2, 3, 4]))
print(summation([-1, -1, -1, 0]), -3 == summation([-1, -1, -1, 0]))
print(summation([100, 67, 21, 3, -4]), summation([100, 67, 21, 3, -4]) == 187)


# QUESTION 2
def largest_factor(n):
    """
    Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    
    """

    "*** YOUR CODE HERE ***"
    return

print(largest_factor(15), 5 == largest_factor(15))
print(largest_factor(80), 40 == largest_factor(80))
print(largest_factor(13), largest_factor(13) == 1)
print()



# QUESTION 3
def even_numbers(x):
    """
    Return the list, x, excluding its odd numbered values.

    >>> even_numbers([1, 2, 3, 4])
    [2, 4]
    >>> even_numbers([-1, -1, -1, 0])
    [0]
    >>> even_numbers([100, 67, 21, 3, -4]) 
    [100, -4]
    
    """

    "*** YOUR CODE HERE ***"
    return

print(even_numbers([1, 2, 3, 4]), [2,4] == even_numbers([1, 2, 3, 4]))
print(even_numbers([-1, -1, -1, 0]), [0] == even_numbers([-1, -1, -1, 0]))
print(even_numbers([100, 67, 21, 3, -4]), [100, -4] == even_numbers([100, 67, 21, 3, -4]))
print()



# QUESTION 4
def triangle(x):
    """
    Return the triangle pattern of '*' from 1 to n.

    >>> triangle(0)
    >>> triangle(1)
    *
    >>> triangle(4) 
    *
    **
    ***
    ****
    
    """

    "*** YOUR CODE HERE ***"
    return

print(triangle(0), '' == triangle(0))
print(triangle(1), '*\n' == triangle(1))
print(triangle(4), '*\n**\n***\n****\n'== triangle(4))
print()



# QUESTION 5
def hailstone(n):
    """
    Print the hailstone sequence starting at n AND return its length at the end.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """

    "*** YOUR CODE HERE ***"
    return

a = hailstone(10)
print(a)
b = hailstone(1)
print(b)
print()



# QUESTION 6
def date(month, year):
    """
    Return the month and year that is 22 months after current month and year.

    >>> date(1, 1999)
    November 2000
    >>> date(11, 2011)
    September 2013
    >>> date(12, 2024) 
    October 2026
    
    """

    "*** YOUR CODE HERE ***"
    return

print(date(1, 1999), date(1, 1999) == 'November 2000')
print(date(11, 2011), date(11, 2011) == 'September 2013')
print(date(12, 2024), date(12,2024) == 'October 2026')
print()



# QUESTION 7a
square = lambda x: x**2
identity = lambda x:x
triple = lambda x:x*3
increment = lambda x:x+1



# QUESTION 7b
def product(n, term):
    """
    Return the product of the first n terms in a sequence.

    n: a positive integer
    term: a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162

    """
    
    "*** YOUR CODE HERE ***"
    return

print(product(3, identity), product(3, identity) == 6)
print(product(5, identity), product(5, identity) == 120) 
print(product(3, square), product(3, square) == 36)   
print(product(5, square), product(5, square) == 14400)    
print(product(3, increment), product(3, increment) == 24) 
print(product(3, triple), product(3, triple) == 162)
print()



# QUESTION 8
add = lambda x, y: x + y
mul = lambda x, y: x * y

def accumulate(merger, start, n, term):
    """
    Return the result of merging the first n terms in a sequence and start.
    The terms to be merged are term(1), term(2), ..., term(n). merger is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> # ((2 * 1^2 * 2) * 2^2 * 2) * 3^2 * 2
    >>> accumulate(lambda x, y: 2 * x * y, 2, 3, square)
    576
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    
    """
    
    "*** YOUR CODE HERE ***"
    return

print(accumulate(add, 0, 5, identity))
print(accumulate(add, 11, 5, identity)) 
print(accumulate(add, 11, 0, identity)) 
print(accumulate(add, 11, 3, square))   
print(accumulate(mul, 2, 3, square))  

print(accumulate(lambda x, y: x + y + 1, 2, 3, square))
print(accumulate(lambda x, y: 2 * x * y, 2, 3, square))
print(accumulate(lambda x, y: (x + y) % 17, 19, 20, square))