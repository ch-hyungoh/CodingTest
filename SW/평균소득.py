for tc in range(1, 1+int(input())):
    N = int(input())

    arr = list(map(int, input().split()))

    result = 0
    sum = 0
    for k in arr:
        sum += k
    
    avg = sum / N

    for j in arr:
        if j <= avg:
            result += 1

    print("#{} {}".format(tc, result))