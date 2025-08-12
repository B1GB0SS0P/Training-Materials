# Mini Exercise 4


    1. The factorial of an integer N is the product of all the integers between 1 and N, inclusive. Write a function that computes the factorial of a given integer N.
    Sample Input: 5
    Output: 120
<hr>

    2. Guess My Number Game (Design the function for both versions)

    Version A: The computer picks a random number between 1 and 100 that the player has to guess. For each guess, the computer must tell the player if the number is too small or too large for the actual number. When the player gets the number, the program will display the number of tries the player used. A sample output is shown below.

    Enter your guess: 50
    Too small
    Enter your guess: 70
    Too small
    Enter your guess: 90
    Too large
    Enter your guess: 85
    Too small
    Enter your guess: 87
    Too small
    Enter your guess: 88
    Too small
    Enter your guess: 89
    You've got it in 7 tries!

    Version B: The player and the computer trade places. That is, the player picks a random number between 1 and 100 that the computer has to guess. Before you start, think about how the computer will guess.
    Hint: You may use the random.randint module to generate a random number from among numbers between two arguments, included.
<hr>

    3. Write a function that takes an integer, n, and prints out the numbers in the Fibonacci sequence until the nth number in the sequence.

    Sample Input: 5
    Output:
    0
    1
    1
    2
    3
<hr>

    4. Write a function that gets a dictionary with names as keys and dates of their respective ORD dates (DDMMYY), and returns a dictionary in a different format with the date as the key and value as a list of people sharing the same ORD date.

    Sample Input: {'Keith': '070126', 'Adam': '070126', 'Zen': '030725'}
    Output: {'070126': ['Keith', 'Adam'], '030725': ['Zen']}