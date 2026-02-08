import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]

def can_visit(x, y, bx, by):
    return  0 <= x < n and \
            0 <= y < n and \
            not visited[x][y] and \
            grid[x][y] == grid[bx][by]

def dfs(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    block = 1

    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_visit(nx, ny, x, y):
            visited[nx][ny] = True
            block += dfs(nx, ny)

    return block

current_block = 0
current_blast = 0
max_blast = 0
blast_count = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] != current_block and not visited[i][j]:
            current_block = grid[i][j]
            current_blast = dfs(i, j)
            max_blast = max(current_blast, max_blast)
            if current_blast >= 4:
                blast_count += 1

print(blast_count, max_blast)