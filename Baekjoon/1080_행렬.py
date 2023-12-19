import sys

n, m = map(int, sys.stdin.readline().split())
listA = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
listB = [list(map(int, list(sys.stdin.readline().rstrip())))for _ in range(n)]

def print_status():
    for a,b in zip(listA, listB):
        print(a, b)
    print()

def process():
    print("Start")
    print_status()
    
    # 행렬의 크기가 3*3보다 작은 경우 -> 두 행렬이 다르면 0->1, 1->0 연산으로 바꿀 수 없다.
    if (n < 3 or m < 3) and (listA != listB):
        print(-1)
        return 
    
    # 애초에 같은 행렬이 주어진 경우
    cnt = 0
    if listA == listB:
        print(cnt)
        return
    
    # 해당 위치에서 값 확인 후 다르면 해당 위치로부터 3간격의 값을 모두 바꿈
    for i in range(n-2):
        for j in range(m-2):
            if listA[i][j] != listB[i][j]:
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if listA[r][c] == 0:
                            listA[r][c] = 1
                        else:
                            listA[r][c] = 0
                cnt += 1
                print(f"현재 cnt: {cnt}")
                print_status()
    
    if listA != listB:
        print(-1)
    else:
        print(cnt)

process()