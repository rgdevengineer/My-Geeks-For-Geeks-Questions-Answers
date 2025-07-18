
'''
For loop - Python

Writing for loop in Python is a tad different from C++ and Java counterparts. In this question, we'll learn to print table by using the for loop.

You are given a number N, you need to print its multiplication table.

Note: Please go through the range function to understand why it's useful in for loops.

Example 1:

Input:
N = 5
Output:
5 10 15 20 25 30 35 40 45 50
Example 2:

Input:
N = 6
Output:
6 12 18 24 30 36 42 48 54 60
Your Task:
This is a function problem. You don't need to take input of testcases. Just complete the function multiplicationTable() that takes N as input.

Constraints:
1 <= N <= 1018
'''
def multiplicationTable(N):
    for n in range(1, 11):
        print(n*N, end=' ')
