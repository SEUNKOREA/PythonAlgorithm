### 2차원 배열을 90도 회전시키는 함수
def rotate_key(key):
    h = len(key) # 2
    w = len(key[0]) # 4
    rotate_key = [[0]* h for _ in range(w)]
    for i in range(w):
        for j in range(h):
            rotate_key[i][j] += key[h-j-1][i]
    return rotate_key

### 자물쇠가 열리는지 확인하는 함수
def check(arr, m, n):
    arr = arr[m-1:m-1+n]
    for aa in arr:
        for a in aa[m-1:m-1+n]:
            if a != 1:
                return False
    return True

def solution(key, lock):
    m = len(key) # 3
    n = len(lock) # 3

    ### 자물쇠 확장
    expand_len = n+2*m-2
    new_lock = [[0] * (expand_len) for _ in range(expand_len)] # 0으초 초기화된 확장된 판에
    for i in range(n): # 자물쇠 원래 위치에 자물쇠 값 더해줌
        for j in range(n):
            new_lock[m-1+i][m-1+j] += lock[i][j]
    
    ### 90, 180, 270, 360 회전한 key값에 대해서
    for _ in range(4):
        key = rotate_key(key)
        ### 왼쪽상단에서부터 오른쪽하단까지 슬라이딩하면서
        for x in range(n+2*m-4):
            for y in range(n+2*m-4):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock, m,n) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
 
if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))