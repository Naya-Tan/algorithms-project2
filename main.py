# project 2: analyzing and verifying asymptotic time complexity of sorting algorithms 

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

#Source: Algorithms chapter 2 lecture note page 11
# merge sort 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    
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
bubble_array1 = []
for num in range(100):
    bubble_array1.append(random.randint(1, 1000)) 
    
# make copies for the other sorts 
merge_array1 = numpy.copy(bubble_array1)
quick_array1 = numpy.copy(bubble_array1)
shell_array1 = numpy.copy(bubble_array1)

# bubble sort size 100 
print('\nBubble Sort - size 100')
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

# merge sort size 100
print('\nMerge Sort - size 100')
print("Unsorted: ", merge_array1[0:10])
start_time = time.time() #Get time at start of sort
merge_sort(merge_array1)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Unsorted: ', merge_array1[0:10])
print('Time elapsed: ', time_elapsed)

merge_array1.sort()
merge_sorted1 = merge_array1
print('Sorted: ', merge_array1[0:10])
start_time = time.time() #Get time at start of sort
merge_sort(merge_sorted1)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Sorted: ', merge_sorted1[0:10])
print('Time elapsed: ', time_elapsed)

merge_sorted_reverse1 = merge_array1[::-1]
print('Reverse sorted: ', merge_sorted_reverse1[0:10])
start_time = time.time() #Get time at start of sort
merge_sort(merge_sorted_reverse1)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Reverse sorted: ', merge_sorted_reverse1[0:10])
print('Time elapsed: ', time_elapsed)

# quick sort size 100
print('\nQuick Sort - size 100')
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

# extra sort size 100
print('\nShell Sort - size 100')
print("Unsorted: ", shell_array1[0:10])
start_time = time.time() #Get time at start of sort
shell_sort(shell_array1, 100)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print("Test Unsorted: ", shell_array1[0:10])
print('Time elapsed: ', time_elapsed)

shell_array1.sort()
shell_sorted1 = shell_array1
print('Sorted: ', shell_sorted1[0:10])
start_time = time.time() #Get time at start of sort
shell_sort(shell_sorted1, 100)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Sorted: ', shell_sorted1[0:10])
print('Time elapsed: ', time_elapsed)

shell_sorted_reverse1 = shell_array1[::-1]
print('Reverse sorted: ', shell_sorted_reverse1[0:10])
start_time = time.time() #Get time at start of sort
shell_sort(shell_sorted_reverse1, 100)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Reverse sorted: ', shell_sorted_reverse1[0:10])
print('Time elapsed: ', time_elapsed)

#############################################################

print('\n-----------------------------------------------------------------------------------------')

################## make array of size 1,000 ##################
bubble_array2 = []
for num in range(1000):
    bubble_array2.append(random.randint(1, 10000)) 
    
# make copies for the other sorts 
merge_array2 = numpy.copy(bubble_array2)
quick_array2 = numpy.copy(bubble_array2)
shell_array2 = numpy.copy(bubble_array2)

# bubble sort size 1,000
print('Bubble Sort - size 1000')
print("Unsorted: ", bubble_array2[0:10])
start_time = time.time() #Get time at start of sort
bubble_sort(bubble_array2)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Unsorted: ', bubble_array2[0:10])
print('Time elapsed: ', time_elapsed)

bubble_array2.sort()
bubble_sorted2 = bubble_array2
print('Sorted: ', bubble_sorted2[0:10])
start_time = time.time() #Get time at start of sort
bubble_sort(bubble_sorted2)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Sorted: ', bubble_sorted2[0:10])
print('Time elapsed: ', time_elapsed)

bubble_sorted_reverse2 = bubble_array2[::-1]
print('Reverse sorted: ', bubble_sorted_reverse2[0:10])
start_time = time.time() #Get time at start of sort
bubble_sort(bubble_sorted_reverse2)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Reverse sorted: ', bubble_sorted_reverse2[0:10])
print('Time elapsed: ', time_elapsed)

# merge sort size 1,000
print('\nMerge Sort - size 1,000')
print("Unsorted: ", merge_array2[0:10])
start_time = time.time() #Get time at start of sort
merge_sort(merge_array2)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Unsorted: ', merge_array2[0:10])
print('Time elapsed: ', time_elapsed)

merge_array2.sort()
merge_sorted2 = merge_array2
print('Sorted: ', merge_array2[0:10])
start_time = time.time() #Get time at start of sort
merge_sort(merge_sorted2)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Sorted: ', merge_sorted2[0:10])
print('Time elapsed: ', time_elapsed)

