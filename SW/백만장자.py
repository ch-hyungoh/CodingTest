for tc in range(1, 1+int(input())):
    N = int(input())

    arr = list(map(int, input().split()))
    
    sum_Num = 0
    max_Num = arr[N-1]
    for i in range(N-1, -1, -1):
        if arr[i] > max_Num:
            max_Num = arr[i]
        else:
            sum_Num += max_Num - arr[i] 
    
    print("#{} {}".format(tc, sum_Num))