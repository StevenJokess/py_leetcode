# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 12:15:54
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 13:44:40
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
        upper = x // 2 if x > 4 else x
        middle = (lower + upper)//2

        while True:
            if (middle * middle <= x) and ((middle + 1) * (middle + 1) > x) :
                break
            elif (middle -1) * (middle -1) > x:
                upper = (upper + middle)//2
                middle = (lower + upper)//2
            elif (middle +2) * (middle +2) < x:
                lower = (lower + middle)//2
                middle = (lower + upper)//2
        return middle




# @lc code=end

