import sys

N = int(input())
sys.setrecursionlimit(10**6)
arr = []
for i in range(N):
    arr.append(list(input()))

arr_2 = [[0 for col in range(N)] for row in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr_2[i][j] = "G"
        else:
            arr_2[i][j] = arr[i][j]

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def isInrange(x, y):
    return 0 <= x < N and 0 <= y < N  

def dfs(x, y, color):
    arr[x][y] = 0
    for (dx,dy) in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if isInrange(nx, ny):
            if arr[nx][ny] == color:
                dfs(nx, ny,color)
                
def dfs_2(x, y, color):
    arr_2[x][y] = 0
    for (dx,dy) in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if isInrange(nx, ny):
            if arr_2[nx][ny] == color:
                dfs_2(nx, ny,color)
count = 0
count_2 = 0
for x in range(N):
    for y in range(N):
        if arr[x][y] != 0:
            count += 1
            dfs(x,y,arr[x][y])
        if arr_2[x][y] != 0:
            count_2 += 1
            dfs_2(x,y,arr_2[x][y])

            
print(count, count_2)