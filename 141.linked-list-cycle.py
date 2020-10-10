# coding=utf-8
'''
version: 
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 16:48:04
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 16:49:45
Description: 
TODO:: 
Reference: 
'''
#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
# @lc code=end

