class Solution:
    def calculate(self, s: str) -> int:
        stack = []  # 用于存储数字和运算符
        num = 0  # 用于临时存储当前数字
        sign = 1  # 用于表示当前的符号，默认为正号
        result = 0  # 用于存储最终的计算结果

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in "+-":
                result += sign * num
                num = 0
                sign = 1 if char == "+" else -1
            elif char == "(":
                stack.append((result, sign))
                result = 0
                sign = 1
            elif char == ")":
                result += sign * num
                num = 0
                prev_result, prev_sign = stack.pop()
                result = prev_result + prev_sign * result

        result += sign * num
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.calculate("156+4*5"))
