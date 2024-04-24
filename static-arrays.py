# Static Array operations: Accessing (Reading), Insertion, traversing, deletion

arr = [1, 3, 4, 5]


# **** Traversing an array O(n) **** #

def traverseArr(arr):
    for index in arr:
        print(index)

# traverseArr(arr)

# **** Reading a value in an array O(1) **** #

def readValueInArr(arr, index):
    print(arr[index])

# readValueInArr(arr, 2)

# **** Delete from end -> O(1) **** #

def deleteEnd(arr):
    arr[len(arr) - 1] = 0
    return print(arr)

# deleteEnd(arr)

# **** Delete from middle or beginning -> O(n) **** #


def deleteFromMiddle(arr, i, length):
    
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]

    arr[length - 1] = None

    return print(arr)

# deleteFromMiddle(arr, 0, 4)

# **** Insert at end  -> O(1) **** #

def insertAtEnd(arr, value, length):
    arr[length - 1] = value

    return print(arr);


# insertAtEnd(arr, 100, 4)

# **** Insert at middle  -> O(n) **** #
def insertInMiddle(arr, i, value, length):
    for index in range(length - 1, i - 1,  -1):
        arr[index + 1] = arr[index]

    arr[i] = value

    return print(arr)


# insertInMiddle(arr, 1, 99, 4)


