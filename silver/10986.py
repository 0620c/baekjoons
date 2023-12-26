n,m = map(int,input().split())
arr = list(map(int,input().split()))

result = 0
for i in range(n):
    for j in range(n):
        if sum(arr[i:j]) == 0:
            result += 1
            
