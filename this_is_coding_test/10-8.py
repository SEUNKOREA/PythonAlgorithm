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

# 집의 개수(n), 길의 개수(m)
n, m = map(int, input().split())
# 도로 유지비 정보 입력
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 집과 b번 집을 연결하는 길의 유지비가 c
    edges.append((c, a, b))

edges.sort()

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

result = 0
last = 0

for edge in edges:
    cost, a, b = edge
    # 사이클을 발생시키지 않으면 스팬트리로 추가
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result-last)

