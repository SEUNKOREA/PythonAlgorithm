# 재귀함수
# 자기 자신을 다시 호출하는 함수

# 가장 간단한 재귀함수
def recursive_function():
    print('재귀함수를 호출합니다.')
    recursive_function()

recursive_function()

# 이 코드를 실행하면
# 재귀의 최대 깊이를 초과했다는 오류가 발생
# 파이썬 인터프리터는 호출 횟수 제한이 있는데 이 한계를 벗어났기 때문에 발생