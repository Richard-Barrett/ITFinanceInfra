#!/bin/usr/ python

import math
import numbers
import operator
import itertools

number_list=[20.5,30.5,40.5,5.5,3]

def round_list_percentages(number_list):
    """
    Takes a list where all values are numbers that add up to 100,
    and rounds them off to integers while still retaining a sum of 100.

    A total value sum that rounds to 100.00 with two decimals is acceptable.
    This ensures that all input where the values are calculated with [fraction]/[total]
    and the sum of all fractions equal the total, should pass.
    """
    # Check input
    if not all(isinstance(i, numbers.Number) for i in number_list):
        raise ValueError('All values of the list must be a number')

    # Generate a key for each value
    key_generator = itertools.count()
    value_dict = {next(key_generator): value for value in number_list}
    return round_dictionary_percentages(value_dict).values()


def round_dictionary_percentages(dictionary):
    """
    Takes a dictionary where all values are numbers that add up to 100,
    and rounds them off to integers while still retaining a sum of 100.

    A total value sum that rounds to 100.00 with two decimals is acceptable.
    This ensures that all input where the values are calculated with [fraction]/[total]
    and the sum of all fractions equal the total, should pass.
    """
    # Check input
    # Only allow numbers
    if not all(isinstance(i, numbers.Number) for i in dictionary.values()):
        raise ValueError('All values of the dictionary must be a number')
    # Make sure the sum is close enough to 100
    # Round value_sum to 2 decimals to avoid floating point representation errors
    value_sum = round(sum(dictionary.values()), 2)
    if not value_sum == 100:
        raise ValueError('The sum of the values must be 100')

    # Initial floored results
    # Does not add up to 100, so we need to add something
    result = {key: int(math.floor(value)) for key, value in dictionary.items()}

    # Remainders for each key
    result_remainders = {key: value % 1 for key, value in dictionary.items()}
    # Keys sorted by remainder (biggest first)
    sorted_keys = [key for key, value in sorted(result_remainders.items(), key=operator.itemgetter(1), reverse=True)]

    # Otherwise add missing values up to 100
    # One cycle is enough, since flooring removes a max value of < 1 per item,
    # i.e. this loop should always break before going through the whole list
    for key in sorted_keys:
        if sum(result.values()) == 100:
            break
        result[key] += 1

    # Return
    return result

print(number_list)
print(round_list_percentages(number_list))
