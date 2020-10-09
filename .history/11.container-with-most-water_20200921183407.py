#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# coding=utf-8
'''
@version:
@Author:  StevenJokes https://github.com/StevenJokes
@Date: 2020-06-27 23:48:20
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-09-21 18:34:07
@Description:128 ms	15.3 MB
@TODO::
@Reference:D:\onedrive\文档\code\leetcode\11-container-with-most-water.py
https://leetcode.com/problems/container-with-most-water/discuss/707711/Python-3-or-Faster-than-98.5
https://leetcode.com/problems/container-with-most-water/discuss/651231/Straightforward-Python-solution-O(n)-6-lines-)
'''

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers: l,r
        l, r, maxArea = 0, len(height) - 1, -1
        while l != r:
            maxArea = max(maxArea, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
# @lc code=end

