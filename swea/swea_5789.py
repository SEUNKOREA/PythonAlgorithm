"""
SWEA 5789. 현주의 상자 바꾸기
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWYygN36Qn8DFAVm
"""

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0] * (N+1)
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            arr[j] = i

    print(f"#{tc}", *arr[1:])