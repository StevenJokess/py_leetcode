# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 14:30:13
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 14:41:52
Description:
TODO::
Reference:
'''
#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = nums[0], nums[-1]
        leng = len(nums)
        middle = leng//2+1
        midnum = nums[middle]
        while l<r: # 找
            if target == l:
                return l
            if target == r:
                return r
            if l < target < midnum:
                middle = middle//2 +1
                l = nums[middle]
            if midnum < target < r:
                middle = (middle+leng)//2 -1
                r = nums[middle]



# @lc code=end

