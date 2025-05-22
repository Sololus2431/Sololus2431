n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
sorted = False
while sorted == False:
    sorted = True
    for j in range(n):
        for i in range(n-1):
            if(arr[i] > arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                sorted = False

for i in arr:
    print(i,end =' ')