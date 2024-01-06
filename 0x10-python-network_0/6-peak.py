#!/usr/bin/python3
"""Defines an algorithm finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers is None or list_of_integers == []:
        return None
    midv = int(len(list_of_integers) / 2)
    if len(list_of_integers) % 2 == 0:
        midv = midv - 1
    middlev = list_of_integers[midv]
    low = list_of_integers[0]
    high = list_of_integers[-1]
    if middlev is low and middlev is high:
        return middlev
    if middlev is low and middlev > list_of_integers[midv + 1]:
        return middlev
    if middlev > list_of_integers[midv + 1]:
        if middlev > list_of_integers[midv - 1]:
            return middlev
        else:
            peak_low = find_peak(list_of_integers[:midv])
            if peak_low is not None:
                return peak_low
    else:
        peak_high = find_peak(list_of_integers[(midv + 1):])
        if peak_high is not None:
            return peak_high
