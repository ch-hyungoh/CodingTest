def dfs(Narr, b, k, N):
    if b == 6:
        return
    if b == N:
        # 현재 배열을 정수로 변환하여 arrList에 추가
        result = int(''.join(map(str, Narr)))
        arrList.append(result)
        return
    
    # k 위치부터 N 위치까지 스왑을 시도
    for i in range(k, len(Narr)):
        # 스왑
        Narr[k], Narr[i] = Narr[i], Narr[k]
        # 다음 재귀 호출
        dfs(Narr, b+1, k + 1, N)
        # 스왑 복원 (백트래킹)
        Narr[k], Narr[i] = Narr[i], Narr[k]

for tc in range(1, 1 + int(input())):
    arrList = []
    arr = list(map(int, input().split()))

    N = arr[1] 
    Numarr = [int(char) for char in str(arr[0])]

    dfs(Numarr, 0, 0, N)

    # 결과 리스트가 비어있지 않은지 확인 후 최대값 출력
    if arrList:
        print(f"#{tc} {max(arrList)}")