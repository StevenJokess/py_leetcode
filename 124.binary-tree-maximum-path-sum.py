# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 17:21:26
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 17:22:40
Description:
TODO::
Reference:
'''
#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return sum(root)
# @lc code=end

