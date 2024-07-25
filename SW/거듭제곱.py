def jegi(x, y, max):
    global result
    if y == 0:
        result = max
    else:
        jegi(x, y-1, max=max*x)

for tc in range(1, 11):
    N = int(input())

    x, y = map(int, input().split())

    result = 0

    jegi(x, y-1, x)

    print(f"#{N} {result}")
