for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0
    for i in range(2, N-2):
        ff, f, c, n, nn = arr[i-2], arr[i-1] , arr[i] ,arr[i+1] , arr[i+2]
        if ff < c and f < c and n < c and nn < c:
            result += c - max(ff, f, n, nn)


    print(result)