def recursive_function(i):
    if i == 100:
        return
    print(f"{i}번째 재귀함수에서 {i+1}번째 재귀함수를 호출합니다.")
    recursive_function(i+1)

recursive_function(0)