merge_sorted_reverse2 = merge_array2[::-1]
print('Reverse sorted: ', merge_sorted_reverse2[0:10])
start_time = time.time() #Get time at start of sort
merge_sort(merge_sorted_reverse2)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Reverse sorted: ', merge_sorted_reverse2[0:10])
print('Time elapsed: ', time_elapsed)

# quick sort size 1,000
print('\nQuick Sort - size 1,000')
print("Unsorted: ", quick_array2[0:10])
start_time = time.time() #Get time at start of sort
quick_sort(quick_array2)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Unsorted: ', quick_array2[0:10])
print('Time elapsed: ', time_elapsed)

quick_array2.sort()
quick_sorted2 = quick_array2
print('Sorted: ', quick_sorted2[0:10])
start_time = time.time() #Get time at start of sort
quick_sort(quick_sorted2)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test sorted: ', quick_sorted2[0:10])
print('Time elapsed: ', time_elapsed)

quick_sorted_reverse2 = quick_array2[::-1]
print('Reverse sorted: ', quick_sorted_reverse2[0:10])
start_time = time.time() #Get time at start of sort
quick_sort(quick_sorted_reverse2)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Reverse sorted: ', quick_sorted_reverse2[0:10])
print('Time elapsed: ', time_elapsed)

# extra sort size 1,000
print('\nShell Sort - size 1,000')
print("Unsorted: ", shell_array2[0:10])
start_time = time.time() #Get time at start of sort
shell_sort(shell_array2, 1000)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print("Test Unsorted: ", shell_array2[0:10])
print('Time elapsed: ', time_elapsed)

shell_array2.sort()
shell_sorted2 = shell_array2
print('Sorted: ', shell_sorted2[0:10])
start_time = time.time() #Get time at start of sort
shell_sort(shell_sorted2, 1000)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Sorted: ', shell_sorted2[0:10])
print('Time elapsed: ', time_elapsed)

shell_sorted_reverse2 = shell_array2[::-1]
print('Reverse sorted: ', shell_sorted_reverse2[0:10])
start_time = time.time() #Get time at start of sort
shell_sort(shell_sorted_reverse2, 1000)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Reverse sorted: ', shell_sorted_reverse2[0:10])
print('Time elapsed: ', time_elapsed)

print('\n-----------------------------------------------------------------------------------------')

################## make array of size 10,000 ##################
bubble_array3 = []
for num in range(10000):
    bubble_array3.append(random.randint(1, 100000)) 
    
# make copies for the other sorts 
merge_array3 = numpy.copy(bubble_array3)
quick_array3 = numpy.copy(bubble_array3)
shell_array3 = numpy.copy(bubble_array3)

# bubble sort size 10,000 
print('\nBubble Sort - size 10,000')
print("Unsorted: ", bubble_array3[0:10])
start_time = time.time() #Get time at start of sort
bubble_sort(bubble_array3)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Unsorted: ', bubble_array3[0:10])
print('Time elapsed: ', time_elapsed)

bubble_array3.sort()
bubble_sorted3 = bubble_array3
print('Sorted: ', bubble_sorted3[0:10])
start_time = time.time() #Get time at start of sort
bubble_sort(bubble_sorted3)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Sorted: ', bubble_sorted3[0:10])
print('Time elapsed: ', time_elapsed)

bubble_sorted_reverse3 = bubble_array3[::-1]
print('Reverse sorted: ', bubble_sorted_reverse3[0:10])
start_time = time.time() #Get time at start of sort
bubble_sort(bubble_sorted_reverse3)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Reverse sorted: ', bubble_sorted_reverse3[0:10])
print('Time elapsed: ', time_elapsed)

# merge sort size 10,000
print('\nMerge Sort - size 10,000')
print("Unsorted: ", merge_array3[0:10])
start_time = time.time() #Get time at start of sort
merge_sort(merge_array3)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Unsorted: ', merge_array3[0:10])
print('Time elapsed: ', time_elapsed)

merge_array3.sort()
merge_sorted3 = merge_array3
print('Sorted: ', merge_array3[0:10])
start_time = time.time() #Get time at start of sort
merge_sort(merge_sorted3)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Sorted: ', merge_sorted3[0:10])
print('Time elapsed: ', time_elapsed)

merge_sorted_reverse3 = merge_array3[::-1]
print('Reverse sorted: ', merge_sorted_reverse3[0:10])
start_time = time.time() #Get time at start of sort
merge_sort(merge_sorted_reverse3)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Reverse sorted: ', merge_sorted_reverse3[0:10])
print('Time elapsed: ', time_elapsed)

