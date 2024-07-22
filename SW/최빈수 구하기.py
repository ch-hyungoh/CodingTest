for tc in range(1, 1+int(input())):
    N = int(input())

    arr = list(map(int, input().split()))

    ST_diction = {i : 0 for i in range(101)}

    for k in range(1000):
        ST_diction[arr[k]] += 1

    max_value = max(ST_diction.values())

    max_key = [key for key, value in ST_diction.items() if value == max_value]

    print("#{} {}".format(tc, max_key[-1]))