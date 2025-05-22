n = int(input())
arr = list(map(int, input().split()))

# 짜잔! 여기가 수정된 부분이야!
for i in range(len(arr) - 1):
    min_idx = i # 정렬되지 않은 부분의 시작점을 일단 최소값으로 찜해두고!
    for j in range(i + 1, len(arr)): # 시작점 다음부터 끝까지 보면서
        if arr[min_idx] > arr[j]: # 만약 더 작은 값을 발견하면
            min_idx = j # 그 작은 값의 위치를 기억해두자!
    
    # 안쪽 반복문이 끝나면 min_idx에는 제일 작은 값의 위치가 저장되어 있을 거야
    # 이제 정렬되지 않은 부분의 시작점(i)에 있는 값이랑
    # 찾은 제일 작은 값(min_idx에 있는 값)을 바꿔주자!
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

for i in arr:
    print(i, end=" ")