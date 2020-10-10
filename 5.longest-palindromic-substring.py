# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 22:34:33
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 23:15:29
Description:
TODO::
Reference:kanhar22:https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).
'''
#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        if s == "":
            return ""
        for i in range(len(s)):
            mid = i
            l = r = mid

            while s[l] == s[r] and l >= 0 and r <= len(s)-1:
                l -= 1
                r += 1
            res = s[l+1:r] if len(s[l+1:r]) > len(res) else res # 没变化前
        return res





# @lc code=end

