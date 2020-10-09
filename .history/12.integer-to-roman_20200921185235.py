# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-09-21 18:38:46
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-09-21 18:52:35
Description:
TODO::
Reference:https://leetcode.com/problems/integer-to-roman/discuss/6304/Python-simple-solution.
bigdatabeast
https://leetcode.com/problems/integer-to-roman/discuss/264454/Python-recursion-beat-97
'''
#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        RomanNum = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}

        res = ""
        for i in RomanNum:
            res += (num//i) * RomanNum[i]
            num %= i
        return res
# @lc code=end

