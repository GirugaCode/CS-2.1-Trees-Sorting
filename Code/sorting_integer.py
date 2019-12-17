#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n) where n is the amount of number
    Memory usage: O(n) where n is the amount of number"""
    minimum = min(numbers)
    maximum = max(numbers)

    # Create list of counts with a slot for each number in input range
    number_list = [0 for _ in range(minimum, maximum + 1)]

    # Loop over given numbers and increment each number's count
    for num in numbers:
        number_list[num - minimum] += 1 

    # Iterate over counts and append to results
    result = []
    for i, count in enumerate(number_list):
        if count == 0:
            continue

        num = i + minimum
        result.extend([num] * count)
    
    numbers[:] = result
    return result
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
