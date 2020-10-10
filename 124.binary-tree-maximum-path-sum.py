# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 17:21:26
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 17:36:08
Description:
TODO::
Reference:https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/39908/Python-solution-with-comments.
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
        def maxPathSum(self, root):
            if not root:
                return 0
        max_path = float("-inf") # placeholder to be updated
        def get_max_gain(node):
            nonlocal max_path # This tells that max_path is not a local variable
            if node is None:
                return 0
        def oneSum(self, node):
            if not node:
                return 0
            l = max(0, self.oneSum(node.left))
            r = max(0, self.oneSum(node.right))

         current_max_path = max(self.val + l + r,self.val)  # Read first three images of going down the recursion stack
         max_path = max(max_path, current_max_path) # Read first three images of going down the recursion stack

         return node.val + max(gain_on_left, gain_on_right) # Read the last image of going down the recursion stack

     get_max_gain(root) # Starts the recursion chain
     return max_path
# @lc code=end

