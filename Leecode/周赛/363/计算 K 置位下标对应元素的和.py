from typing import List

"""
输入：nums = [5,10,1,5,2], k = 1
输出：13
解释：下标的二进制表示是： 
0 = 0002
1 = 0012
2 = 0102
3 = 0112
4 = 1002 
下标 1、2 和 4 在其二进制表示中都存在 k = 1 个置位。
因此，答案为 nums[1] + nums[2] + nums[4] = 13 。
示例 2：

输入：nums = [4,3,2,1], k = 2
输出：1
解释：下标的二进制表示是： 
0 = 002
1 = 012
2 = 102
3 = 112
只有下标 3 的二进制表示中存在 k = 2 个置位。
因此，答案为 nums[3] = 1 。
"""


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        count = 0
        for i, j in enumerate(nums):
            if bin(i).count(str(1)) == k:
                count += j
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.sumIndicesWithKSetBits(nums=[5, 10, 1, 5, 2], k=1))
    print(s.sumIndicesWithKSetBits(nums=[4, 3, 2, 1], k=2))
