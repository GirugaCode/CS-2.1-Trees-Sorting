#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # Traverse through the items with the amount on indexes
    for item in range(len(items) - 1):
        if items[item] > items[item + 1]: # Check if next item is greater than previous
            return False
    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Best running time: O(n) where n is sorting a list that is sorted
    Worst running time: O(n^2) where n is sorting out a very unsorted list 
    TODO: Memory usage: ??? Why and under what conditions?"""
    num_items = len(items) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for item in range(num_items):
            if items[item] > items[item + 1]:
                is_sorted = False
                items[item], items[item + 1] = items[item + 1], items[item]
        if is_sorted:
            break


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Best running time: O(n^2) where n is going through the list twice to find sub_item
    Worst running time: O(n^2) where n is going through the list twice to find sub_item
    TODO: Memory usage: ??? Why and under what conditions?"""
    for item in range(len(items)):
        minimum = item
        for sub_item in range(item, len(items)):
            if items[sub_item] < items[minimum]:
                minimum = sub_item
        items[minimum], items[item] = items[item], items[minimum] 

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Best running time: O(n) where n only sorts one item
    Worst running time: O(n^2) where n is going through the list twice to find sub_items
    TODO: Memory usage: ??? Why and under what conditions?"""

    for item in range(len(items)): # Traverse through length of array, starting with the element at index 0.
        current_unsorted_item = items[item] # Assumes the first item is sorted
        sub_item = item - 1 # Assignment of the next item in array
        
        # Continue through the array for items[0 -> item - 1] 
        while sub_item >= 0 and current_unsorted_item < items[sub_item]:
            items[sub_item + 1] = items[sub_item] 
            sub_item -= 1 
        items[sub_item + 1] = current_unsorted_item # Set the sub_item in the sorted section

