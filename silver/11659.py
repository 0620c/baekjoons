n,m = map(int,input().split())
arr = list(map(int,input().split()))

for i in range(len(m)):
    a,b = map(int,input().split())
    print(sum(arr[a-1:b]))
    
