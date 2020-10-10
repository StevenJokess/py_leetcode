# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 16:51:49
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 17:20:31
Description:
TODO::
Reference:
https://leetcode.com/problems/linked-list-cycle-ii/discuss/358863/Python-97.29-Faster
https://leetcode.com/problems/linked-list-cycle-ii/discuss/461075/Python-two-pointers-O(n)-time-O(1)-space
https://www.bilibili.com/video/BV1YK411K7rq?from=search&seid=13525766042231041427
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

# s(slow) = D + C1 + m*(C1+C2)
# s(fast) = D + C1 + n*(C1+C2)
# s(fast) = 2*s(slow)
# 0<m<n,

# (n-2m-1)*(C1+C2) +C2=D 相遇！


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                start = head
                while start != slow:
                    slow = slow.next
                    start = start.next
                return slow  # 相遇！
        return None

        # @lc code=end

