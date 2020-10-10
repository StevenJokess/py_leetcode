# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 22:34:33
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 23:34:56
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
        if s == "":
            return ""

        res = ""

        for mid in range(len(s)):
            odd  = self.findPalindrome(mid, mid, s)
            even = self.findPalindrome(mid, mid+1, s)
        res = odd if len(odd)>len(even) else even
        return res

    def findPalindrome(self, l: int, r: int, s: str) -> str:
        tmp = ""
        while s[l] == s[r] and l >= 0 and r <= len(s)-1:
            l -= 1
            r += 1
        tmp = s[l+1:r] if len(s[l+1:r]) > len(tmp) else tmp # 没变化前
        return tmp





# @lc code=end

