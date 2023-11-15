class Solution:
    def isValid(self, s: str) -> bool:
        # 创建一个空列表 res 来模拟栈
        res = []

        # 定义一个字典，存储右括号与对应的左括号的映射关系
        mydict = {")": "(", "]": "[", "}": "{"}

        # 遍历输入的字符串 s 中的每个字符
        for i in s:
            # 如果当前字符是左括号（'('、'['、'{'），则将其压入栈中
            if i in ["(", "[", "{"]:
                res.append(i)
            # 如果当前字符是右括号
            elif res and res[-1] == mydict[i]:
                # 检查栈不为空，并且栈顶元素与当前字符对应的左括号匹配
                # 则弹出栈顶元素，表示匹配成功
                res.pop()
            else:
                # 如果不匹配，直接返回False
                return False

        # 最后，检查栈是否为空，如果为空则说明所有括号都匹配成功，返回True，否则返回False
        return len(res) == 0
