n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

def possible(answer):
    for x, y, stuff in answer:
        ## 기둥조건
        if stuff == 0:
            # 바닥 위에 있거나, 보의 한쪽 끝부분 위에 있거나, 다른 기둥 위에 있거나
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        ## 보 조건
        elif stuff == 1:
            # 한쪽 끝부분이 기둥 위에 있거나, 양쪽 끝부분이 다른 보와 동시에 연결되어 있거나, 바닥에 놓이지 않는다.
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []

    for x, y, struct, install in build_frame:
        ## 설치하는 경우
        if install == 1:
            answer.append([x, y, struct]) # 일단 설치해본다.
            # 설치가 가능한지 체크
            if possible(answer):
                continue
            else:
                answer.remove([x, y, struct])

        ## 삭제하는 경우
        elif install == 0:
            answer.remove([x, y, struct]) # 일단 삭제해본다.
            # 삭제가 가능한지 체크
            if possible(answer):
                continue
            else:
                answer.append([x, y, struct])

    return sorted(answer)

"""
### 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        # 설치된 것이 기둥인 경우
        if stuff == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        # 설치된 것이 보인 경우
        elif stuff == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []

    for frame in build_frame: # frame의 개수는 최대 1,000개
        x, y, stuff, operate = frame

        ### 삭제하는 경우
        if operate == 0:
            # 일단 삭제를 해본 뒤에
            answer.remove([x, y, stuff])
            # 가능한 구조물인지 확인
            # 가능한 구조물이 아니라면 다시 설치
            if not possible(answer):
                answer.append([x, y, stuff]) 
        
        ### 설치하는 경우
        if operate == 1:
            # 일단 설치를 해본 뒤에
            answer.append([x, y, stuff])
            # 가능한 구조물인지 확인
            # 가능한 구조물이 아니라면 다시 제거
            if not possible(answer):
                answer.remove([x, y, stuff])
    
    return sorted(answer)
"""