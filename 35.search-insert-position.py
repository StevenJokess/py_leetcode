# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 14:30:13
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 16:01:11
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
        l, r = 0, len(nums)-1
        mid = len(nums)//2  # 让二叉永远左边大，0--8共9个数

        while l < r: # 试图去找，找不到的话最后使得l=r=mid
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid  # 现在右边界为原来的中界
                mid = (l+r)//2  #
            else:
                l = mid  # 现在左边界为原来的中界
                mid = (l+r)//2

        if target < nums[mid]:  # 小，就代替原来位置
            return mid
        else:
            return mid+1  # 大，就在原来位置后面一格



# @lc code=end

