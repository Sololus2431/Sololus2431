n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.



import sys

# 재귀 깊이 제한을 늘려주는 설정 (필요에 따라 사용)
# sys.setrecursionlimit(3000)

# 올바른 swap 함수: 리스트와 교환할 두 요소의 인덱스를 받아서 리스트 내에서 직접 값을 교환합니다.
def swap(arr, idx1, idx2):
  arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

# 피벗을 선택하는 함수 (여기서는 간단하게 마지막 요소를 피벗으로 사용합니다)
# 중앙값을 사용하고 싶으시면 select_pivot 로직을 수정하여 해당 요소를 high 위치로 스왑해야 합니다.
def select_pivot(arr, low, high):
    # 간단하게 마지막 요소를 피벗으로 사용
    return arr[high]

# 파티션 함수: low부터 high까지의 부분 배열을 피벗 기준으로 나눕니다.
def partition(arr, low, high):
  # 피벗 선택 (select_pivot 함수에서 선택한 값을 사용)
  # 여기서는 select_pivot이 단순히 arr[high]를 반환한다고 가정하고 작성
  pivot_value = select_pivot(arr, low, high) # 피벗 '값'

  # 만약 select_pivot에서 특정 인덱스를 반환하고 싶다면,
  # 해당 인덱스의 요소를 high 위치로 스왑한 후 arr[high]를 피벗으로 사용할 수 있습니다.
  # 예: pivot_idx = select_pivot_index(arr, low, high)
  #     swap(arr, pivot_idx, high)
  #     pivot_value = arr[high]

  i = low - 1  # 피벗보다 작은 요소들의 끝 인덱스

  # low부터 high-1까지 반복 (high 위치에 있는 피벗 요소는 제외)
  for j in range(low, high) :
    # 현재 요소가 피벗 값보다 작으면
    if arr[j] < pivot_value:
      i += 1 # 작은 요소의 끝 인덱스를 하나 늘리고
      swap(arr, i, j) # 현재 요소와 작은 요소의 끝 위치에 있는 요소를 교환

  # 반복문이 끝나면 i + 1 위치는 피벗 값이 들어갈 자리입니다.
  # 원래 high 위치에 있던 피벗 값을 i + 1 위치로 옮깁니다.
  # Note: 현재 코드에서는 pivot_value만 사용하고 arr[high]가 항상 피벗이라고 가정했으므로
  #       이 swap은 high 위치의 피벗 요소와 i+1 위치 요소를 교환하는 역할을 합니다.
  swap(arr, i + 1, high)
  return i + 1 # 피벗의 최종 위치를 반환

# 퀵 정렬 함수
def quick_sort(arr, low, high):
    if low < high:
        # 파티션을 수행하고 피벗의 위치를 얻습니다.
        pos = partition(arr, low, high)

        # 피벗을 기준으로 왼쪽 부분과 오른쪽 부분에 대해 재귀적으로 퀵 정렬을 수행합니다.
        quick_sort(arr, low, pos - 1) # 피벗의 왼쪽 부분
        quick_sort(arr, pos + 1, high) # 피벗의 오른쪽 부분

    # 재귀 호출이 모두 끝나면 정렬된 배열이 됩니다.
    return arr

# 사용자 입력 받기

# 퀵 정렬 실행 및 결과 출력
sorted_arr = quick_sort(arr, 0, n - 1)
for i in sorted_arr:
    print(i, end = ' ')