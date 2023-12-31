from collections import deque

# 큐(Queue)구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5) # 5
queue.append(2) # 5 2
queue.append(3) # 5 2 3
queue.append(7) # 5 2 3 7
queue.popleft() # 2 3 7
queue.append(1) # 2 3 7 1
queue.append(4) # 2 3 7 1 4
queue.popleft() # 3 7 1 4

print(queue)    # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력

