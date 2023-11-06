# 선택정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)): # 리스트 내 모든 원소의 인덱스를 처음부터 순차적으로 순회
    min_index = i   # 가장 작은 원소의 인덱스를 앞에서부터 순차적으로 설정
    print(f"i={i}")
    for j in range(i+1, len(array)): # i 이후의 요소중에 작은걸 찾기 위함
        if array[min_index] > array[j]:
            min_index = j
            print(f"j={j}")
    array[i], array[min_index] = array[min_index], array[i]

    print(f"현재까지의 array: {array}")

print(i)