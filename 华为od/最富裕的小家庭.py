n = int(input())  # 树的节点数
wealth = list(map(int, input().split()))  # 每个节点的财富值

# 将每个节点的财富值插入数组，索引对应成员编号 1~N
wealth.insert(0, 0)

family_wealth = []
family_wealth.extend(wealth)

# 根据节点间的关系，计算每个节点所在小家庭的总财富
for _ in range(n - 1):
    parent, child = map(int, input().split())
    family_wealth[parent] += wealth[child]

# 找到最富裕的小家庭的财富和
print(max(family_wealth))
