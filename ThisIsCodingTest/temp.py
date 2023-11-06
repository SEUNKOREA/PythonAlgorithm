### 회전할 방향(좌, 우)과 현재 바라보고 있는 방향(동,서,남,북) 인덱스를 받아서
### 회전할 방향에 따라서 다음에 바라보고 있는 방향의 인덱스를 반환하는 함수
### 해당 방향전환 함수는 dx, dy가 동,남,서,북 순서라고 가정했을 때 만족하는 함수이다.
def turn(d_idx, turn_dir):
    if turn_dir == "R":
        d_idx = (d_idx + 1) % 4
    elif turn_dir == "L":
        d_idx = (d_idx - 1) % 4
    return d_idx





