n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(len(arr)-1):
    Min = i
    for j in range(i+1, len(arr)-1):
        if(arr[Min]>arr[j]):
            Min = j

    temp = arr[Min]
    arr[Min] = arr[i]
    arr[i] = temp

for i in arr:
    print(i, end=" ")