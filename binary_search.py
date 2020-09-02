from operator import attrgetter
from read_csv import read_csv


def identity(element):
    return element

def find_index(elements, value, key:str)->int:
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = key(elements[middle])

        if middle_element == value:
            return middle

        if middle_element < value:
            left = middle + 1
        elif middle_element > value:
            right = middle - 1


def find_leftmost_index(elements, value, key=identity):
    index = find_index(elements, value, key)
    if index is not None:
        while index >= 0 and key(elements[index]) == value:
            index -= 1
        index += 1
    return index


def find_rightmost_index(elements, value, key=identity):
    index = find_index(elements, value, key)
    if index is not None:
        while index < len(elements) and key(elements[index]) == value:
            index += 1
        index -= 1
    return index


def find_all_indices(elements, value, key=identity):
    left = find_leftmost_index(elements, value, key)
    right = find_rightmost_index(elements, value, key)
    if left and right:
        return set(range(left, right + 1))
    return set()


def find_leftmost(elements, value, key=identity):
    index = find_leftmost_index(elements, value, key)
    return None if index is None else elements[index]


def find_rightmost(elements, value, key=identity):
    index = find_rightmost_index(elements, value, key)
    return None if index is None else elements[index]


def find_all(elements, value, key=identity):
    return {elements[i] for i in find_all_indices(elements, value, key)}


def find(elements, value, key=identity):
    index = find_index(elements, value, key)
    # if index is not None:
    #     print("player is found at ", index)
    #     return index
    # return None
    return None if index is None else elements[index]

by_full_name = attrgetter('full_name')
arr = read_csv('chess-players.csv')
arr.sort(key=by_full_name)
result = find(arr, value='Šarūnas Šulskis', key=by_full_name)
if (result == -1): 
    print("Element not present") 
else: 
    print("Element found at index", result) 
