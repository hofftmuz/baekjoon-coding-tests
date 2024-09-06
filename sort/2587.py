import sys


def quickSort(n: int, data):
    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = data[(low + high) // 2]
        while low <= high:
            while data[low] < pivot:
                low += 1
            while data[high] > pivot:
                high -= 1
            if low <= high:
                data[low], data[high] = data[high], data[low]
                low, high = low + 1, high - 1
            return low

    sort(0, n - 1)


input = sys.stdin.read
data = list(map(int, input().strip().split()))
quickSort(len(data), data)
print(sum(data) // len(data))
print(data[len(data) // 2])
