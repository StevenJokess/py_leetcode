# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-09 21:53:46
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-09 23:28:54
Description:
TODO::
Reference:https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/857004/O(n)-greater99.63-40ms-Readable-for-beginners
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/si-lu-qing-xi-yi-ci-bian-li-gao-xiao-qiu-jie-by-jo/
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/
https://www.geeksforgeeks.org/enumerate-in-python/
'''

#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # k右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 （即重复）且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c] #
                c_dict[c] = i # 跳到后面
                # print(k, c, c_dict, c_dict[c], res, i-k, "-1")
            else:
                c_dict[c] = i
                res = max(res, i-k) # 如果是当前最长的，就替换掉之前的。i-k
                # print(k, c, c_dict, c_dict[c], res, i-k, "-2")
        return res

# @lc code=end

