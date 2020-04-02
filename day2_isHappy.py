"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the
sum of the squares of its digits, and repeat the process until
the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1. Those numbers
for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
# Original solution. Apparently better than only 5% of others lol
def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    for _ in range(10):
        new_num = 0
        for i in str(n):
            print(n,i)
            new_num += int(i)**2
        if new_num == 1:
            return True
        n = new_num
    return False


# Other answers
def is_happy(n):
    s = { 1 }
    
    while n not in s:
        s.add(n)
        n = sum(i * i for i in map(int, str(n)))

    return n == 1