def solution(operations):
    answer = []

    for i in range(len(operations)):
        if operations[i][0] == 'I':
            answer.append(int(operations[i][2:]))  # 'I' 뒤의 숫자를 큐에 삽입
        if operations[i][0] == 'D':
            if len(answer) == 0:
                pass  # 큐가 비어 있으면 아무것도 하지 않음
            else:
                if operations[i][2] == '-':
                    answer.remove(min(answer))  # 'D -1'이면 최솟값 제거
                else:
                    answer.remove(max(answer))  # 'D 1'이면 최댓값 제거

    if answer == []:
        answer.append(0)  # 큐가 비어 있으면 0을 삽입
    result = [max(answer), min(answer)]  # 최댓값과 최솟값 반환
    return result

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))