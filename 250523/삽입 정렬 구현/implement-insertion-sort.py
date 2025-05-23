n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(1, len(arr)-1):
    j = i-1
    key = arr[i]
    while j >=0  and arr[j] > key:
        arr[j+1] = arr[j]
        arr[j] = key
        j-=1

for i in arr:
    print(i, end = " ")