def partition(arr, low, high) -> int:
    pi_idx = low

    for i in range(low+1, high+1):
        if arr[i] <= arr[low]:
            pi_idx += 1

            #swap arr[i] & arr[pivot]
            arr[pi_idx], arr[i] = arr[i], arr[pi_idx]

    # swap the actual element at correct pivot index wiht element at current pi_idx
    arr[pi_idx], arr[low] = arr[low], arr[pi_idx]
    
    return pi_idx

def quicksort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quicksort(arr, low, pivot_idx-1)
        quicksort(arr, pivot_idx+1, high)



arr = [9, 5, 10, 12, 8, 1, 15, 13]

quicksort(arr, 0, len(arr)-1)

print(arr)

# merge sort

def mergesort(arr):

    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        # combine
        i_left, i_right, i_main = 0, 0, 0

        while i_left < len(left) and i_right < len(right):
            if left[i_left] < right[i_right]:
                arr[i_main] = left[i_left]
                i_left += 1
            else: # left[i_left] >+ right[i_right]
                arr[i_main] = right[i_right]
                i_right += 1

            i_main += 1

        while i_left < len(left):
            arr[i_main] = left[i_left]
            i_left += 1
            i_main += 1

        while i_right < len(right):
            arr[i_main] = right[i_right]
            i_right += 1
            i_main += 1

arr2 = [9, 5, 10, 12, 8, 1, 15, 13]
mergesort(arr2)

print(arr2)



