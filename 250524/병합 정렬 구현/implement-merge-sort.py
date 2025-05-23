n = int(input())
arr = list(map(int, input().split()))

def merge(arr, low, mid, high):
    left_half = arr[low : mid + 1]
    right_half = arr[mid + 1 : high + 1]

    i = 0
    j = 0
    k = low

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

merge_sort(arr, 0, n - 1)

for i in arr:
    print(i, end=" ")

