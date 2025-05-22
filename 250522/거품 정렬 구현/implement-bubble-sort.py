n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

do {
    sorted = True
    for i in range(n-1):
        if(arr[i] > arr[i+1]):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            sorted = False
}while sorted == False

for i in arr
print(i,end = ' ')