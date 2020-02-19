# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):

    a = 0
    b = 0
    merged_arr = []
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    merged_arr += arrA[a:]
    merged_arr += arrB[b:]
    return merged_arr




# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    # Base Case 
    if len(arr) == 1 or len(arr) == 0:
        return arr

    # Split
    middle = len(arr)//2
    A = merge_sort(arr[0:middle])
    B = merge_sort(arr[middle:])
                
    return merge(A, B)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


merge_sort([3,1,5,2,6,9,7])

