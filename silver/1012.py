C = int(input())

global n
global m  

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def isInrange(x, y):
    return 0 <= x < n and 0 <= y < m         
                
def dfs(arr,x,y):
    arr[x][y] = 0
    for (dx, dy) in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if isInrange(nx, ny):
            if arr[nx][ny] == 1:
                dfs(nx, ny)

for i in range(C):
    n,m,k =  map(int,input().split())
    arr = [[0 for col in range(m)] for row in range(n)]
    for j in range(k):
        X,Y = map(int,input().split())
        arr[X][Y] = 1
    count = 0
    for x in range(m):
        for y in range(n):
            if arr[x][y] == 1:
                arr = dfs(arr,x,y)
                count += 1
    print(count)
    
                
                    