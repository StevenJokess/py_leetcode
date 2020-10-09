# coding=utf-8
'''
version:
Author:  StevenJokess https://github.com/StevenJokess
Date: 2020-10-09 21:36:06
LastEditors:  StevenJokess https://github.com/StevenJokess
LastEditTime: 2020-10-09 22:25:49
Description:
TODO::
Reference:
https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/798678/Beast-96-Python-fully-commented-and-explained-%3A)
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/cong-yi-ban-dao-te-shu-de-fang-fa-dai-ma-jing-jian/
        if len(nums) % 2 == 0:
            median = (nums[len(nums)//2] + nums[len(nums)//2-1]/2 )
'''
#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # 找第k小数
        def helper(nums1, nums2, k):
            if(len(nums1) <len(nums2)):
                nums1, nums2 = nums2 , nums1 #保持nums1比较长
            if(len(nums2) == 0):
                return nums1[k-1] # 短数组空，直接返回
            if(k==1):
                return min(nums1[0], nums2[0])  #找最小数，比较数组首位
            t = min(k//2, len(nums2)) # 保证不上溢?
            if(nums1[t-1] >= nums2[t-1]): # 舍一半
                return helper(nums1, nums2[t:], k-t) # nums2数组的左半边都不需要考虑了
            else:
                return helper(nums1[t:], nums2, k-t)

        k1 = ( len(nums1) + len(nums2) + 1 ) // 2
        k2 = ( len(nums1) + len(nums2) + 2 ) // 2
        return ( helper(nums1,nums2,k1) + helper(nums1,nums2,k2) ) /2



# @lc code=end

