from operator import attrgetter
from read_csv import read_csv
from sort import bubble_sort
from chess_player import Chessplayer

def binary_search(array, element):
   
    low = 0
    high = len(array) - 1
    count = 0

    while low <= high:
        # divide list into half while low is still less than high
        middle = low + (high - low) // 2

        if array[middle] == element:
            print('Number of tries: ' + str(count))
            return middle

        elif array[middle] < element:
            low = middle + 1

        else:
            high = middle - 1
        count += 1

    # print('Number of searching: ' + str(count))
    return -1


# find players by attribute
def identity(element):
    return element


def find_index(elements, value, key):
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


def find(elements, value, key=identity):
    index = find_index(elements, value, key)
    return None if index is None else elements[index]


    
