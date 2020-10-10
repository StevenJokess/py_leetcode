# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 10:21:05
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 11:34:14
Description:
TODO::
Reference:D:\onedrive\leetcode\Python\1.two-sum.py
https://leetcode.com/problems/3sum/discuss/7392/Python-easy-to-understand-solution-(O(n*n)-time).
'''
#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = [] # List[List[int]
        nums.sort()
        leng = len(nums)
        for i in range(leng-2):# need at least 3 numbers to continue. py2:xrange
            if nums[i] > 0:
                break # sum of positive will be always >0
            if i > 0 and nums[i] == nums[i - 1]: # prevent checking duplicate again.
                continue
            l, r = i+1, leng-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: #prevent checking duplicate， l < r保证了不溢出
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

# @lc code=end

