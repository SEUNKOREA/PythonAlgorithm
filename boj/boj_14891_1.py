"""
BOJ 14891 톱니바퀴
출처: https://www.acmicpc.net/problem/14891
"""

import sys
sys.stdin = open('input.txt', 'r')

def turn(arr, dr):
    if dr == 1: # 시계방향
        return [arr[-1]] + arr[:-1]
    elif dr == -1:
        return arr[1:] + [arr[0]]


def dfs_right(start, dr):
    if start >= 4:
        return
    if arr[start][2] != arr[start+1][6]:
        dfs_right(start+1, -dr)
        arr[start+1] = turn(arr[start+1], -dr)
        # print(start+1, -dr)

def dfs_left(start, dr):
    if start <= 1:
        return
    if arr[start][6] != arr[start-1][2]:
        dfs_left(start-1, -dr)
        arr[start - 1] = turn(arr[start - 1], -dr)
        # print(start-1, -dr)

arr = [list(map(int, input())) for _ in range(4)]
arr = [[0]*8] + arr

K = int(input())
for _ in range(K):
    start, dr = map(int, input().split())
    dfs_right(start, dr)
    dfs_left(start, dr)
    arr[start] = turn(arr[start], dr)

score = 0
if arr[1][0] == 1:
    score += 1
if arr[2][0] == 1:
    score += 2
if arr[3][0] == 1:
    score += 4
if arr[4][0] == 1:
    score += 8

print(score)