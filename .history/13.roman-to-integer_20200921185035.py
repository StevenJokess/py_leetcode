# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-09-21 18:46:49
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-09-21 18:50:35
Description:
TODO::
Reference:D:\onedrive\leetcode\Python\12.integer-to-roman.py
https://leetcode.com/problems/roman-to-integer/discuss/450264/Python-Beginner-98-fast-100-Memo
'''
#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        RomanNum = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ""
        for i in s[::-1]:
            res += (num//i) * RomanNum[i]
            num %= i
        return res
# @lc code=end

