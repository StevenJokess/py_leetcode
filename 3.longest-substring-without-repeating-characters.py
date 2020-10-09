# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-09 21:53:46
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-09 22:49:14
Description:
TODO::
Reference:https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/857004/O(n)-greater99.63-40ms-Readable-for-beginners
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/si-lu-qing-xi-yi-ci-bian-li-gao-xiao-qiu-jie-by-jo/
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/
'''

#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0

        for i in range(n):
            # 遍历，若不重复则记录该字符
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            if i not in tep:
                tep += i
            # 如果遇到了已经存在的字符，则找到该字符所在位置，删除该字符，并保留该位置之后的子串，并把当前字符加入到最后，完成更新
            else:
                tep = tep[tep.index(i)+1:]
                tep += i
            # 如果是当前最长的，就替换掉之前存储的最长子串
        if len(tep) > len(ans):
                    ans = tep
        return ans

# @lc code=end

