n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(1, len(arr)-1):
    j = i-1
    key = arr[i]
    while j >=0  and arr[j] > key:
        arr[j+1] =arr[j]
        j-=1
        arr[j+1] = key

for i in arr:
    print(i, end = " ")