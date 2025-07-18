
'''
String Functions - II - Python

Given a string S, the task is to determine whether the string starts and ends with the characters 'gfg' (case insensitive). In order to complete this task, you need to utilize the string functions S.lower(), S.upper(), S.startswith('string2'), and S.endswith('string2'). By using these functions, you can check if the given string S meets the specified conditions of starting and ending with 'gfg'.

Example 1:

Input:
S: "gFgabcdEGfG"
Output:
Yes
Explanation:
The given string "gFgabcdEGfG" starts with "gfg" and also ends with "gfg" after converting it to lowercase ("gfgabcdegfg"), so the output is Yes.
Example 2:

Input:
S: "GgfhTnagfg"
Output:
No
Explanation:
The given string "GgfhTnagfg" only ends with "gfg" after converting it to lowercase ("ggfhtnagfg"), but it does not start with "gfg", so the output is No.
Your Task:
You are given a string, 'S'. You need to write a function called 'gfg' that takes 'S' as input and checks if the string starts and ends with the substring 'gfg'.

If the given string starts and ends with 'gfg', the function should print "Yes". Otherwise, it should print "No".

Constraints:
1 ≤ |S| ≤ 105
'''

def gfg(S):
    b = S.lower()
    if 'gfg' in b[:3] and 'gfg' in b[:-3]:
        print("Yes")
    else:
        print("No")