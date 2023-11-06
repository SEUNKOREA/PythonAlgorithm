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
def check(arr):
    n = len(arr)//3
    for row in arr[n:2*n]:
        for r in row[n:2*n]:
            if r != 1:
                return False
    return True

def solution(key, lock):
    m = len(key) # 3
    n = len(lock) # 3

    ### 자물쇠 확장
    new_lock = [[0]*(3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] += lock[i][j]
    
    ### 90, 180, 270, 360 회전한 키에 대해서 슬라이딩 하면서 확인
    for _ in range(4):
        key = rotate_key(key)
        
        for x in range(2*n+1):
            for y in range(2*n+1):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                
                if check(new_lock) == True:
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False

 
if __name__ == "__main__":
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    solution(key, lock)