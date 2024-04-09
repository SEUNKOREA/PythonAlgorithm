"""
SWEA 1206. View
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh
"""
import sys
sys.stdin = open('input.txt', 'r')

def make_arr(cur, tar):
    if cur <= tar:
        return [1] * cur
    else:
        return [1]*tar + [0]*(cur-tar)

for tc in range(1, 11):
    n = int(input()) # 건물의 개수
    arr = list(map(int, input().split())) # n개의 건물의 높이
    ans = 0
    for i in range(2, n-2):
        height = arr[i]
        left_1 = make_arr(height, arr[i - 1])
        left_2 = make_arr(height, arr[i - 2])
        right_1 = make_arr(height, arr[i + 1])
        right_2 = make_arr(height, arr[i + 2])
        # print(left_1)
        # print(left_2)
        # print(right_1)
        # print(right_2)
        tmp = 0
        for j in range(height):
            left, right = True, True
            if left_1[j] == 1 or left_2[j] == 1:
                left = False
            if right_1[j] == 1 or right_2[j] == 1:
                right = False
            if left and right:
                tmp += 1
        ans += tmp
        # print(tmp)
    print(f"#{tc}", ans)

### 다른 풀이
# for tc in range(1, 11):
#     n = int(input()) # 건물의 개수
#     arr = list(map(int, input().split())) # n개의 건물의 높이
#     ans = 0
#
#     for i in range(2, n-2):
#         mx = arr[i-2]
#         for j in range(i-1, i+3):
#             if i == j: continue
#             if mx < arr[j]: mx = arr[j]
#         if mx < arr[i]:
#             ans += (arr[i] - mx)
#     print(f"#{tc} {ans}")