def solution(key, lock):
    # 자물쇠의 크기
    n = len(lock)
    # 홈의 크기
    m = len(lock)

    # 자물쇠 3배 확장
    array = [[0] * (3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            array[i+n][j+n] = lock[i][j]

    def turn_left(array):
        n = len(array)
        m = len(array[0])

        new_array = [[0] * n for _ in range(m)]
        for i in range()

    for _ in range(4):


    return
