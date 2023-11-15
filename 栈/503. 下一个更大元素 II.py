from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 将原始数组复制一次并拼接在原数组后面，处理循环数组的情况
        nums = nums + nums

        # 创建一个栈来存储元素的索引
        stack = []

        # 初始化一个结果列表，将所有元素的下一个更大元素初始化为-1
        res = [-1] * len(nums)

        # 遍历两倍长度的数组
        for i in range(len(nums)):
            # 如果栈不为空，并且当前元素大于栈顶元素所表示的元素
            while stack and nums[i] > nums[stack[-1]]:
                # 弹出栈顶元素
                small = stack.pop()
                # 将栈顶元素的下一个更大元素设置为当前元素
                res[small] = nums[i]

            # 将当前元素的索引压入栈中
            stack.append(i)

        # 返回结果列表的前半部分，因为数组已经复制了一次
        return res[: len(res) // 2]


if __name__ == "__main__":
    # 创建Solution类的实例
    s = Solution()

    # 测试用例1：nums = [1, 2, 1]
    result1 = s.nextGreaterElements([1, 2, 1])
    print(result1)

    # 测试用例2：nums = [1, 2, 3, 4, 3]
    result2 = s.nextGreaterElements([1, 2, 3, 4, 3])
    print(result2)
