# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 14:30:13
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 15:46:00
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
        if leng == 0:
            return 0

        l, r = 0, leng-1

        middle = leng//2  # 让二叉永远左边大，0--8共9个数

        if leng == 1:
            if target < nums[l]:
                return l
            if target == nums[l]:
                return l
            if target > nums[r]:
                return r+1

        while l < r: # 找
            # 边界处理
            if target < nums[l]:
                return l
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            if target > nums[r]:
                return r+1
            if target == nums[middle]:
                return middle
            # ----------------------------------------------------------------
            if nums[l] < target < nums[middle]:
                r = middle  # 现在右边界为原来的中界
                middle = (l+r)//2  #
            if nums[middle] < target < nums[r]:
                l = middle  # 现在左边界为原来的中界
                middle = (l+r)//2
        if target < nums[middle]:  # 小，就代替原来位置
            return middle
        else:
            return middle+1  # 大，就在原来位置后面一格


# @lc code=end

