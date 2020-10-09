#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author:  StevenJokes https://github.com/StevenJokes
@Date: 2020-06-28 05:09:51
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-09-21 18:36:33
@Description:76 ms 13.9 MB
@TODO::
@Reference:https://leetcode.com/problems/add-two-numbers/discuss/352181/Python3-Carry-sum10
'''
#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur =ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //=10
        return dummy.next
# @lc code=end

