import sys


# 计算感染所有电脑的最短时间
def shortest_infection_time(n, connections, start_computer, connection_info):
    # 创建邻接表表示网络连接关系
    graph = {}

    # 读取网络连接信息并构建邻接表
    for i in range(connections):
        u, v, w = connection_info[i]
        graph.setdefault(u, [])
        graph[u].append([v, w])  # 将连接信息加入到对应起始电脑号的连接列表中

    # 初始化记录感染时间的列表，初始值设为无穷大
    dist = [sys.maxsize] * (n + 1)
    dist[start_computer] = 0  # 病毒开始感染的电脑所需时间为0

    # 初始化待检查的电脑列表和访问标记列表
    need_check = [start_computer]
    visited = [False] * (n + 1)
    visited[start_computer] = True

    # 使用Dijkstra算法计算感染所有电脑的最短时间
    while len(need_check) > 0:
        cur = need_check.pop()
        visited[cur] = False

        # 检查当前电脑是否有连接的其他电脑
        if graph.get(cur) is not None:
            # 遍历当前电脑连接的其他电脑
            for v, w in graph[cur]:
                new_dist = dist[cur] + w

                # 更新感染时间列表中的值，找到更短的感染时间
                if dist[v] > new_dist:
                    dist[v] = new_dist
                    # 如果电脑未被访问过，则加入待检查列表中，并按感染时间排序
                    if not visited[v]:
                        visited[v] = True
                        need_check.append(v)
                        need_check.sort(key=lambda x: -dist[x])

    # 计算最终结果，如果有电脑无法感染，则返回-1
    ans = max(dist[1:])
    return -1 if ans == sys.maxsize else ans


# 获取输入数据
num_computers = int(input())  # 局域网内电脑个数
total_connections = int(input())  # 总共多少条网络连接
connection_info = []
for i in range(total_connections):
    connection = list(map(int, input().split()))  # 网络连接信息：起始电脑号、目标电脑号、感染时间
    connection_info.append(connection)

start_computer = int(input())  # 病毒最开始所在电脑号

# 计算感染所有电脑的最少时间
result = shortest_infection_time(
    num_computers, total_connections, start_computer, connection_info
)
print(result)
