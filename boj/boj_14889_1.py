"""
조합으로 풀이
"""
from itertools import combinations, permutations

# 축구를 하기 위해 모인 사람 수 (n)
n = int(input())
# 능력치 정보 배열 입력받기
array = [list(map(int, input().split())) for _ in range(n)]

people = [x for x in range(n)]

candidates = combinations(people, n//2)

answer = 1e9

for candidate in candidates:
    A = candidate
    B = list(set(people) - set(candidate))

    comb_A = permutations(A, 2)
    ability_A = 0
    for comb in comb_A:
        ability_A += array[comb[0]][comb[1]]

    comb_B = permutations(B, 2)
    ability_B = 0
    for comb in comb_B:
        ability_B += array[comb[0]][comb[1]]


    diff = abs(ability_A - ability_B)

    answer = min(diff, answer)

print(answer)