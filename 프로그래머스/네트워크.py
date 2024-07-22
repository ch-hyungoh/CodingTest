def dfs(x, computers, visited):
    n = len(visited)
    for i in range(n):
        if x != i:
            if computers[x][i] == 1 and not visited[i]:
                visited[i] = 1
                dfs(i, computers, visited)


def solution(n, computers):
    answer = 0
    visited = [0]*n

    for i in range(n):
        if visited[i] == 0:
            visited[0] = 1
            dfs(i, computers, visited)
            answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))