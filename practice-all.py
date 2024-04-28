arr = [1, 2, 3, 4, 5, 5]

def removeElements(arr, num):
    k = 0

    for index in range(len(arr)):
        if arr[index] != num:
            arr[k] =  arr[index]
            k += 1

    return k
        

    