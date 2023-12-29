import sys

input = sys.stdin.readline

name = input().strip()
n = int(input())

for i in range(n):
    arr = input().split()
    score = 0
    for j in range(int(arr[1]),int(arr[2]) + 1):
        if name[j] == arr[0]:

            score += 1
    print(score)