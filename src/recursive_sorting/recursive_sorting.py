# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    if arrA[0] > arrB[0]:
        merged_arr = arrB + arrA
    if arrA[0] < arrB[0]:
        merged_arr = arrA + arrB
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    # Base Case TODO
    if len(arr) == 1:
        return arr

    
    middle = int(len(arr)/2)
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

