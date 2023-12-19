import sys

n = int(sys.stdin.readline())
current = list(map(int, list(sys.stdin.readline().rstrip())))
goal = list(map(int, list(sys.stdin.readline().rstrip())))

def reverse(idx, array):
    if array[idx] == 0:
        array[idx] = 1
    else:
        array[idx] = 0

def process(array, cnt):
    for i in range(1, n-1):
        if array[i-1] != goal[i-1]:
            cnt += 1
            for j in range(i-1, i+2):
                reverse(j, array)
    if array[n-1] != goal[n-1]:
        cnt += 1
        for j in range(n-2, n):
            reverse(j, array)
    
    if array == goal:
        return cnt
    else:
        return -1


# 0번째 스위치를 누른 상태
backup = current[:]
reverse(0, backup)
reverse(1, backup)
res1 = process(backup, 1)

# 0번째 스위치를 누르지 않은 상태
res2 = process(current, 0)

# 최종정답
if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1 < 0 and res2 >= 0:
    print(res2)
elif res1 >= 0 and res2 < 0:
    print(res1)
else:
    print(-1)