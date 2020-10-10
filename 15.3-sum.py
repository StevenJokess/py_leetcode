# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 10:21:05
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 10:39:52
Description:
TODO::
Reference:D:\onedrive\leetcode\Python\1.two-sum.py
'''
#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dict = {}
        res = [] # List[List[int]
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if 0  - num1 - num2 in dict:
                    res.append([0 - num1 - num2, num1, num2])
                dict[num2] = j
            dict[num1] = i
        return res

# @lc code=end

