# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    
    # TO-DO
    a = 0 # index of arrA
    b = 0 # index of arrB
    
    for i in range(0, elements):
        
        if i == len(arrA):
            print(arrA, arrB)
            merged_arr[i] = arrB[b - 1]
            print(merged_arr)
            break

        if i == len(arrB):
            print(i)
            merged_arr[i] = arrA[a - 1]
            break

        if arrA[a] <= arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
            
        else:
            merged_arr[i] = arrB[b]
            b += 1
            
    return merged_arr




# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    # Base Case 
    if len(arr) == 1 or len(arr) == 0:
        print(arr)
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

