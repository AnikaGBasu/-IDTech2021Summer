import random


def binarySearch(array, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch(array, low, mid - 1, x)
        else:
            return binarySearch(array, mid + 1, high, x)
    else:
        return -1


def main():
    array = []
    for i in range(0, 1001):
        i = random.randint(0, 2000)
        if i in array:
            pass
        else:
            array.append(i)
    array.sort()

    result = binarySearch(array, 0, len(array) - 1, random.randint(0, 2000))
    if result != -1:
        print("The number is at the index ", str(result))
    else:
        print("The number is not present in the given array.")


main()