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

# make array of size 100 

bubble_array = []
 
for num in range(100):
        bubble_array.append(random.randint(1, 1000000))
        
print(bubble_array)
print("Bubble sort")
    
print("    Sorted: ", bubble_sort(bubble_array)
bubble_sorted = bubble_array.sort()
bubble_sort(bubble_sorted)
bubble_sorted_reverse = sort.bubble_array(reverse = True)
    
merge_array = numpy.copy(bubble_array)
merge_sorted = sort.merge_array()
merge_sorted_reverse = sort.merge_array(reverse = True)
    
quick_array = numpy.copy(bubble_array)
quick_sorted = sort.quick_array()
quick_sorted_reverse= sort.quick_array(reverse = True)
    
extra_array = numpy.copy(bubble_array)
extra_sorted = sort.extra_array()
extra_sorted_reverse = sort.extra_array(reverse = True)

# make array of size 1000
