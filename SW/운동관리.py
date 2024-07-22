for tc in range(1, 1+int(input())):
    arr = list(map(int, input().split()))

    l = arr[0]
    u = arr[1]
    x = arr[2]

    if l <= x <= u:
        print("#{} {}".format(tc, 0))
    elif x < l:
        print("#{} {}".format(tc, l-x))
    else:
        print("#{} {}".format(tc, -1))
