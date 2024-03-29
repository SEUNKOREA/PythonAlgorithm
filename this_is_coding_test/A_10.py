def turn_left(matrix):
    n = len(matrix)
    m = len(matrix[0])

    after = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            after[j][n-i-1] = matrix[i][j]
    return after    

def check_valid(result):
    length = len(result) // 3
    for i in range(length, length*2):
        for j in range(length, length*2):
            if result[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)

    # 자물쇠 확장
    aug_lock = [[0]*(3*n) for _ in range((3*n))]
    for i in range(n):
        for j in range(n):
            aug_lock[i+n][j+n] = lock[i][j]
    
    # 90도씩 회전시킨 모든 키에 대해서 한칸씩 이동시켜서 들어맞는지 확인
    for _ in range(4):
        key = turn_left(key)

        for x in range(2*n):
            for y in range(2*n):

                for i in range(m):
                    for j in range(m):
                        aug_lock[x+i][y+j] += key[i][j]
                
                if check_valid(aug_lock):
                    return True

                for i in range(m):
                    for j in range(m):
                        aug_lock[x+i][y+j] -= key[i][j]
    return False
