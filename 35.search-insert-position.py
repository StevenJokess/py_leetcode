# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 14:30:13
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 15:01:28
Description:
TODO::
Reference:index方法获取的只是第一个索引
https://blog.csdn.net/Jerry_1126/article/details/88924288
'''
#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        leng = len(nums)
        print(leng)
        if leng == 0:
            return 0

        l, r = nums[0], nums[-1]

        middle = leng//2
        midnum = nums[middle]

        while l < r: # 找
            if target == l:
                return nums.index(l)
            if target == r:
                return nums.index(r)
            if target == midnum:
                return middle
            if l < target < midnum:
                middle = middle//2
                l = nums[middle]
            if midnum < target < r:
                middle = (middle+leng+1)//2
                r = nums[middle]
        return middle


# @lc code=end

