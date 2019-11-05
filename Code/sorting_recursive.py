#!python
from sorting_iterative import bubble_sort, selection_sort, insertion_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Runtime: O(n) where n is the number of items we put into the item_result
    Memory Usage: O(n) where n is the space that is appended into the item_result"""
    item_result = []
    while items1 or items2:
        if not items2 or items1 and items1[0] < items2[0]:
            item_result.append(items1.pop(0))
        else:
            item_result.append(items2.pop(0))
    return item_result

    # Method Two
    # num_items1 = len(items1)
    # num_items2 = len(items2)

    # item_result = []
    # items1_pointer = 0
    # items2_pointer = 0

    # while items1_pointer < num_items1 and items2_pointer < num_items2:
    #     if items1[items1_pointer] < items2[items2_pointer]:
    #         item_result.append(items1[items1_pointer])
    #         items1_pointer += 1
    #     else:
    #         item_result.append(items2[items2_pointer])
    #         items2_pointer += 1
    # return item_result


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running Time: O(n^2) because of using bubble_sort and insertion_sort
    Memory Usage: O(n) where n is the amount of items you are merging together"""
    middle = len(items) // 2
    left = bubble_sort(items[:middle]) # Sorting the items on the left 
    right = insertion_sort(items[middle:]) # Sorting the items on the right

    sorted_items = merge(left, right)

    # Sets the sorted items in the list
    for index in range(len(items)):
        items[index] = sorted_items[index]

    return items
    



def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running Time: O(n*logn) Using the merge function is O(n) and recursivly spliting the array in merge_sort is O(logn)
    Memory Usage: O(n) where n is the amount of items you are merging together"""

    # Base Case
    if len(items) < 2:
        return items
    
    middle = len(items) // 2
    left = merge_sort(items[:middle]) # Marks every item on the left of the array
    right = merge_sort(items[middle:]) # Marks every item on the right of the array

    # Merges the seperate items together
    sorted_items = merge(left, right) 

    # Mutates the sorted items in the list
    items[:] = sorted_items

    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (Choosing the first element as the pivot) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Best case running time: O(n*logn) where the pivot index creates a balanced tree. Each level of the tree is partitioned
    Worst case running time: O(n^2) where the pivot index is bad and the recursion depth of the tree is deep
    Best Case Memory usage: O(1) Where memory is in-place but technically O(logn) to store pointers"""

    pivot_index = items[low] # Choosing the low value as my pivot
    swapped_index = low + 1 # Keep track of how many times i've swapped

    for item in range(low, high): # Iterate through low to high of items 
        if items[item] < pivot_index: # Compare the element to our pivot
            items[item], items[swapped_index] = items[swapped_index], items[item] # Swap
            swapped_index += 1 # Continue the iteration

    # Move the pivot items into the final positions
    items[low], items[swapped_index - 1] = items[swapped_index - 1], items[low]

    # Return the partitioned index
    return swapped_index - 1



def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: O(n*logn) where the pivot index creates a balanced tree. Each level of the tree is partitioned
    Worst case running time: O(n^2) where the pivot index is bad and the recursion depth of the tree is deep
    Best Case Memory usage: O(1) Where memory is in-place but technically O(logn) to store pointers """

    # To avoid None Types, assign low and high to its appropriate index
    if high is None and low is None:
        high = len(items)
        low = 0
        
    # Base case, if the list is 1 or none then it is already sorted
    if (high - low) < 2:
        return

    # Partition the items in place
    pivot_index = partition(items, low, high)

    # Recursivly call quick_sort with a new pivot_index each time
    quick_sort(items, low, pivot_index)
    quick_sort(items, pivot_index + 1, high)