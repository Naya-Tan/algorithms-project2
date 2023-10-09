import random
from numpy import*
import numpy 
import time

#Source: https://www.mybluelinux.com/top-5-sorting-algorithms-with-python-code/
# bubble sort 
def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                    
    return arr

#Merge sort
#Source: https://www.geeksforgeeks.org/python-program-for-merge-sort/
def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def merge_sort(arr, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		merge_sort(arr, l, m)
		merge_sort(arr, m+1, r)
		merge(arr, l, m, r)


#Source: https://www.mybluelinux.com/top-5-sorting-algorithms-with-python-code/
# quick sort 
def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, begin, end)

#Source: https://www.geeksforgeeks.org/python-program-for-shellsort/
# sort of our choice 
def shell_sort(arr, n):
 
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
   interval = n // 2
   while interval > 0:
       for i in range(interval, n):
           temp = arr[i]
           j = i
           while j >= interval and arr[j - interval] > temp:
               arr[j] = arr[j - interval]
               j -= interval

           arr[j] = temp
       interval //= 2

# make sure we test the same arrays to compare each algorithm 
# make an array and make copies of it 
    # test random generated array
    # test sorted array 
    # test reverse sorted array 
    
    # test different size arrays 
    # n = 100
    # n = 1000
    # n = 10,000
    # n = 100,000
    
    
################## make array of size 100 ##################

size = [100, 1000, 10000, 100000, 1000000]

for n in size:
    bubble_array1 = []
    for num in range(n):
        bubble_array1.append(random.randint(1, 100)) 
        
    # make copies for the other sorts 
    merge_array1 = numpy.copy(bubble_array1)
    quick_array1 = numpy.copy(bubble_array1)
    shell_array1 = numpy.copy(bubble_array1)
    
    if n < 100000:
        # bubble sort size n 
        print('\nBubble Sort - size ', n)
        print("Unsorted: ", bubble_array1[0:10])
        start_time = time.time() #Get time at start of sort
        bubble_sort(bubble_array1)
        end_time = time.time() #Get time at end of sort
        time_elapsed = end_time - start_time #Calculate time elapsed
        print('Test Unsorted: ', bubble_array1[0:10])
        print('Time elapsed: ', time_elapsed)
        
        bubble_array1.sort()
        bubble_sorted1 = bubble_array1
        print('Sorted: ', bubble_sorted1[0:10])
        start_time = time.time() #Get time at start of sort
        bubble_sort(bubble_sorted1)
        end_time = time.time() #Get time at end of sort
        time_elapsed = end_time - start_time #Calculate time elapsed
        print('Test Sorted: ', bubble_sorted1[0:10])
        print('Time elapsed: ', time_elapsed)
        
        bubble_sorted_reverse1 = bubble_array1[::-1]
        print('Reverse sorted: ', bubble_sorted_reverse1[0:10])
        start_time = time.time() #Get time at start of sort
        bubble_sort(bubble_sorted_reverse1)
        end_time = time.time() #Get time at end of sort
        time_elapsed = end_time - start_time #Calculate time elapsed
        print('Test Reverse sorted: ', bubble_sorted_reverse1[0:10])
        print('Time elapsed: ', time_elapsed)
    
    # merge sort size n
    print('\nMerge Sort - size ', n)
    print("Unsorted: ", merge_array1[0:10])
    start_time = time.time() #Get time at start of sort
    merge_sort(merge_array1, 0, n-1)
    end_time = time.time() #Get time at end of sort
    time_elapsed = end_time - start_time #Calculate time elapsed
    print('Test Unsorted: ', merge_array1[0:10])
    print('Time elapsed: ', time_elapsed)
    
    merge_array1.sort()
    merge_sorted1 = merge_array1
    print('Sorted: ', merge_array1[0:10])
    start_time = time.time() #Get time at start of sort
    merge_sort(merge_sorted1, 0, n-1)
    end_time = time.time() #Get time at end of sort
    time_elapsed = end_time - start_time #Calculate time elapsed
    print('Test Sorted: ', merge_sorted1[0:10])
    print('Time elapsed: ', time_elapsed)
    
    merge_sorted_reverse1 = merge_array1[::-1]
    print('Reverse sorted: ', merge_sorted_reverse1[0:10])
    start_time = time.time() #Get time at start of sort
    merge_sort(merge_sorted_reverse1, 0, n-1)
    end_time = time.time() #Get time at end of sort
    time_elapsed = end_time - start_time #Calculate time elapsed
    print('Test Reverse sorted: ', merge_sorted_reverse1[0:10])
    print('Time elapsed: ', time_elapsed)
    
    #Skip quick sort for 100'000 and 1'000'000
    if n < 100000:
        # quick sort size n
        print('\nQuick Sort - size ', n)
        print("Unsorted: ", quick_array1[0:10])
        start_time = time.time() #Get time at start of sort
        quick_sort(quick_array1)
        end_time = time.time() #Get time at end of sort
        time_elapsed = end_time - start_time #Calculate time elapsed
        print('Test Unsorted: ', quick_array1[0:10])
        print('Time elapsed: ', time_elapsed)
        
        
        quick_array1.sort()
        quick_sorted1 = quick_array1
        print('Sorted: ', quick_sorted1[0:10])
        start_time = time.time() #Get time at start of sort
        quick_sort(quick_sorted1)
        end_time = time.time() #Get time at end of sort
        time_elapsed = end_time - start_time #Calculate time elapsed
        print('Test sorted: ', quick_sorted1[0:10])
        print('Time elapsed: ', time_elapsed)
        
        quick_sorted_reverse1 = quick_array1[::-1]
        print('Reverse sorted: ', quick_sorted_reverse1[0:10])
        start_time = time.time() #Get time at start of sort
        quick_sort(quick_sorted_reverse1)
        end_time = time.time() #Get time at end of sort
        time_elapsed = end_time - start_time #Calculate time elapsed
        print('Test Reverse sorted: ', quick_sorted_reverse1[0:10])
        print('Time elapsed: ', time_elapsed)
    
    # extra sort size n
    print('\nShell Sort - size ', n)
    print("Unsorted: ", shell_array1[0:10])
    start_time = time.time() #Get time at start of sort
    shell_sort(shell_array1, n)
    end_time = time.time() #Get time at end of sort
    time_elapsed = end_time - start_time #Calculate time elapsed
    print("Test Unsorted: ", shell_array1[0:10])
    print('Time elapsed: ', time_elapsed)
    
    shell_array1.sort()
    shell_sorted1 = shell_array1
    print('Sorted: ', shell_sorted1[0:10])
    start_time = time.time() #Get time at start of sort
    shell_sort(shell_sorted1, n)
    end_time = time.time() #Get time at end of sort
    time_elapsed = end_time - start_time #Calculate time elapsed
    print('Test Sorted: ', shell_sorted1[0:10])
    print('Time elapsed: ', time_elapsed)
    
    shell_sorted_reverse1 = shell_array1[::-1]
    print('Reverse sorted: ', shell_sorted_reverse1[0:10])
    start_time = time.time() #Get time at start of sort
    shell_sort(shell_sorted_reverse1, n)
    end_time = time.time() #Get time at end of sort
    time_elapsed = end_time - start_time #Calculate time elapsed
    print('Test Reverse sorted: ', shell_sorted_reverse1[0:10])
    print('Time elapsed: ', time_elapsed)