# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-09-21 18:38:46
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-09-21 18:55:31
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
        self.answer = ''

        def helper(num, base, divide_two, flag):
        if base == 0:
            return
        if base == 1000:
            for _ in range(num // base): self.answer = self.answer + look_table[base]
        else:
            if num // base == 4 and flag:   # Handle 9***
                self.answer = self.answer[:-1] + look_table[base] + look_table[base * 10]
            elif num // base == 4 and (not flag):   # Handle 4***
                self.answer = self.answer + look_table[base] + look_table[base * 5]
            else:
                for _ in range(num // base):
                    self.answer = self.answer + look_table[base]
            if num > base:
                flag = True
            else:
                flag = False

        if divide_two:
            helper(num % base, base // 2, not divide_two, flag)
        else:
            helper(num % base, base // 5, not divide_two, flag)

        for i in RomanNum:
            res += (num//i) * RomanNum[i]
            num %= i
        return self.answer
# @lc code=end

