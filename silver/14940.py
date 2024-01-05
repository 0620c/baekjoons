import sys
from collections import deque

queue = deque([])
input = sys.stdin.readline
n,m = map(int,input().split())
matrix = []

visit = [[False]*m for _ in range(n)]
distance_matrix = [[-1 for col in range(m)] for row in range(n)]

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        if row[j] == 2:
            queue.append((i,j))
            visit[i][j] = True
            distance_matrix[i][j] = 0

        if row[j] == 0:
            distance_matrix[i][j] = 0
    matrix.append(row)
    
            
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def isInrange(x, y):
    return 0 <= x < n and 0 <= y < m  

while queue:
    x, y = queue.popleft()
    
    for dx,dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy
        
        if isInrange(nx,ny) and not visit[nx][ny] and matrix[nx][ny] == 1:
            queue.append((nx, ny))
            visit[nx][ny] = True
            distance_matrix[nx][ny] = distance_matrix[x][y] + 1
        
for row in distance_matrix:
    for i in row:
        print(i, end=" ")
    print()