
'''
The FizzBuzz Program

You are given a number  and you have to print your answer according to the following:
If the number is divisible by 3, you print "Fizz" (without quotes)
If the number is divisible by 5, you print "Buzz" (without quotes)
If the number is divisible by both 3 and 5, you print "FizzBuzz" (without quotes)
In any other case, you print the number itself

Note: You should add a newline character after print() statement.

Examples:

Input: number = 3
Output: Fizz
Explanation: Here, the number is divisible by 3, so Fizz is printed.
Input: number = 5
Output: Buzz
Explanation: Here the number is divisible by 5, so Buzz is printed.
Input: number = 15
Output: FizzBuzz
Explanation: Here, the number 15 is divisible by both 3 and 5, so FizzBuzz is printed.
Constraints:

1 <= number <= 100
'''


def fizzBuzz(number):
    if number % 5 == 0 and number % 3 == 0:
        print('FizzBuzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0:
        print('Fizz')
    else:
        print(number)