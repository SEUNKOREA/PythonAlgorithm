### SWEA 2072 홀수만더하기

import sys

def process():
    sys.stdin = open("input.txt", 'r')
    sys.stdout = open("output.txt", "w")

    tc = int(sys.stdin.readline().strip())
    for i in range(1, tc+1):
        array = list(map(int, input().split()))
        result = 0
        for num in array:
            if num % 2 == 1:
                result += num

        print(f"#{i} {result}")

if __name__ == "__main__":
    process()

