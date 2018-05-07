"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    neg = False
    digits = []
    reversed_num = 0
    if x < 0:
        neg = True
        x = abs(x)  # Modulo operator in Python doesn't return a negative integer
    while x > 0:
        digits.append(x % 10)
        # print (digits)
        x = x // 10
        # print (x)

    power = len(digits) - 1
    print(power)
    for digit in digits:
        reversed_num += digit * pow(10,power)
        print (reversed_num)
        power -= 1

    if neg:
        return -reversed_num
    return reversed_num


print(reverse(1203))