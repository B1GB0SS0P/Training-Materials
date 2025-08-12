"""
All texts written in quotations are instructions and examples for you to use. Do not edit them.

Write your code in the functions given below and return the necessary values.

Uncomment out the test cases to test if your function returns the right values.
Comment it back when moving on to the next question
"""

# QUESTION 1
def summation1(n):
    """
    Return the sum of values from 1 to n.

    >>> summation(1)
    1
    >>> summation(4)
    10
    >>> summation(50) 
    1275
    
    """

    "*** YOUR CODE HERE ***"
    return
print(summation1(1))
print(summation1(4))
print(summation1(50))
print()


# QUESTION 2
def summation(x):
    """
    Return the sum of values in list, x, recursively without using other built-in Python functions.

    >>> summation([1, 2, 3, 4])
    10
    >>> summation([-1, -1, -1, 0])
    -3
    >>> summation([100, 67, 21, 3, -4]) 
    187
    
    """

    "*** YOUR CODE HERE ***"
    return

print(summation([1, 2, 3, 4]))
print(summation([-1, -1, -1, 0]))
print(summation([100, 67, 21, 3, -4]))
print()


# QUESTION 3
def num_eights(n):
    """
    Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    
    """
    
    "*** YOUR CODE HERE ***"
    return

print(num_eights(3))
print(num_eights(8))
print(num_eights(88888888))
print(num_eights(2638))
print(num_eights(86380))
print(num_eights(12345))
print(num_eights(8782089))
print()


# QUESTION 4
def palindrome(x):
    """
    Returns True if x is a palindrome and False otherwise.

    >>> palindrome('aaa')
    True
    >>> palindrome('abba')
    True
    >>> palindrome('1234567898765432I')
    False
    >>> palindrome('aAjHytFVDUgUivgviUgUDVFtyHjAa')
    True

    """
    
    "*** YOUR CODE HERE ***"
    return

print(palindrome('aaa'))
print(palindrome('abba'))
print(palindrome('1234567898765432I'))
print(palindrome('aAjHytFVDUgUivgviUgUDVFtyHjAa'))
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
def digit_distance(n):
    """
    Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777)
    0
    >>> digit_distance(314)
    5
    >>> digit_distance(31415926535)
    32
    >>> digit_distance(3464660003)
    16

    """
    
    "*** YOUR CODE HERE ***"
    return

print(digit_distance(3))
print(digit_distance(777))
print(digit_distance(314))
print(digit_distance(31415926535))
print(digit_distance(3464660003))
print()


# QUESTION 7
def reverse(x):
    """
    Returns the reversed form of string, x.

    >>> reverse('abcdefg')
    gfedcba
    >>> reverse('Hello World!')
    !dlroW olleH
    >>> reverse('SCVU is the best unit')
    tinu tseb eht si UVCS

    """
    
    "*** YOUR CODE HERE ***"
    return

print(reverse('abcdefg'))
print(reverse('Hello World!'))
print(reverse('SCVU is the best unit'))
print()



# QUESTION 8
def pingpong(n):
    """
    Returns the nth element of the pingpong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    8
    >>> pingpong(15)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2

    """
    
    "*** YOUR CODE HERE ***"
    return

print(pingpong(7))
print(pingpong(8))
print(pingpong(15))
print(pingpong(25))
print(pingpong(100))
print()


    
# QUESTION 9
def next_larger_coin(coin):
    """
    FUNCTION DEFINED FOR YOU TO USE: Returns the next larger coin in order.

    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None

    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_smaller_coin(coin):
    """
    FUNCTION DEFINED FOR YOU TO USE: Returns the next smaller coin in order.

    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None

    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1




def count_coins(total):
    """
    Return the number of ways to make change using coins of value of 1, 5, 10, 25.

    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463

    """
    
    "*** YOUR CODE HERE ***"
    return

print(count_coins(15))
print(count_coins(10))
print(count_coins(20))
print(count_coins(100))
print(count_coins(200))