### 백만 장자 프로젝트

# import sys
# sys.stdin = open("input.txt", 'r')
# sys.stdout = open("output.txt", "w")

def main():
    T = int(input())
    for tc in range(1, T+1):
        n = int(input())
        array = list(map(int, input().split()))

        max_price = 0
        answer = 0
        for i in range(n-1,-1, -1):
            if array[i] >= max_price:
                max_price = array[i]
            else:
                answer += max_price - array[i]

        print(f"#{tc} {answer}")

if __name__ == "__main__":
    main()
