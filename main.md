- dfs

以下是四种常见算法的Python模板，包括深度优先搜索（DFS）、动态规划（DP）、单调栈和滑动窗口的模板：

1. 深度优先搜索（DFS）模板：

```python
def dfs(node, visited):
    if node in visited:
        return
    
    # 标记节点为已访问
    visited.add(node)
    
    # 处理当前节点
    # ...

    # 递归遍历相邻节点
    for neighbor in get_neighbors(node):
        dfs(neighbor, visited)
```



79. 单词搜索.py
200. 岛屿数量.py
797. 所有可能的路径.py
1020. 飞地的数量.py



- dp


2. 动态规划（DP）模板：

```python
def dp_solution(nums):
    n = len(nums)
    dp = [0] * n
    
    dp[0] = nums[0]
    
    for i in range(1, n):
        # 计算 dp[i] 的值
        dp[i] = max(dp[i-1] + nums[i], nums[i])
    
    return max(dp)
```

数位dp 233. 数字 1 的个数.py

139. 单词拆分.py
354. 俄罗斯套娃信封问题.py
322. 零钱兑换.py
718. 最长重复子数组.py

- 单调栈


3. 单调栈模板：

以下是单调栈算法的 Python 模板，带有中文注释：

```python
def monotonic_stack(nums):
    n = len(nums)
    stack = []  # 存储索引的栈

    # 遍历数组中的元素
    for i in range(n):
        # 确保栈不为空且当前元素大于栈顶元素
        while stack and nums[i] > nums[stack[-1]]:
            # 对栈顶元素进行操作
            top = stack.pop()
            # 可以在这里执行与弹出元素或其索引相关的操作

        # 将当前索引压入栈
        stack.append(i)

    # 在处理完所有元素后，栈可能仍然包含一些索引
    # 如果需要，可以在这里执行任何剩余的操作

# 示例用法：
nums = [3, 1, 4, 2, 5]
monotonic_stack(nums)
```

这个模板是解决涉及查找数组中每个元素的下一个更大（或更小）元素的问题的基本结构。你可以根据具体的问题要求定制模板。

以下是模板的详细说明：

1. 遍历数组中的元素。
2. 对于每个元素，检查栈是否不为空，并且当前元素是否大于（或小于）栈顶元素。
3. 如果条件满足，则从栈中弹出元素，并对弹出的元素执行相关操作（例如，计算下一个更大元素）。
4. 将当前索引压入栈。
5. 在处理完所有元素后，如果需要，执行任何仍在栈中的元素的操作。


题目：

84. 柱状图中最大的矩形.py


- 滑块

4. 滑动窗口模板：

```python
def sliding_window(nums, k):
    n = len(nums)
    left = 0
    result = []

    for right in range(n):
        # 增加右边界
        # ...

        while right - left >= k:
            # 缩小窗口
            # ...

        # 更新结果
        # ...

        left += 1

    return result
```

这些模板可以作为各自算法的基础框架，根据具体问题进行适当的修改和扩展。在实际应用中，需要根据问题的要求来设计算法的细节部分。

题目：

 30. 串联所有单词的子串
76. 最小覆盖子串