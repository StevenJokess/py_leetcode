# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 16:51:49
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 17:02:58
Description:
TODO::
Reference:
https://leetcode.com/problems/linked-list-cycle-ii/discuss/358863/Python-97.29-Faster
https://leetcode.com/problems/linked-list-cycle-ii/discuss/461075/Python-two-pointers-O(n)-time-O(1)-space
'''
#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return fast.next
        return None

        # @lc code=end

