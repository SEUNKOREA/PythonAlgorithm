"""
SWEA 6485. 삼성시의 버스노선
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWczm7QaACgDFAWn
"""
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    answer = [0] * 5001
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            answer[i] += 1
    p = int(input())
    ans = []
    for _ in range(p):
        idx = int(input())
        ans.append(answer[idx])

    print(f"#{tc}", *ans)