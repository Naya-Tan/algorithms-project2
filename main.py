# project 2: analyzing and verifying asymptotic time complexity of sorting algorithms 

import random
from numpy import*
import numpy 


# bubble sort 
# merge sort 
# quick sort 
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
    bubble_array.append(random.randrange(1, 1000000))
    
bubble_sorted = bubble_array.sort()
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