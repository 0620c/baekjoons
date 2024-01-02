T = int(input())

def R(arr):
    arr_reverse = []
    arr_len = len(arr)
    for i in range(arr_len):
        arr_reverse.append(arr[arr_len-i-1])
    return arr_reverse

def D(arr):
    arr_del = []
    for i in range(1,len(arr)):
        arr_del.append(arr[i])
    return arr_del

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
            arr = R(arr)
        else:
            if len(arr) == 0:
                print('error')
                flag = 1
                break
            else:
                arr = D(arr)
    
    if flag == 0:
        print(arr)