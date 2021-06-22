import random


def search(array, x):
    for i in range(0, len(array)):
        if (array[i] == x):
            return i
    return -1


def main():
    # array = int(input("Enter a series of numbers: "))
    array = []
    for i in range(0, 1001):
        i = array.append(random.randint(0, 2000))
        if i in array:
            pass

    # print(array)
    # print()
    result = search(array, 7)
    print("Your number was found at index " + str(result) + ".")


main()
