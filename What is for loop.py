"""
You have a positive integer number N as an input. Please write a program in Python 3 that calculates the sum in range 1 and N.

Limitations:
N <= 10^25;
Execution time: 0.1 seconds.

Examples:
Input: 1
Output: 1

Input: 3
Output: 6

Input 10:
Output: 55


"""

def forloop(n):
    return ((1 + n) * n) // 2


print(forloop(10))

for_loop = lambda x: (x * (x + 1)) // 2
for_loop(10)





