import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

chicken = []
house = []
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))
        
candidates = combinations(chicken, m)
answer = int(1e9)
for candidate in candidates:
    city_chicken_dist = 0
    for i in range(len(house)):
        chicken_dist = int(1e9)
        for j in range(len(candidate)):
            dist = abs(house[i][0]-candidate[j][0]) + abs(house[i][1]-candidate[j][1])
            chicken_dist = min(chicken_dist, dist)
        city_chicken_dist += chicken_dist
    answer = min(city_chicken_dist, answer)
print(answer)