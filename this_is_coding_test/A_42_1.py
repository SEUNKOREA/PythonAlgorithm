"""
시간복잡도 O(p*g)로 시간초과 발생가능
"""

# 전체 탑승구의 수
g = int(input())
# 비행기의 수
p = int(input())

graph = [[0] * (g+1) for _ in range(p+1)]
data = []
indegree = [0] * (g+1)

for i in range(1, p+1):
    port = int(input())
    data.append((port, i))
    for j in range(1, port+1):
        indegree[j] += 1
        graph[i][j] = 1

data.sort()

answer = 0

for d in data:
    gate_num, plane_num = d

    # 도킹할 수 있는 탑승 구 중 indegree 값이 가장 작은 탑승구 선택
    max_indegree = -1
    final_gate_num = False
    for idx, g in enumerate(graph[plane_num][1:]):
        if g == 1:
            if indegree[idx+1] > max_indegree:
                max_indegree = indegree[idx+1]
                final_gate_num = idx+1

    if final_gate_num and indegree[final_gate_num] != 0:
        indegree[final_gate_num] = 0
        answer += 1
    else:
        break


print(answer)