# quick sort size 10,000
#print('\nQuick Sort - size 10,000')
#print("Unsorted: ", quick_array3[0:10])
#start_time = time.time() #Get time at start of sort
#quick_sort(quick_array3)
#end_time = time.time() #Get time at end of sort
#time_elapsed = end_time - start_time #Calculate time elapsed
#print('Test Unsorted: ', quick_array3[0:10])
#print('Time elapsed: ', time_elapsed)

#quick_array3.sort()
#quick_sorted3 = quick_array3
#print('Sorted: ', quick_sorted3[0:10])
#start_time = time.time() #Get time at start of sort
#quick_sort(quick_sorted3)
#end_time = time.time() #Get time at end of sort
#time_elapsed = end_time - start_time #Calculate time elapsed
#print('Test sorted: ', quick_sorted3[0:10])
##print('Time elapsed: ', time_elapsed)

#quick_sorted_reverse3 = quick_array3[::-1]
#print('Reverse sorted: ', quick_sorted_reverse3[0:10])
#start_time = time.time()
#quick_sort(quick_sorted_reverse3)
#end_time = time.time() #Get time at end of sort
#time_elapsed = end_time - start_time #Calculate time elapsed
#print('Test Reverse sorted: ', quick_sorted_reverse3[0:10])
#print('Time elapsed: ', time_elapsed)

# extra sort size 10,000
print('\nShell Sort - size 10,000')
print("Unsorted: ", shell_array3[0:10])
start_time = time.time() #Get time at start of sort
shell_sort(shell_array3, 10000)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print("Test Unsorted: ", shell_array3[0:10])
print('Time elapsed: ', time_elapsed)

shell_array3.sort()
shell_sorted3 = shell_array3
print('Sorted: ', shell_sorted3[0:10])
start_time = time.time() #Get time at start of sort
shell_sort(shell_sorted3, 10000)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Sorted: ', shell_sorted3[0:10])
print('Time elapsed: ', time_elapsed)

shell_sorted_reverse3 = shell_array3[::-1]
print('Reverse sorted: ', shell_sorted_reverse3[0:10])
start_time = time.time() #Get time at start of sort
shell_sort(shell_sorted_reverse3, 10000)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Reverse sorted: ', shell_sorted_reverse3[0:10])
print('Time elapsed: ', time_elapsed)

#############################################################

print('\n-----------------------------------------------------------------------------------------')

################## make array of size 100,000 ##################
bubble_array4 = []
for num in range(100000):
    bubble_array4.append(random.randint(1, 1000000)) 
    
# make copies for the other sorts 
merge_array4 = numpy.copy(bubble_array4)
quick_array4 = numpy.copy(bubble_array4)
shell_array4 = numpy.copy(bubble_array4)

# bubble sort size 100,000
#print('\nBubble Sort - size 100,000')
#print("Unsorted: ", bubble_array4[0:10])
#start_time = time.time() #Get time at start of sort
#bubble_sort(bubble_array4)
#end_time = time.time() #Get time at end of sort
#time_elapsed = end_time - start_time #Calculate time elapsed
#print('Test Unsorted: ', bubble_array4[0:10])
#print('Time elapsed: ', time_elapsed)

#bubble_array4.sort()
#bubble_sorted4 = bubble_array4
#print('Sorted: ', bubble_sorted4[0:10])
#start_time = time.time() #Get time at start of sort
#bubble_sort(bubble_sorted4)
#end_time = time.time() #Get time at end of sort
#time_elapsed = end_time - start_time #Calculate time elapsed
#print('Test Sorted: ', bubble_sorted4[0:10])
#print('Time elapsed: ', time_elapsed)

#bubble_sorted_reverse4 = bubble_array4[::-1]
#print('Reverse sorted: ', bubble_sorted_reverse4[0:10])
#start_time = time.time() #Get time at start of sort
#bubble_sort(bubble_sorted_reverse4)
#end_time = time.time() #Get time at end of sort
#time_elapsed = end_time - start_time #Calculate time elapsed
#print('Test Reverse sorted: ', bubble_sorted_reverse4[0:10])
#print('Time elapsed: ', time_elapsed)

# merge sort size 100,000
print('\nMerge Sort - size 100,000')
print("Unsorted: ", merge_array4[0:10])
start_time = time.time() #Get time at start of sort
merge_sort(merge_array4)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Unsorted: ', merge_array4[0:10])
print('Time elapsed: ', time_elapsed)

merge_array4.sort()
merge_sorted4 = merge_array4
print('Sorted: ', merge_array4[0:10])
start_time = time.time() #Get time at start of sort
merge_sort(merge_sorted4)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Sorted: ', merge_sorted4[0:10])
print('Time elapsed: ', time_elapsed)

