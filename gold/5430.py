T = int(input())

def trans_arr(arr):
    if arr == '[]':
        return []
    arr = arr.split(',')
    arr[0] = arr[0].replace('[','')
    arr[len(arr)-1] = arr[len(arr)-1].replace(']','')
    arr = list(map(int,arr))
    
    return arr


for i in range(T):
    flag = 0
    fun_arr = list(input())
    N = int(input())
    
    arr = input()
    arr = trans_arr(arr)
    for fun in fun_arr:
        if fun == "R":
            arr.reverse()
        else:
            if len(arr) == 0:
                print('error')
                flag = 1
                break
            else:
                arr.popleft()
    
    if flag == 0:
        print(arr)