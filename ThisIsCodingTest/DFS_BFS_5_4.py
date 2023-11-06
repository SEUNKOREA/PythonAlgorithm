# 재귀함수 종료 예제
# 재귀함수를 문제풀이에 사용할 때는 재귀함수가 언제 끝날지 종료 조건을 명시해야 한다.

def recursive_function(i):
    if i == 100:
        return
    print(f"{i}번째 재귀함수에서 {i+1}번째 재귀함수를 호출합니다.")
    recursive_function(i+1)
    print(f"{i}번째 재귀함수를 종료합니다.")

recursive_function(1)