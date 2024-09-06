import sys


def merge_sort(arr, n):
    if n > 1:
        mid = n // 2

        # 왼쪽 절반과 오른쪽 절반을 나눔
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 각 절반의 길이
        left_len = len(left_half)
        right_len = len(right_half)

        # 재귀적으로 병합 정렬
        merge_sort(left_half, left_len)
        merge_sort(right_half, right_len)

        # 병합
        i = j = k = 0

        while i < left_len and j < right_len:
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 왼쪽 절반에 남은 요소들 추가
        while i < left_len:
            arr[k] = left_half[i]
            i += 1
            k += 1

        # 오른쪽 절반에 남은 요소들 추가
        while j < right_len:
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


input = sys.stdin.read
data = list(map(int, input().strip().split()))
length, data = data[0], data[1:]
data = merge_sort(data, length)
print("\n".join(map(str, data)))
