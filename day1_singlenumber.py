
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
# Initial attempt in comments below. Superior attempt is
# bitwise comparison, always maintaining in cursor that
# value which has only once appeared in the input array,
# allowing us to pass through list just once.


#         dic = {}
#         for item in nums:
#             if item in dic.keys():
#                 dic[item] += 1
#             else:
#                 dic[item] = 1
                
#         for num in dic.keys():
#             if dic[num] == 1:
#                 return num
    n = len(nums)
    cursor = nums[0]
    
    for i in range(1, n):
        cursor = cursor ^ nums[i]
    return cursor
