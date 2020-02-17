# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_inde = i
        smallest_inde = cur_inde
        # TO-DO: find net smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_inde, len(arr)):
            if arr[smallest_inde] > arr[j]:
                 smallest_inde = j

        # TO-DO: swap   
        arr[i], arr[smallest_inde] = arr[smallest_inde], arr[i]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for j in range(0,len(arr)):
        for i in range(0, len(arr) - j - 1):
            if arr[i] > arr[i + 1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maimum=-1 ):

    return arr

lis = [9,2,4,5,1]
print("Before sorted:", list(lis))
print("After sored:", list(selection_sort(lis)))