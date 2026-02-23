import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
q = deque()

def can_visit(x, y):
    return  0 <= x < n and \
            0 <= y < m and \
            not visited[x][y] and \
            grid[x][y] != 0

def push(x, y):
    visited[x][y] = True
    q.append((x, y))

def bfs(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_visit(nx, ny):
                push(nx, ny)
        
push(0, 0)
bfs(0, 0)

if visited[n-1][m-1]:
    print(1)
else:
    print(0)