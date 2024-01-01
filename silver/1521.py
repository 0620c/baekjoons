a = input()

arr = a.split('-')
val = 0
for j in list(map(int,arr[0].split('+'))):
    val += j
    
result = val
for i in arr[1:]:
    val = 0
    for j in list(map(int,i.split('+'))):
        val += j
    result -= val
print(result)

    
        
    