merge_sorted_reverse4 = merge_array4[::-1]
print('Reverse sorted: ', merge_sorted_reverse4[0:10])
start_time = time.time() #Get time at start of sort
merge_sort(merge_sorted_reverse4)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Reverse sorted: ', merge_sorted_reverse4[0:10])
print('Time elapsed: ', time_elapsed)

# quick sort size 100,000
print("Unsorted: ", quick_array4[0:10])
start_time = time.time() #Get time at start of sort
quick_sort(quick_array4)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Unsorted: ', quick_array4[0:10])
print('Time elapsed: ', time_elapsed)

#quick_array4.sort()
#quick_sorted4 = quick_array4
#print('Sorted: ', quick_sorted4[0:10])
#start_time = time.time() #Get time at start of sort
#quick_sort(quick_sorted4)
#end_time = time.time() #Get time at end of sort
#time_elapsed = end_time - start_time #Calculate time elapsed
#print('Test sorted: ', quick_sorted4[0:10])
#print('Time elapsed: ', time_elapsed)

#quick_sorted_reverse4 = quick_array4[::-1]
#print('Reverse sorted: ', quick_sorted_reverse4[0:10])
#start_time = time.time() #Get time at start of sort
#quick_sort(quick_sorted_reverse4)
#end_time = time.time() #Get time at end of sort
#time_elapsed = end_time - start_time #Calculate time elapsed
#print('Test Reverse sorted: ', quick_sorted_reverse4[0:10])
#print('Time elapsed: ', time_elapsed)

# extra sort size 100,000
print('\nShell Sort - size 100,000')
print("Unsorted: ", shell_array4[0:10])
start_time = time.time() #Get time at start of sort
shell_sort(shell_array4, 100000)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print("Test Unsorted: ", shell_array4[0:10])
print('Time elapsed: ', time_elapsed)

shell_array4.sort()
shell_sorted4 = shell_array4
print('Sorted: ', shell_sorted4[0:10])
start_time = time.time()
shell_sort(shell_sorted4, 100000)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Sorted: ', shell_sorted4[0:10])
print('Time elapsed: ', time_elapsed)

shell_sorted_reverse4 = shell_array4[::-1]
print('Reverse sorted: ', shell_sorted_reverse4[0:10])
start_time = time.time() #Get time at start of sort
shell_sort(shell_sorted_reverse4, 100000)
end_time = time.time() #Get time at end of sort
time_elapsed = end_time - start_time #Calculate time elapsed
print('Test Reverse sorted: ', shell_sorted_reverse4[0:10])
print('Time elapsed: ', time_elapsed)

print('\n-----------------------------------------------------------------------------------------')

################## make array of size 100,000 ##################
bubble_array5 = []
for num in range(100000):
    bubble_array5.append(random.randint(1, 1000000)) 
    
# make copies for the other sorts 
merge_array5 = numpy.copy(bubble_array5)
quick_array5 = numpy.copy(bubble_array5)
shell_array5 = numpy.copy(bubble_array5)

# # bubble sort size 1,000,000 
# print('\nBubble Sort - size 1,000,000')
# print("Unsorted: ", bubble_array5[0:10])
# #print('Testing: ')
# #Starting timer goes here
# #(bubble_array5)
# #print('Test Unsorted: ', bubble_array5[0:10])

# bubble_array5.sort()
# bubble_sorted5 = bubble_array5
# print('Sorted: ', bubble_sorted5[0:10])
# bubble_sorted_reverse5 = bubble_array5[::-1]
# print('Reverse sorted: ', bubble_sorted_reverse5[0:10])


# # merge sort size 1,000,000
#print('\nMerge Sort - size 1,000,000')
#print("Unsorted: ", merge_array5[0:10])
#merge_array5.sort()
#merge_sorted5 = merge_array5
#print('Sorted: ', merge_array5[0:10])
#merge_sorted_reverse5 = merge_array5[::-1]
#print('Reverse sorted: ', merge_sorted_reverse5[0:10])

# # quick sort size 1,000,000
# print('\nQuick Sort - size 1,000,000')
# print("Unsorted: ", quick_array5[0:10])
# quick_array5.sort()
# quick_sorted5 = quick_array5
# print('Sorted: ', quick_array5[0:10])
# quick_sorted_reverse5 = quick_array5[::-1]
# print('Reverse sorted: ', quick_sorted_reverse5[0:10])

# # extra sort size 1,000,000
# print('\nShell Sort - size 1,000,000')
# print("Unsorted: ", shell_array5[0:10])
# shell_array5.sort()
# shell_sorted5 = shell_array5
# print('Sorted: ', shell_array5[0:10])
# shell_sorted_reverse5 = shell_array5[::-1]
# print('Reverse sorted: ', shell_sorted_reverse5[0:10])
# #############################################################

