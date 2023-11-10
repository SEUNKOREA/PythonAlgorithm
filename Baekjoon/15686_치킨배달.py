import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

home_coord = []
chicken_coord = []
for x in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for y, value in enumerate(row):
        if value == 1: # 집
            home_coord.append((x+1, y+1))
        elif value == 2: # 치킨집
            chicken_coord.append((x+1, y+1))

# 치킨 집의 개수가 i(1~m)일 때 치킨집 선택해서 후보리스트 만들기
chicken_candidate_list = []
for i in range(1, m+1):
    chicken_candidate_list.extend(list(combinations(chicken_coord, i)))

answer = 987654321
for selected_chicken_list in chicken_candidate_list:
    temp = 0
    for home in home_coord:
        min_dist_per_home = 987654321
        for chicken in selected_chicken_list:
            dist = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])
            if dist < min_dist_per_home :
                min_dist_per_home = dist
        temp += min_dist_per_home
    if temp < answer:
        answer = temp

print(answer)
