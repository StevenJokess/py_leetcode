# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 12:15:54
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 13:56:33
Description:
TODO::
Reference:https://leetcode.com/problems/sqrtx/discuss/871095/Python3-solution-using-binary-search
'''
#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1

        lower = 0
        upper = x//2 + 1 if x > 4 else x # must add 1 to make upper big enough
        middle = (lower + upper)//2

        while True:
            if (middle * middle <= x) and ((middle + 1) * (middle + 1) > x) :
                break
            elif middle * middle > x:
                upper = middle
            elif (middle+1) * (middle+1) <= x:
                lower = middle
            middle = (lower + upper)//2
        return middle




# @lc code=end

