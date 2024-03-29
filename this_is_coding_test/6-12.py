n, k = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

# 배열 a는 오름차순
arr_a.sort()
# 배열 b는 내림차순
arr_b.sort(reverse=True)

for i in range(k):
    if arr_a[i] < arr_b[i]:
        arr_a[i], arr_b[i] = arr_b[i], arr_a[i]
    else:
        break

print(sum(arr_a))