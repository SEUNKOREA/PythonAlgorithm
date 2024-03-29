from collections import deque

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 여행지의 수(n), 여행 계획에 속한 도시의 수(m)
n, m = map(int, input().split())

# 부모 노드 테이블 각 노드 번호로 초기화
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

# 두 여행지가 서로 연결되어 있는지
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i, j)

# 한울이의 여행계획에 포함된 여행지의 번호
plan = list(map(int, input().split()))

answer = "YES"
for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        answer = "NO"
        break

print(answer)