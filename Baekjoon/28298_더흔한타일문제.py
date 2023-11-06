import sys

n, m, k = map(int, sys.stdin.readline().split()) # 4, 6, 2
tile = [sys.stdin.readline().rstrip() for _ in range(n)]
# # ['ABCBAB', 'BBACCA', 'BPAZBB', 'BBAABB']

answer_tile = [[0] * m for _ in range(n)]
# """
# [[0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0]]
# """
answer = 0
from collections import defaultdict
for i in range(k): # 0,1,2
    for j in range(k): # 0,1,2
        cnt_dict = defaultdict(int)
        for a in range(n//k): #2 (0,1)
            for b in range(m//k): #3 (0,1,2)
                current = tile[a*k+i][b*k+j]
                cnt_dict[current] += 1
        key, value = sorted(cnt_dict.items(), key=lambda x:x[1], reverse=True)[0]
        answer += (n//k) * (m//k) - value
        for a in range(n//k):
            for b in range(m//k):
                answer_tile[a*k+i][b*k+j] = key


print(answer)
for row in answer_tile:
    print(''.join(row))

