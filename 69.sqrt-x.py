# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 12:15:54
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 14:23:10
Description:
TODO::
Reference:https://leetcode.com/problems/sqrtx/discuss/871095/Python3-solution-using-binary-search
'''
#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 1 or x == 0:
            return x

        l = 0
        r = x//2 if x > 4 else x
        mid = (l+r+1)//2

        while True:
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                r = mid
            elif (mid+1) * (mid+1) <= x:
                l = mid
            mid = (l+r+1)//2





# @lc code=end

