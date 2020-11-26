import random

def main():
    arr = list(range(0, 10))
    arrCopy = arr.copy()

    print(arr)
    shuffle(arr)
    print(arr)

    badSort(arr)
    arrCopy.sort()
    print(arr)

    assert arr == arrCopy

def badSort(arr):
    for n in range(len(arr)):
        min = n
        for i in range(n + 1, len(arr)):
            if arr[i] < arr[min]:
                min = i
        if min != n:
            t = arr[n]
            arr[n] = arr[min]
            arr[min] = t

def shuffle(arr):
    arrCopy = arr.copy()
    for n in range(len(arr)):
        r = random.randint(0, len(arrCopy) - 1)
        arr[n] = arrCopy.pop(r)

if __name__ == "__main__":
    main()