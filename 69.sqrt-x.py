# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 12:15:54
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 13:33:45
Description:
TODO::
Reference:
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
        upper = x / 2 if x > 4 else x
        middle = (lower + upper)/2

        while middle*middle != x:
            if middle * middle < x:
                lower = (lower + middle)/2
                middle = (lower + upper)/2
            else:
                upper = (upper + middle)/2
                middle = (lower + upper)/2
        return int(middle)




# @lc code=end

