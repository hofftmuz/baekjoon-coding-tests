import sys


def insertionSort(n: int, data):
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    print("\n".join(map(str, data)))


def selectionSort(n: int, data):
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if data[j] < data[minIndex]:
                minIndex = j
        if minIndex != i:
            data[i], data[minIndex] = data[minIndex], data[i]
    print("\n".join(map(str, data)))


# 버블 sort
def bubbleSort(n: int, data):
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    print("\n".join(map(str, data)))


# Quick sort
def quickSort1(n, data):
    if n <= 1:
        return data
    pivot = data[n // 2]
    leftArr, equalArr, rightArr = [], [], []
    for num in data:
        if num < pivot:
            leftArr.append(num)
        elif num > pivot:
            rightArr.append(num)
        else:
            equalArr.append(num)
    data = (
        quickSort1(len(leftArr), leftArr)
        + equalArr
        + quickSort1(len(rightArr), rightArr)
    )
    print("\n".join(map(str, data)))


def quickSort2(n: int, arr):
    def sort(low, high):
        if high <= low:
            return
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1

            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    arr = sort(0, n - 1)
    print("\n".join(map(str, arr)))


# Merge sort

# Heap sort

input = sys.stdin.read
data = list(map(int, input().strip().split()))
n = data.pop(0)

# selectionSort(n, data)
quickSort2(n, data)
