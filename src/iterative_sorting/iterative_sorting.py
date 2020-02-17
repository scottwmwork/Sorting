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
def count_sort( arr, maximum=-1 ):

    # Create array 
    count = []
    for _ in range(0, maximum):
        count.append(0)

    # Count occurences and add in new array
    for num in arr:
        count[num] = count[num] + 1

    # Add array elements
    for index in range(0,len(count) - 1):
        count[index + 1] = count[index] + count[index + 1]

    # Create new array with same length as original array
    sorted = []
    for _ in range(len(arr)):
        sorted.append(0)

    for num in arr:
        
        sorted[count[num]] = num
        count[num] = count[num] - 1

    return arr

# lis = [1,4,1,2,7,5,2]
# print("Before count sort:", list(lis))
# print("After count sort:", list(count_sort(lis, 9)))