#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # [3,6,1,2,12,4] 
    curr_item = 0
    for _ in range(1, len(items)):
        if items[curr_item] > items[curr_item + 1]:
            return False
        curr_item += 1
    return True

    # First Approach 
        # for _ in items:
        #     if items[tracker] > items[tracker + 1]:
        #         return False
        #     tracker += 1
        # return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    num_items = len(items) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for item in range(num_items):
            if items[item] > items[item + 1]:
                is_sorted = False
                items[item], items[item + 1] = items[item + 1], items[item]


    # curr_item = 0
    # for _ in range(1, len(items)):
    #     if items[curr_item] < items[curr_item + 1]:
    #         items[curr_item], items[curr_item + 1] = items[curr_item + 1], items[curr_item]
    #     curr_item += 1
    # return items



def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
