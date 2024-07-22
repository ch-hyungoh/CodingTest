for tc in range(1, 1+int(input())):
    arr = list(map(int, input().split()))

    a = arr[0]
    b = arr[1]

    if a+b >= 24:
        c = a+b-24
    else:
        c = a+b
    print("#{} {}".format(tc, c))