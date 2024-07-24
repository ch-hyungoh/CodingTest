# 파이썬은 최소힙 밖에 존재 하지 않음
import heapq

def solution(n, works):
    anwser = 0
    heap = []

    for work in works:
        #최대 힙을 구현하기 위해서 음수를 push해줘서 최대힙을 만들어준다
        heapq.heappush(heap, (-work, work))

    while True:
        if n == 0:
            break
        #최대 힙을 꺼내서 1 감소 시켜주고 다시 넣어준다
        work = heapq.heappop(heap)[1]-1
        heapq.heappush(heap, (-work, work))
        n -= 1

    for h in heap:
        if h[1] < 0:
            continue
        anwser += h[1] ** 2

    return anwser
