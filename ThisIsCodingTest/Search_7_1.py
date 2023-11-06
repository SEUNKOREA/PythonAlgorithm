# 순차 탐색 소스코드
def sequential_search(n, target, array):
    # array 안의 모든 원소를 하나씩 순회하면서
    for i in range(n):
        if array[i] == target: # 타겟과 일치하는 데이터가 있다면
            return i+1 # 해당 데이터의 위치 반환(인덱스는 0부터 시작하기때문에 1을 더해서 반환한다.)

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 저근 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차탐색 수행결과 출력
print(sequential_search(n, target, array))