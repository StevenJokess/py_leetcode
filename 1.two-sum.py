#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author:  StevenJokes https://github.com/StevenJokes
@Date: 2020-06-28 04:48:10
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-09-21 18:36:44
@Description: (44 ms)(15.1 MB)
@TODO::
@Reference:https://leetcode.com/problems/two-sum/discuss/2/Python-solution-using-hash
https://leetcode.com/problems/two-sum/discuss/320/5-line-Python-solution-hashtable-beats-90/216950/
enumerate(nums):https://www.runoob.com/python/python-func-enumerate.html
https://zhuanlan.zhihu.com/p/61077440
图解LeetCode 初级算法 P94
https://blog.csdn.net/Norsaa/article/details/77674193
# if num not in dict: # have not only one solution
#   dict[num] = i
'''

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        # @return a list, [index1, index2]
        dict = {}
        for i, num in enumerate(nums):
            if target - num in dict:
                return [dict[target-num], i]
            dict[num] = i
        return []
# @lc code=end
