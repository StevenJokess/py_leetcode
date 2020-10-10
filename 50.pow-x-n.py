# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-10 11:35:17
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-10 12:07:06
Description:
TODO::
Reference:https://leetcode-cn.com/problems/powx-n/solution/kuai-su-mi-yang-ti-by-duo1j/
https://leetcode.com/problems/powx-n/discuss/749109/Python-Recursive-Solution-Faster-than-99
https://leetcode.com/problems/powx-n/discuss/345741/python3-Pow(xn)
https://leetcode.com/problems/powx-n/discuss/632283/Python-Clean-solution
'''

#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            return Solution.PowP(1/x, -n)
        else:
            return Solution.PowP(x, n)
    @staticmethod
    def Powp(x, y):
        res = 1
        if y == 0:
            return res
        while y > 0:
            if y % 2 == 1 :
                res = res * x
            y = y >> 1
            x *= x
        return res
            # @lc code=end

