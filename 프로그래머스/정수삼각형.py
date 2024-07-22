def solution(triangle):
    for i in range(len(triangle)-1, -1, -1):
        for j in range(i):
            if triangle[i][j] > triangle[i][j+1]:
                triangle[i-1][j] = triangle[i-1][j] + triangle[i][j]
            else:
                triangle[i-1][j] = triangle[i-1][j] + triangle[i][j+1]
    return triangle[0][0]

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
