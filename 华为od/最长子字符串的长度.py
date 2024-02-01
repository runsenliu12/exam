def find_longest_even_o(s):
    zero_count = s.count("o")  # 统计字符串中'o'的个数

    if zero_count % 2 == 0:
        return len(s)  # 如果'o'的个数是偶数，返回字符串长度
    else:
        return len(s) - 1  # 如果'o'的个数是奇数，返回字符串长度减一


# 获取输入
s = input()

# 调用函数并输出结果
result = find_longest_even_o(s)
print(result)
