# 퀵 정렬 소스코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # end는 (배열의 길이-1) 즉, 배열의 가장 마지막 원소의 인덱스가 들어오는데 
                     # start가 end보다 크거나 같으면 원소개 1개인 경우
        return       # 종료
    pivot = start    # 피벗은 첫번째 원소    
    left = start + 1 # 첫번째 원소의 바로 다음 원소부터 시작
    right = end      # right에는 end를 넣는다
    while left <= right: # right와 left가 뒤바뀌지 않는동안 반복
        # 피벗보다 큰 데이터를 찾을 때까지
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[right], array[left] = array[right], array[left]
        
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)

