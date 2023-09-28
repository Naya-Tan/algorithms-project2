# project 2: analyzing and verifying asymptotic time complexity of sorting algorithms 

import random
from numpy import*
import numpy 
import time

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

# merge sort 
def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged

# quick sort 
def partition(array, begin, end):
    pivot_idx = begin
    for i in xrange(begin+1, end+1):
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

# sort of our choice 

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
    
    
def random_array(size, range):
    temp = []
    for num in range(size):
        temp.append(random.randrange(1, range))
        

# make array of size 100 
bubble_array1 = []
for num in range(100):
    bubble_array1.append(random.randint(1, 1000)) # random numbers 1 - 1000
    
print(bubble_array1)
###############################
bubble_array1.sort()
bubble_sorted1 = bubble_array1
print('sorted array', bubble_sorted1)
bubble_sorted_reverse1 = bubble_array1[::-1]
print('reverse sorted array', bubble_sorted_reverse1)
#####################################

merge_array1 = numpy.copy(bubble_array1)
merge_sorted1 = numpy.sort(bubble_array1)
#merge_sorted_reverse1 = merge_array1.sort(reverse = True)

quick_array1 = numpy.copy(bubble_array1)
quick_sorted1 = quick_array1.sort()
#quick_sorted_reverse1 = quick_array1.sort(reverse = True)

extra_array1 = numpy.copy(bubble_array1)
extra_sorted1 = extra_array1.sort()
#extra_sorted_reverse1 = extra_array1.sort(reverse = True)

