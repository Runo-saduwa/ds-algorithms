

# def removeElement(arr, num):
#      k = 0

#      for i in range(len(arr)):
#           if arr[i] != num:
#                arr[k] = arr[i]
#                k += 1
#      return k

#   out of place solution
def removeElementOutOfPlace(arr, val):
    newArr = []

    for index in range(len(arr)):
        if(arr[index] != val):
            newArr.append(arr[index])

    return print(newArr, len(newArr))

  


removeElementOutOfPlace([1,3, 2,3,4,5,6,7,8], 3)


def removeElementInPlace(arr, val):
    k = 0

    for index in range(len(arr)): 
        if arr[index] != val:
            arr[k] = arr[index]
            k += 1
    return print(k)


# removeElementInPlace([1,3, 2,3,4,5,6,7,8], 3)


def removeElement2(arr, val):

    l = 0

    for index in range(len(arr)):
        if arr[index] != val:
            arr[l] = arr[index]
            k +=1



def removeElements(arr, val):
    k = 0
    for index in range(len(arr)):
        if arr[index] != val:
            arr[k] = arr[index]
            k += 1



def removeElement2(arr, num):

    k = 0

    for index in range(len(arr)):
        if arr[index] != num:
            arr[k] = arr[index]
            k  += 1

    return k


def removeElement3(arr, n):
    k = 0
    for index in range(len(arr)):
        if arr[index] != n:
            arr[k] = arr[index]
            k += 1

    return k



def removeElementX(arr, val):
    k = 0

    for index in range(len(arr)):
        if arr[index] == val:
            arr[k] = arr[index]
            k += 1
    
    return k


