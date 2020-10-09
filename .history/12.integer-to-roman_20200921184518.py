# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-09-21 18:38:46
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-09-21 18:45:18
Description:
TODO::
Reference:https://leetcode.com/problems/integer-to-roman/discuss/6304/Python-simple-solution.
bigdatabeast
'''
#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        RomanNum = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ""
        for i in RomanNum:
            res += (num//i) * RomanNum[i]
            num %= i
        return res
# @lc code=end

