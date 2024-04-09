"""
SWEA 1945. 간단한 소인수분해
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pl0Q6ANQDFAUq
"""


import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [11, 7, 5, 3, 2]
    ans = [0, 0, 0, 0, 0]

    for i in range(5):
        div_n = arr[i]
        while True:
            if n % div_n != 0:
                break
            n //= div_n
            ans[i] += 1

    print(f"#{tc}", end=' ')
    for i in range(5):
        print(ans[::-1][i], end=' ')
    print()

