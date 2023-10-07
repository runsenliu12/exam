def mars_calculator(s):
    # 定义计算函数，根据运算符进行不同的计算
    def calc(x, y, op):
        if op == "#":
            return 2 * x + 3 * y + 4
        elif op == "$":
            return 3 * x + y + 2

    # 初始化栈，数字和运算符
    stack = []
    num = 0
    op = None

    # 遍历输入的字符串，添加一个 "#" 是为了处理字符串最后的数字
    for ch in s + "#":
        if ch.isdigit():  # 如果字符是数字
            num = num * 10 + int(ch)  # 累加数字
        else:  # 如果字符是运算符
            if op == "$":  # 如果当前运算符是 "$"
                stack[-1] = calc(stack[-1], num, op)  # 计算并替换栈顶元素
            else:  # 如果当前运算符是 "#"
                stack.append(num)  # 将数字压入栈
            num = 0  # 数字清零
            op = ch  # 更新运算符

    # 处理栈中剩余的元素
    while len(stack) > 1:
        x = stack.pop(0)  # 弹出栈顶元素
        y = stack.pop(0)  # 弹出栈顶元素
        stack.insert(0, calc(x, y, "#"))  # 计算并插入结果到栈顶

    return stack[0]  # 返回栈顶元素，即最后的计算结果


print(mars_calculator("7#6$5#12"))  # 输出：226
